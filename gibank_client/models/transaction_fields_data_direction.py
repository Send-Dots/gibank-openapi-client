from enum import Enum


class TransactionFieldsDataDirection(str, Enum):
    INCOMING = "incoming"
    OUTGOING = "outgoing"

    def __str__(self) -> str:
        return str(self.value)
