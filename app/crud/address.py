from sqlalchemy.orm import Session
from typing import Dict, Any
import uuid
from datetime import datetime

from app.models import AddressUpdate

def create_address_update(
    db: Session,
    order_id: str,
    platform: str,
    shipping_address: Dict[str, Any],
    billing_address: Dict[str, Any] = None
) -> AddressUpdate:
    """
    Create a new address update request in the database.
    """
    db_address_update = AddressUpdate(
        id=uuid.uuid4(),
        order_id=order_id,
        platform=platform,
        shipping_address=shipping_address,
        billing_address=billing_address,
        status="pending",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    
    db.add(db_address_update)
    db.commit()
    db.refresh(db_address_update)
    return db_address_update

def get_address_update(db: Session, address_update_id: str) -> AddressUpdate:
    """
    Get an address update request by ID.
    """
    return db.query(AddressUpdate).filter(AddressUpdate.id == address_update_id).first()

def get_address_updates_by_order(db: Session, order_id: str, skip: int = 0, limit: int = 100):
    """
    Get all address update requests for a specific order.
    """
    return (
        db.query(AddressUpdate)
        .filter(AddressUpdate.order_id == order_id)
        .offset(skip)
        .limit(limit)
        .all()
    )

def update_address_update_status(
    db: Session, 
    address_update_id: str, 
    status: str
) -> AddressUpdate:
    """
    Update the status of an address update request.
    """
    db_address_update = get_address_update(db, address_update_id)
    if db_address_update:
        db_address_update.status = status
        db_address_update.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(db_address_update)
    return db_address_update
