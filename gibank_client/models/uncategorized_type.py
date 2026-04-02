from enum import Enum


class UncategorizedType(str, Enum):
    UNCATEGORIZED = "uncategorized"

    def __str__(self) -> str:
        return str(self.value)
