from enum import Enum


class TransactionDataWIRE20022TransferType(str, Enum):
    RETURN = "return"
    TRANSACTION = "transaction"

    def __str__(self) -> str:
        return str(self.value)
