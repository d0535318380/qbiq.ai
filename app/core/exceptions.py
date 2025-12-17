"""
Custom exceptions for external API interactions.
"""


class ExternalAPIError(Exception):
    """Base exception for external API errors."""

    pass


class APITimeoutError(ExternalAPIError):
    """Raised when external API request times out."""

    pass


class APIConnectionError(ExternalAPIError):
    """Raised when connection to external API fails."""

    pass


class APIRateLimitError(ExternalAPIError):
    """Raised when API rate limit is exceeded."""

    pass


class APINotFoundError(ExternalAPIError):
    """Raised when requested resource is not found."""

    pass


class APIAuthenticationError(ExternalAPIError):
    """Raised when API authentication fails."""

    pass


class APIServerError(ExternalAPIError):
    """Raised when external API returns 5xx error."""

    pass


class CircuitBreakerOpenError(ExternalAPIError):
    """Raised when circuit breaker is open and blocking requests."""

    pass
