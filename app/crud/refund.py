from sqlalchemy.orm import Session
from typing import Optional
import uuid
from datetime import datetime
from app.models.refund_request import RefundRequest as RefundRequestModel

def create_refund_request(
    db: Session, 
    order_id: str, 
    platform: str, 
    request_data: dict,
    status: str = "pending"
) -> RefundRequestModel:
    """
    Create a new refund request in the database
    """
    db_refund = RefundRequestModel(
        id=str(uuid.uuid4()),
        order_id=order_id,
        platform=platform,
        status=status,
        request_data=request_data,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    db.add(db_refund)
    db.commit()
    db.refresh(db_refund)
    return db_refund

def get_refund_request(db: Session, refund_id: str) -> Optional[RefundRequestModel]:
    """
    Get a refund request by ID
    """
    return db.query(RefundRequestModel).filter(RefundRequestModel.id == refund_id).first()

def update_refund_request_status(
    db: Session, 
    refund_id: str, 
    status: str, 
    response_data: Optional[dict] = None
) -> Optional[RefundRequestModel]:
    """
    Update the status of a refund request
    """
    db_refund = db.query(RefundRequestModel).filter(RefundRequestModel.id == refund_id).first()
    if db_refund:
        db_refund.status = status
        if response_data is not None:
            db_refund.response_data = response_data
        db_refund.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(db_refund)
    return db_refund
