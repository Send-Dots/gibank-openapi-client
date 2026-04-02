from enum import Enum


class UBODateOfBirthCategory(str, Enum):
    UBO_DATE_OF_BIRTH = "ubo_date_of_birth"

    def __str__(self) -> str:
        return str(self.value)
