from enum import Enum


class UBOIdentificationCategory(str, Enum):
    UBO_IDENTIFICATION = "ubo_identification"

    def __str__(self) -> str:
        return str(self.value)
