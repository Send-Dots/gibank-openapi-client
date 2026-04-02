from enum import Enum


class UBOControlProngConfirmationType(str, Enum):
    CUSTOMER_APPLICATION = "customer_application"
    OTHER = "other"

    def __str__(self) -> str:
        return str(self.value)
