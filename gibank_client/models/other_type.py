from enum import Enum


class OtherType(str, Enum):
    OTHER = "other"

    def __str__(self) -> str:
        return str(self.value)
