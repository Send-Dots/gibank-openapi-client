from enum import Enum


class TransactionDataWIRETransferType(str, Enum):
    RETURN = "return"
    TRANSACTION = "transaction"

    def __str__(self) -> str:
        return str(self.value)
