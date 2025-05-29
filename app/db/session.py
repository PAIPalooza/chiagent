from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session as SessionType, declarative_base
from sqlalchemy import create_engine

# SQLite database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./chiagent.db"

# Create SQLAlchemy engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False},
    echo=True  # Enable SQL query logging for development
)

# Create session factory
SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine
)

# Base class for models
Base = declarative_base()

def get_db() -> SessionType:
    """
    Dependency function that yields db sessions
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
