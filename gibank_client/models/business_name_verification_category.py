from enum import Enum


class BusinessNameVerificationCategory(str, Enum):
    BUSINESS_NAME_VERIFICATION = "business_name_verification"

    def __str__(self) -> str:
        return str(self.value)
