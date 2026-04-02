from enum import Enum


class TransactionDataACHType(str, Enum):
    ACH = "ach"

    def __str__(self) -> str:
        return str(self.value)
