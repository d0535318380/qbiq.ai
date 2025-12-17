"""
Weather API routes.
This demonstrates proper importing from nested service modules.
"""

from typing import Any

from fastapi import APIRouter, HTTPException, Query
from fastapi_cache.decorator import cache

# Example of importing from deeply nested module structure
# Note: We use absolute imports starting from 'app'
from app.services.weather_service import weather_service

# Create a router instance
router = APIRouter(
    prefix="/weather",
    tags=["weather"],
)


@cache(expire=600)
@router.get("/", response_model=dict[str, Any])
async def get_weather(
    city: str = Query(
        ...,
        description="Name of the city to get weather for",
        examples=["New York", "London", "Tokyo"],
    ),
) -> dict[str, Any]:
    """
    Get current weather for a specific city.

    This is the main GET route demonstrating:
    - Proper import from services module
    - Query parameter validation
    - Error handling
    - Response model typing

    Args:
        city: Name of the city

    Returns:
        Weather information dictionary

    Raises:
        HTTPException: 404 if city not found
    """
    try:
        # Call the service layer (imported from app.services.weather_service)
        weather_data = await weather_service.get_weather_async(city)

        return weather_data
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e)) from e
