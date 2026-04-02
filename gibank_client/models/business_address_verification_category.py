from enum import Enum


class BusinessAddressVerificationCategory(str, Enum):
    BUSINESS_ADDRESS_VERIFICATION = "business_address_verification"

    def __str__(self) -> str:
        return str(self.value)
