# # chiagent

AI Power Agent for E-commerce

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up PostgreSQL database:
```bash
# Create database
createdb chiagent
```

4. Run migrations (coming soon)

5. Start the development server:
```bash
uvicorn app.main:app --reload
```

The API will be available at http://localhost:8000

## API Documentation

Swagger UI: http://localhost:8000/docs
ReDoc: http://localhost:8000/redoc

## Project Structure

```
app/
├── api/           # API routes and endpoints
├── core/          # Core application logic
├── db/            # Database models and sessions
├── models/        # SQLAlchemy models
├── schemas/       # Pydantic schemas
└── main.py        # FastAPI application entry point
```

## Features

- Product search with natural language query
- Faceted search support
- Platform integration (Shopify, WooCommerce)
- Customer service automation
- Virtual try-on functionality
