"""
Core configuration module using pydantic-settings.
This demonstrates best practices for FastAPI configuration management.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.

    Attributes:
        app_name: Name of the application
        debug: Debug mode flag
        api_version: API version string
        max_temperature: Maximum temperature threshold (dummy config)
    """

    app_name: str = "Weather API"
    debug: bool = False
    api_version: str = "v1"
    max_temperature: float = 100.0
    weatherstack_api_key: str = "75371f224d72a622591dd93b48af8bec"
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


# Global settings instance
settings = Settings()
