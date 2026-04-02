from enum import Enum


class NaturalPersonDateOfBirthCategory(str, Enum):
    NATURAL_PERSON_DATE_OF_BIRTH = "natural_person_date_of_birth"

    def __str__(self) -> str:
        return str(self.value)
