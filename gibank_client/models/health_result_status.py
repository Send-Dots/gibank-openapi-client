from enum import Enum


class HealthResultStatus(str, Enum):
    DEGRADED = "degraded"
    DISABLED = "disabled"
    HEALTHY = "healthy"
    UNHEALTHY = "unhealthy"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
