from enum import Enum


class TransactionDataICLTransferType(str, Enum):
    CHECK = "check"
    RETURN = "return"

    def __str__(self) -> str:
        return str(self.value)
