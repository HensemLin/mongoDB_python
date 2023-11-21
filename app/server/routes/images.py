from fastapi import APIRouter, status, UploadFile, File, Form, HTTPException
from beanie import PydanticObjectId
from bson.binary import Binary
from beanie import BsonBinary
from ..utils.pydantic_encoder import encode_input
from ..models import Images


router = APIRouter(tags=["Images"], prefix="/images")


@router.post("/", status_code=status.HTTP_201_CREATED)
async def upload_image(
    filename: str = Form(...),
    description: str = Form(...),
    file: UploadFile = File(...)
):
    file_data = await file.read()
    encoded = BsonBinary(file_data)
    images_document = Images(
        filename=filename,
        description=description,
        file=encoded
    )
    await images_document.insert()
    return {"id": str(images_document.id), "filename": images_document.filename, "description": images_document.description}

@router.get("/{id}")
async def get_image(id: PydanticObjectId):
    print(id)
    images = await Images.get(id)
    if not images:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Book with id {id} not found"
        )
    print(images)
    return "hello"
