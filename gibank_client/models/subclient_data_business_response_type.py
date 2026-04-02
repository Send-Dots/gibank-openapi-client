from enum import Enum


class SubclientDataBusinessResponseType(str, Enum):
    BUSINESS = "business"

    def __str__(self) -> str:
        return str(self.value)
