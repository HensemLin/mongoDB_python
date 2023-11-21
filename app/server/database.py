from beanie import init_beanie
import motor.motor_asyncio

from .models import Book, Images


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(
        "mongodb://localhost:27017"
    )
    await init_beanie(database=client.db_name, document_models=[Book, Images])