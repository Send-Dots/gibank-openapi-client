from enum import Enum


class OtherCategory(str, Enum):
    OTHER = "other"

    def __str__(self) -> str:
        return str(self.value)
