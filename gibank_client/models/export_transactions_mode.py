from enum import Enum


class ExportTransactionsMode(str, Enum):
    BALANCE = "balance"

    def __str__(self) -> str:
        return str(self.value)
