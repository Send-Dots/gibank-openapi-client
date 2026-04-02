from enum import Enum


class SearchTransactionsMode(str, Enum):
    BALANCE = "balance"

    def __str__(self) -> str:
        return str(self.value)
