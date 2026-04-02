from enum import Enum


class NaturalPersonAddressVerificationCategory(str, Enum):
    NATURAL_PERSON_ADDRESS_VERIFICATION = "natural_person_address_verification"

    def __str__(self) -> str:
        return str(self.value)
