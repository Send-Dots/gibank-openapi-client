from enum import Enum


class UBOOwnershipProngConfirmationCategory(str, Enum):
    UBO_OWNERSHIP_PRONG_CONFIRMATION = "ubo_ownership_prong_confirmation"

    def __str__(self) -> str:
        return str(self.value)
