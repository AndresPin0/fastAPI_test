from fastapi import FastAPI, HTTPException
from typing import List
from models import Item
from seed_data import load_seed_data

app = FastAPI(title="API REST Test", redoc_url=None)

# Base de datos en memoria
items_db: List[Item] = []

@app.on_event("startup")
def startup_event():
    global items_db
    if not items_db:
        items_db = load_seed_data()

# Endpoints CRUD básicos

@app.get("/items", response_model=List[Item])
def get_items():
    return items_db

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items", response_model=Item)
def create_item(item: Item):
    for existing in items_db:
        if existing.id == item.id:
            raise HTTPException(status_code=400, detail="Item already exists")
    items_db.append(item)
    return item

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated: Item):
    for i, item in enumerate(items_db):
        if item.id == item_id:
            items_db[i] = updated
            return updated
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for i, item in enumerate(items_db):
        if item.id == item_id:
            items_db.pop(i)
            return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")
