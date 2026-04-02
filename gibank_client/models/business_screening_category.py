from enum import Enum


class BusinessScreeningCategory(str, Enum):
    BUSINESS_SCREENING = "business_screening"

    def __str__(self) -> str:
        return str(self.value)
