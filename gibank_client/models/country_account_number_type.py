from enum import Enum


class CountryAccountNumberType(str, Enum):
    HIGHLY_RECOMMENDED = "highly_recommended"
    IBAN_MANDATORY = "iban_mandatory"

    def __str__(self) -> str:
        return str(self.value)
