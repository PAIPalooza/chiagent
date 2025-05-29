# Import models here to make them available when importing from app.models
from app.models.base import Base
from app.models.refund_request import RefundRequest
from app.models.address_update import AddressUpdate

# This makes the models available for SQLAlchemy to discover them
__all__ = ["Base", "RefundRequest", "AddressUpdate"]
