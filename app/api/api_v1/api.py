from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import platform_product
from app.schemas import product
from app.db.session import SessionLocal
from app.core.config import settings

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/search", response_model=product.ProductListResponse)
def search_products(
    q: str,
    page: int = 1,
    per_page: int = 10,
    db: Session = Depends(get_db)
):
    """
    Search for products using natural language query.
    Supports basic faceted search through query parameters.
    """
    # For now, return sample data
    sample_products = [
        {
            "sku": "SKU123",
            "platform": "shopify",
            "title": "Sample Product",
            "description": "This is a sample product description",
            "product_metadata": {},
            "price": 99.99,
            "available": True,
            "synced_at": "2025-05-30T00:00:00+05:30"
        }
    ]
    
    return {
        "products": sample_products,
        "total": len(sample_products),
        "page": page,
        "per_page": per_page
    }
