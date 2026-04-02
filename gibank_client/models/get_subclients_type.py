from enum import Enum


class GetSubclientsType(str, Enum):
    BUSINESS = "business"
    NATURAL_PERSON = "natural_person"

    def __str__(self) -> str:
        return str(self.value)
