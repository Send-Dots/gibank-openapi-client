from enum import Enum


class AccountBalanceFieldsType(str, Enum):
    CORE = "core"
    VIRTUAL = "virtual"

    def __str__(self) -> str:
        return str(self.value)
