from sqlalchemy import Column, String, JSON, DateTime, ForeignKey
import uuid
from datetime import datetime
from app.models.base import Base

class RefundRequest(Base):
    __tablename__ = "refund_requests"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    order_id = Column(String(100), nullable=False)
    platform = Column(String(50), nullable=False)  # 'shopify' or 'woocommerce'
    status = Column(String(20), nullable=False, default='pending')  # 'pending', 'processed', 'failed'
    request_data = Column(JSON, nullable=True)  # Store the full request payload
    response_data = Column(JSON, nullable=True)  # Store the response from the platform
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f"<RefundRequest {self.id} for order {self.order_id}>"
