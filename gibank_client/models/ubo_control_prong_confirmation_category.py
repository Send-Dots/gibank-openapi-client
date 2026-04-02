from enum import Enum


class UBOControlProngConfirmationCategory(str, Enum):
    UBO_CONTROL_PRONG_CONFIRMATION = "ubo_control_prong_confirmation"

    def __str__(self) -> str:
        return str(self.value)
