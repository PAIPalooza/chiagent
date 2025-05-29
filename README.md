# ChiAgent - AI-Powered E-commerce Customer Agent

## Overview
ChiAgent is an AI-powered customer service agent for e-commerce platforms, providing automated support for refunds, order updates, and product discovery.

## Features

- **Refund Processing**: Stub endpoint for handling refund requests
- **Order Management**: Track and manage customer orders
- **Multi-platform Support**: Designed to work with Shopify and WooCommerce

## Getting Started

### Prerequisites

- Python 3.8+
- SQLite (for development)
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/chiagent.git
   cd chiagent
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. Start the FastAPI development server:
   ```bash
   uvicorn app.main:app --reload
   ```

2. The API will be available at `http://127.0.0.1:8000`
3. Access the interactive API documentation at `http://127.0.0.1:8000/docs`

## API Endpoints

### Refunds

- `POST /api/v1/orders/{order_id}/refund` - Request a refund for an order

Example request:
```json
{
  "order_id": "TEST123",
  "platform": "shopify",
  "amount": 100.00,
  "reason": "Customer requested refund"
}
```

## Running Tests

```bash
# Install test dependencies
pip install -r requirements-test.txt

# Run tests
pytest tests/
```

## Project Structure

```
chiagent/
├── app/
│   ├── api/
│   │   └── v1/
│   │       └── endpoints/
│   │           └── refunds.py
│   ├── crud/
│   │   └── refund.py
│   ├── db/
│   │   └── session.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   └── refund_request.py
│   ├── schemas/
│   │   └── refund.py
│   └── main.py
├── tests/
│   └── test_refunds.py
├── requirements.txt
└── README.md
```

## License

This project is licensed under the terms of the MIT license. See the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
