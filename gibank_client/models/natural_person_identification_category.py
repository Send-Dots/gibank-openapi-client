from enum import Enum


class NaturalPersonIdentificationCategory(str, Enum):
    NATURAL_PERSON_IDENTIFICATION = "natural_person_identification"

    def __str__(self) -> str:
        return str(self.value)
