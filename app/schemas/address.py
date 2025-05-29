from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from datetime import datetime
from uuid import UUID

class AddressUpdateRequest(BaseModel):
    """Schema for address update request."""
    order_id: str = Field(..., description="The ID of the order to update address for")
    platform: str = Field(..., description="The platform where the order was placed", example="shopify")
    shipping_address: Dict[str, Any] = Field(
        ...,
        description="The new shipping address details",
        example={
            "first_name": "John",
            "last_name": "Doe",
            "address1": "123 Main St",
            "city": "San Francisco",
            "province": "CA",
            "country": "United States",
            "zip": "94105",
            "phone": "+14155551234"
        }
    )
    billing_address: Optional[Dict[str, Any]] = Field(
        None,
        description="The new billing address details (if different from shipping)",
        example={
            "first_name": "John",
            "last_name": "Doe",
            "address1": "123 Main St",
            "city": "San Francisco",
            "province": "CA",
            "country": "United States",
            "zip": "94105",
            "phone": "+14155551234"
        }
    )

class AddressUpdateResponse(BaseModel):
    """Schema for address update response."""
    status: str = Field(..., description="Status of the address update request", example="pending")

class AddressUpdateCreate(AddressUpdateRequest):
    """Schema for creating a new address update record."""
    pass

class AddressUpdateInDB(AddressUpdateRequest):
    """Schema for address update record in database."""
    id: UUID
    status: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True
