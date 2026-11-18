from itertools import count

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Building REST APIs with FastAPI")


class BookCreate(BaseModel):
    title: str
    author: str


class Book(BookCreate):
    id: int


books: dict[int, Book] = {}
book_ids = count(1)
