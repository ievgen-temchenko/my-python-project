from typing import List, Optional
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# Pydantic models for request/response
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    is_available: bool = True

class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    is_available: bool = True

# In-memory storage (replace with database in production)
items_db = [
    Item(id=1, name="Laptop", description="High-performance laptop", price=999.99),
    Item(id=2, name="Mouse", description="Wireless mouse", price=29.99),
    Item(id=3, name="Keyboard", description="Mechanical keyboard", price=79.99),
]

@router.get("/", response_model=List[Item])
async def get_items():
    """Get all items - This is your public endpoint!"""
    return items_db

@router.get("/{item_id}", response_model=Item)
async def get_item(item_id: int):
    """Get a specific item by ID"""
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@router.post("/", response_model=Item)
async def create_item(item: ItemCreate):
    """Create a new item"""
    new_id = max(item.id for item in items_db) + 1 if items_db else 1
    new_item = Item(id=new_id, **item.dict())
    items_db.append(new_item)
    return new_item
