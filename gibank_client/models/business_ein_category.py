from enum import Enum


class BusinessEINCategory(str, Enum):
    BUSINESS_EIN = "business_ein"

    def __str__(self) -> str:
        return str(self.value)
