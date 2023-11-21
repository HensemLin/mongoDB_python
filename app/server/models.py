from beanie import Document
from pydantic import BaseModel
from typing import List, Optional
from bson.binary import Binary
from fastapi import Form

class Book(Document):
    title: str
    author: str
    published_year: int
    reviews: list[str] = []

    class Settings:
        name = "books"

    class Config:
        json_schema_extra = {
            "example": {
                "title": "The Great Gatsby",
                "author": "F. Scott Fitzgerald",
                "published_year": 1925,
                "reviews": ["Excellent course!"],
            }
        }

class UpdateBook(BaseModel):
    title: Optional[str]
    author: Optional[str]
    published_year: int

class Images(Document):
    filename: str
    description: str
    file: Binary  # Use Binary to store binary data

    class Settings:
        name = "images"

    class Config:
        arbitrary_types_allowed = True
