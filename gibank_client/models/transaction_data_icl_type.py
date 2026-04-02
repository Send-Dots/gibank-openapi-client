from enum import Enum


class TransactionDataICLType(str, Enum):
    ICL = "icl"

    def __str__(self) -> str:
        return str(self.value)
