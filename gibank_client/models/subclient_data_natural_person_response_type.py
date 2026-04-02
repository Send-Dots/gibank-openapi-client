from enum import Enum


class SubclientDataNaturalPersonResponseType(str, Enum):
    NATURAL_PERSON = "natural_person"

    def __str__(self) -> str:
        return str(self.value)
