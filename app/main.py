from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import logging
import sys
from contextlib import asynccontextmanager
from typing import Generator, AsyncGenerator

# Import database and models first to ensure tables are created
from app.db.session import engine, Base, SessionLocal, get_db
from app.api.v1.endpoints import refunds

# Import models to ensure they are registered with SQLAlchemy
from app.models import *

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("app.log")
    ]
)
logger = logging.getLogger(__name__)

# Create database tables
def init_db() -> None:
    """Initialize the database by creating all tables."""
    try:
        logger.info("Creating database tables...")
        # Import all models here to ensure they are registered with SQLAlchemy
        from app.models.refund_request import RefundRequest
        Base.metadata.create_all(bind=engine)
        logger.info("Database tables created successfully")
    except Exception as e:
        logger.error(f"Error creating database tables: {e}")
        raise

# Lifespan handler for FastAPI
@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    # Initialize database on startup
    init_db()
    yield
    # Clean up on shutdown
    pass

# Create FastAPI app with lifespan
app = FastAPI(
    title="ChiAgent API",
    description="API for ChiAgent - AI Power Agent for ECom",
    version="0.1.0",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(
    refunds.router,
    prefix="/api/v1",
    tags=["refunds"],
)

@app.get("/health", tags=["health"])
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

@app.on_event("startup")
async def startup_event():
    """Run on application startup"""
    logger.info("Starting ChiAgent API...")

@app.on_event("shutdown")
def shutdown_event():
    """Run on application shutdown"""
    logger.info("Shutting down ChiAgent API...")
