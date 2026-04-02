from enum import Enum


class TransactionDataWIREType(str, Enum):
    WIRE = "wire"

    def __str__(self) -> str:
        return str(self.value)
