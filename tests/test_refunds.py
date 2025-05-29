import pytest

# These fixtures are provided by conftest.py
# - client_with_db: A test client with database access
# - db_session: A database session for direct database operations



def test_refund_endpoint(client_with_db):
    """Test the refund endpoint with valid data"""
    test_data = {
        "order_id": "TEST123",
        "platform": "shopify",
        "amount": 100.00,
        "reason": "Customer requested refund"
    }
    
    response = client_with_db.post("/api/v1/orders/TEST123/refund", json=test_data)
    assert response.status_code == 202
    assert response.json() == {"status": "pending"}

def test_refund_endpoint_invalid_data(client_with_db):
    """Test the refund endpoint with invalid data"""
    test_data = {"platform": "invalid_platform"}  # Missing required fields
    
    response = client_with_db.post("/api/v1/orders/TEST123/refund", json=test_data)
    assert response.status_code == 422  # Validation error

def test_refund_endpoint_logging(client_with_db, db_session):
    """Test that refund requests are logged to the database"""
    from app.models.refund_request import RefundRequest
    
    test_data = {
        "order_id": "TEST456",
        "platform": "woocommerce",
        "amount": 50.00,
        "reason": "Defective product"
    }
    
    response = client_with_db.post("/api/v1/orders/TEST456/refund", json=test_data)
    assert response.status_code == 202
    
    # Verify the refund request was logged to the database
    refund_request = db_session.query(RefundRequest).filter_by(order_id="TEST456").first()
    
    assert refund_request is not None
    assert refund_request.platform == "woocommerce"
    assert refund_request.status == "pending"
    assert refund_request.request_data["reason"] == "Defective product"
