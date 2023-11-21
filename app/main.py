from fastapi import FastAPI
from .server.database import init_db
from .server.routes.book import router
from .server.routes.images import router as image_router

app = FastAPI()
app.include_router(router)
app.include_router(image_router)

@app.on_event("startup")
async def start_db():
    await init_db()

@app.get("/")
def main():
    return ({"message": "hello world"})

