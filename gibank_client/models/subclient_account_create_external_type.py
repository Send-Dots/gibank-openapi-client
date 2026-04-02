from enum import Enum


class SubclientAccountCreateExternalType(str, Enum):
    EXTERNAL = "external"

    def __str__(self) -> str:
        return str(self.value)
