import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.main import app
from app.db.session import Base, get_db
from app.models import AddressUpdate, Base
from app.models.address_update import AddressUpdate as AddressUpdateModel

# Import all models to ensure they are registered with SQLAlchemy
from app.models import *

# Create test database
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create test database tables
Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

# Create test client
client = TestClient(app)

# Create the test client
client = TestClient(app)

# Test data
TEST_ORDER_ID = "TEST123"
TEST_PLATFORM = "shopify"
TEST_SHIPPING_ADDRESS = {
    "first_name": "John",
    "last_name": "Doe",
    "address1": "123 Main St",
    "city": "San Francisco",
    "province": "CA",
    "country": "United States",
    "zip": "94105",
    "phone": "+14155551234"
}

# Fixture to set up and tear down the test database
@pytest.fixture(scope="function")
def test_db():
    # Create all tables
    Base.metadata.create_all(bind=engine)
    
    # Create a new database session
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        # Drop all tables after the test
        Base.metadata.drop_all(bind=engine)

def test_update_order_address_success(test_db: Session):
    # Ensure all tables are created
    Base.metadata.create_all(bind=engine)
    """Test successful address update request."""
    # Prepare test data
    request_data = {
        "order_id": TEST_ORDER_ID,
        "platform": TEST_PLATFORM,
        "shipping_address": TEST_SHIPPING_ADDRESS
    }
    
    # Make the request
    response = client.post(
        f"/api/v1/orders/{TEST_ORDER_ID}/address",
        json=request_data
    )
    
    # Assert the response
    assert response.status_code == 202
    assert response.json() == {"status": "pending"}
    
    # Verify the database record
    db_record = test_db.query(AddressUpdate).filter(
        AddressUpdate.order_id == TEST_ORDER_ID
    ).first()
    
    assert db_record is not None
    assert db_record.platform == TEST_PLATFORM
    assert db_record.status == "pending"
    assert db_record.shipping_address == TEST_SHIPPING_ADDRESS
    assert db_record.billing_address is None

def test_update_order_address_with_billing(test_db: Session):
    # Ensure all tables are created
    Base.metadata.create_all(bind=engine)
    """Test address update with billing address."""
    # Prepare test data with billing address
    billing_address = {
        "first_name": "John",
        "last_name": "Doe",
        "address1": "456 Billing St",
        "city": "San Francisco",
        "province": "CA",
        "country": "United States",
        "zip": "94105",
        "phone": "+14155551234"
    }
    
    request_data = {
        "order_id": TEST_ORDER_ID,
        "platform": TEST_PLATFORM,
        "shipping_address": TEST_SHIPPING_ADDRESS,
        "billing_address": billing_address
    }
    
    # Make the request
    response = client.post(
        f"/api/v1/orders/{TEST_ORDER_ID}/address",
        json=request_data
    )
    
    # Assert the response
    assert response.status_code == 202
    
    # Verify the database record
    db_record = test_db.query(AddressUpdate).filter(
        AddressUpdate.order_id == TEST_ORDER_ID
    ).first()
    
    assert db_record is not None
    assert db_record.billing_address == billing_address

def test_update_order_address_missing_required_fields(test_db: Session):
    # Ensure all tables are created
    Base.metadata.create_all(bind=engine)
    """Test address update with missing required fields."""
    # Missing shipping_address
    request_data = {
        "order_id": TEST_ORDER_ID,
        "platform": TEST_PLATFORM
    }
    
    response = client.post(
        f"/api/v1/orders/{TEST_ORDER_ID}/address",
        json=request_data
    )
    
    assert response.status_code == 422  # Validation error
