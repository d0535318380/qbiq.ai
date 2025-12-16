"""
Pytest configuration and fixtures.
This file is automatically discovered by pytest.
"""

import pytest
from fastapi.testclient import TestClient

# Import the FastAPI app - note the proper import path
from app.main import app


@pytest.fixture
def client():
    """
    Create a test client for the FastAPI application.

    This fixture can be used in any test function by including
    'client' as a parameter.

    Yields:
        TestClient: FastAPI test client
    """
    with TestClient(app) as test_client:
        yield test_client
