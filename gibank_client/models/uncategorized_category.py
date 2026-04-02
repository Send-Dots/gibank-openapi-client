from enum import Enum


class UncategorizedCategory(str, Enum):
    UNCATEGORIZED = "uncategorized"

    def __str__(self) -> str:
        return str(self.value)
