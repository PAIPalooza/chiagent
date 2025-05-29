from sqlalchemy import Column, String, JSON, DateTime, text
import uuid
from datetime import datetime

from app.models.base import Base

class AddressUpdate(Base):
    """
    Database model for tracking address update requests.
    """
    __tablename__ = "address_updates"

    id = Column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        unique=True,
        nullable=False,
        comment="UUID as string for SQLite compatibility"
    )
    order_id = Column(String, nullable=False, index=True, comment="The ID of the order being updated")
    platform = Column(String, nullable=False, comment="Platform where the order was placed")
    shipping_address = Column(JSON, nullable=False, comment="New shipping address details")
    billing_address = Column(JSON, nullable=True, comment="New billing address details (if different from shipping)")
    status = Column(String, nullable=False, default="pending", comment="Status of the address update")
    created_at = Column(DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<AddressUpdate {self.id} for order {self.order_id}>"
