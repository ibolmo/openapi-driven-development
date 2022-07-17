
from typing import List

import toml
import yaml
from fastapi import Body, FastAPI, status
from fastapi.responses import Response
from pydantic import BaseModel

app = FastAPI(version=toml.load('pyproject.toml')['tool']['poetry']['version'])

class Author(BaseModel):
    name: str

class Book(BaseModel):
    author: Author
    title: str

olmo = Author(name='Olmo Maldonado')
books = [Book(author=olmo, title="Where the red fern grows.")]

@app.get("/api/v1/books", responses={
    status.HTTP_200_OK: {'model': List[Book]},
})
async def get_books():
    return books


@app.post("/api/v1/books", responses={
    status.HTTP_201_CREATED: {'model': Book},
})
async def create_book(book: Book = Body(embed=True)):
    books.append(book)
    return book


# I like yaml or json, but whatever floats your boat!
@app.get('/openapi.yaml', include_in_schema=False)
def get_openapi_yaml():
    openapi_json= app.openapi()
    return Response(yaml.dump(openapi_json), media_type='text/yaml')
