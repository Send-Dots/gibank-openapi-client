from enum import Enum


class NaturalPersonFieldsRiskRating(str, Enum):
    HIGH = "high"
    LOW = "low"
    MEDIUM = "medium"
    VERY_HIGH = "very_high"
    VERY_LOW = "very_low"

    def __str__(self) -> str:
        return str(self.value)
