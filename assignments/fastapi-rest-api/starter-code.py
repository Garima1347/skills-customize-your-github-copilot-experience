from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Item API")


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float


items = []


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI item API"}


# TODO: Implement GET /items


# TODO: Implement POST /items


# TODO: Implement GET /items/{item_id}


# TODO: Implement PUT /items/{item_id}


# TODO: Implement DELETE /items/{item_id}
