from enum import Enum


class SubclientAccountResponseType(str, Enum):
    CORE = "core"
    EXTERNAL = "external"
    VIRTUAL = "virtual"

    def __str__(self) -> str:
        return str(self.value)
