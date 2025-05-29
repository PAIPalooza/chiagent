from sqlalchemy import Boolean, Column, String, DECIMAL, TIMESTAMP, text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class PlatformProduct(Base):
    __tablename__ = "platform_product"

    sku = Column(String(100), primary_key=True)
    platform = Column(String(50), primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(String())
    product_metadata = Column(JSONB)
    price = Column(DECIMAL(10, 2), nullable=False)
    available = Column(Boolean, nullable=False, server_default=text("true"))
    synced_at = Column(TIMESTAMP(timezone=True))
