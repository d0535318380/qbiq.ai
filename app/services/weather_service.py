"""
Weather service module containing business logic.
This demonstrates how to organize service/business logic layer.
Includes retry mechanism for resilience.
"""

import httpx
from typing import Any
from app.core.config import settings
from app.core.logging import get_logger
from tenacity import retry, stop_after_attempt, wait_exponential

class WeatherService:
    """
    Service class for weather-related business logic.
    Implements retry mechanism with exponential backoff and circuit breaker pattern.
    """

    def __init__(self, options):
        self.access_key = options.weatherstack_api_key
        self.logger = get_logger(__name__)

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1))
    async def get_weather_async(self, city: str) -> dict[str, Any]:
        """
        Get weather information for a specific city.

        Args:
            city: Name of the city

        Returns:
            Dictionary containing weather information

        Raises:
            ValueError: If city is not found
        """
        city = city.strip()
        if not city:
            raise ValueError("City must be a non-empty string.")

        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.get(
                    "https://api.weatherstack.com/current",
                    params={
                        "access_key": self.access_key,
                        "query": city,
                        "units": "m"
                    }
                )

                self.logger.info("Weather provider response", city=city, status_code=response.status_code, attempt=attempt + 1)
                response.raise_for_status()

                return response.json()

        except Exception as e:
            self.logger.error("Weather provider failed", city=city, ex=e)
            raise ValueError(f"An error occurred: {e}") from e

# Create a singleton instance that can be imported
weather_service = WeatherService(settings)
