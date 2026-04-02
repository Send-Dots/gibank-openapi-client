from enum import Enum


class UBOIdentificationNumberCategory(str, Enum):
    UBO_IDENTIFICATION_NUMBER = "ubo_identification_number"

    def __str__(self) -> str:
        return str(self.value)
