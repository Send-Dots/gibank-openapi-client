from enum import Enum


class SubclientDataNaturalPersonType(str, Enum):
    NATURAL_PERSON = "natural_person"

    def __str__(self) -> str:
        return str(self.value)
