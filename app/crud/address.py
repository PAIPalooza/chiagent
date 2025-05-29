from sqlalchemy.orm import Session
from typing import Any, Dict, List, Optional
import uuid
from datetime import datetime

from app.models import AddressUpdate
from app.schemas.address import AddressUpdateCreate

def create_address_update(
    db: Session,
    order_id: str,
    platform: str,
    shipping_address: dict,
    billing_address: dict = None,
    status: str = "pending"
) -> AddressUpdate:
    """
    Create a new address update record in the database.
    
    Args:
        db: Database session
        order_id: ID of the order to update
        platform: Platform where the order was placed
        shipping_address: New shipping address details
        billing_address: New billing address details (optional)
        status: Status of the address update (default: "pending")
        
    Returns:
        AddressUpdate: The created address update record
    """
    # Create the database model instance
    db_address_update = AddressUpdate(
        order_id=order_id,
        platform=platform,
        shipping_address=shipping_address,
        billing_address=billing_address,
        status=status,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    
    # Add to session and commit
    db.add(db_address_update)
    try:
        db.commit()
        db.refresh(db_address_update)
        return db_address_update
    except Exception as e:
        db.rollback()
        logger.error(f"Error creating address update: {str(e)}")
        raise

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
