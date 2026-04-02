from enum import Enum


class SubclientAccountCreateVirtualType(str, Enum):
    VIRTUAL = "virtual"

    def __str__(self) -> str:
        return str(self.value)
