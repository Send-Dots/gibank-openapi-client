from enum import Enum


class SubclientAccountCreateCoreType(str, Enum):
    CORE = "core"

    def __str__(self) -> str:
        return str(self.value)
