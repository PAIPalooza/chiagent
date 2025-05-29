# Import models here to make them available when importing from app.models
from app.models.base import Base
from app.models.refund_request import RefundRequest

# This makes the models available for SQLAlchemy to discover them
__all__ = ["Base", "RefundRequest"]
