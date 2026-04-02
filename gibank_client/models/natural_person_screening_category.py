from enum import Enum


class NaturalPersonScreeningCategory(str, Enum):
    NATURAL_PERSON_SCREENING = "natural_person_screening"

    def __str__(self) -> str:
        return str(self.value)
