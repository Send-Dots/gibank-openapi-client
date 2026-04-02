from enum import Enum


class BusinessEINVerificationCategory(str, Enum):
    BUSINESS_EIN_VERIFICATION = "business_ein_verification"

    def __str__(self) -> str:
        return str(self.value)
