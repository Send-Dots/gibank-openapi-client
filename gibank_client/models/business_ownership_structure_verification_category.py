from enum import Enum


class BusinessOwnershipStructureVerificationCategory(str, Enum):
    BUSINESS_VERIFICATION_OF_OWNERSHIP_STRUCTURE = (
        "business_verification_of_ownership_structure"
    )

    def __str__(self) -> str:
        return str(self.value)
