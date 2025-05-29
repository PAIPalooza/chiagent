from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from datetime import datetime
from uuid import UUID

class RefundRequestBase(BaseModel):
    order_id: str = Field(..., description="The ID of the order to be refunded")
    platform: str = Field(..., description="The platform where the order was placed", example="shopify")
    amount: Optional[float] = Field(None, description="Amount to refund (if different from order total)")
    reason: Optional[str] = Field(None, description="Reason for the refund")
    items: Optional[list[dict[str, Any]]] = Field(None, description="Specific items to refund")

class RefundRequestCreate(RefundRequestBase):
    pass

class RefundRequestInDB(RefundRequestBase):
    id: UUID
    status: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class RefundResponse(BaseModel):
    status: str = Field(..., description="Status of the refund request", example="pending")
