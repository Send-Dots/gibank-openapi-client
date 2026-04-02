from enum import Enum


class BalanceFieldsAccountsItemSource(str, Enum):
    API = "api"
    CORE = "core"
    CORE_FILES = "core_files"

    def __str__(self) -> str:
        return str(self.value)
