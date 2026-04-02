from enum import Enum


class UBOScreeningCategory(str, Enum):
    UBO_SCREENING = "ubo_screening"

    def __str__(self) -> str:
        return str(self.value)
