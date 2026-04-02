from enum import Enum


class TransactionDataBOOKTransferType(str, Enum):
    RETURN = "return"
    TRANSACTION = "transaction"

    def __str__(self) -> str:
        return str(self.value)
