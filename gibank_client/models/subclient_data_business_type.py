from enum import Enum


class SubclientDataBusinessType(str, Enum):
    BUSINESS = "business"

    def __str__(self) -> str:
        return str(self.value)
