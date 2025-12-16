"""
Tests for weather API endpoints.
Demonstrates pytest best practices for FastAPI testing.
"""

import pytest
from fastapi.testclient import TestClient


def test_root_endpoint(client: TestClient):
    """Test the root endpoint returns correct response."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "version" in data
    assert data["version"] == "v1"


def test_health_check(client: TestClient):
    """Test health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_get_weather_valid_city(client: TestClient):
    """Test getting weather for a valid city."""
    response = client.get("/api/v1/weather/?city=New York")
    assert response.status_code == 200


def test_get_weather_invalid_city(client: TestClient):
    """Test getting weather for an invalid city returns 404."""
    response = client.get("/api/v1/weather/?city=InvalidCity")
    assert response.status_code == 404
    assert "detail" in response.json()
