from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="API REST Test - Andres Pino")

# Modelo de datos
class Item(BaseModel):
    id: int
    name: str
    price: float
    available: bool = True

# Base de datos en memoria
items_db: List[Item] = []

# Creación de endpoints
# Traer todos los items
@app.get("/items", response_model=List[Item])
def get_items():
    return items_db

# Crear un nuevo item
@app.post("/items", response_model=Item)
def create_item(item: Item):
    for existing in items_db:
        if existing.id == item.id:
            raise HTTPException(status_code=400, detail="Item already exists")
    items_db.append(item)
    return item

# Traer un item específico
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

# Actualizar un item específico
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated: Item):
    for i, item in enumerate(items_db):
        if item.id == item_id:
            items_db[i] = updated
            return updated
    raise HTTPException(status_code=404, detail="Item not found")

# Eliminar un item específico
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for i, item in enumerate(items_db):
        if item.id == item_id:
            items_db.pop(i)
            return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")
