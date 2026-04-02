from enum import Enum


class NaturalPersonIdentificationNumberCategory(str, Enum):
    NATURAL_PERSON_IDENTIFICATION_NUMBER = "natural_person_identification_number"

    def __str__(self) -> str:
        return str(self.value)
