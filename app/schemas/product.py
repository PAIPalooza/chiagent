from typing import Optional, List
from pydantic import BaseModel

class ProductSearch(BaseModel):
    q: str
    filters: Optional[dict] = None

class ProductResponse(BaseModel):
    sku: str
    platform: str
    title: str
    description: Optional[str]
    product_metadata: Optional[dict]
    price: float
    available: bool
    synced_at: Optional[str]

class ProductListResponse(BaseModel):
    products: List[ProductResponse]
    total: int
    page: int
    per_page: int
