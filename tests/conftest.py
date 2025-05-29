import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from app.main import app
from app.db.session import Base, SQLALCHEMY_DATABASE_URL, get_db
from app.models.refund_request import RefundRequest  # Explicit import

# Use an in-memory SQLite database for testing
TEST_DATABASE_URL = "sqlite:///./test.db"

# Override the database URL for testing
app.dependency_overrides = {}

# Create test engine and session
engine = create_engine(
    TEST_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Import all models to ensure they are registered with SQLAlchemy
from app.models import *  # noqa

# Create all tables
def create_tables():
    Base.metadata.create_all(bind=engine)

# Drop all tables
def drop_tables():
    Base.metadata.drop_all(bind=engine)

# Create test client
client = TestClient(app)

@pytest.fixture(scope="function")
def db_session():
    """Create a fresh database for each test."""
    # Drop all tables and create fresh ones
    drop_tables()
    create_tables()
    
    # Create a new session
    db = TestingSessionLocal()
    
    try:
        yield db
    finally:
        db.close()
        # Clean up after test
        drop_tables()

@pytest.fixture(scope="function")
def client_with_db(db_session):
    """Create a test client that uses the test database."""
    def override_get_db():
        try:
            yield db_session
        finally:
            db_session.rollback()
    
    app.dependency_overrides[app.dependency_overrides.get('get_db', get_db)] = override_get_db
    yield client
    app.dependency_overrides = {}

# Import all models to ensure they are registered with SQLAlchemy
from app.models.refund_request import RefundRequest  # noqa
