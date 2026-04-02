from enum import Enum


class SearchTransactionsTransferType(str, Enum):
    BATCH = "batch"
    CHECK = "check"
    IAT_BATCH = "iat_batch"
    IAT_RETURN = "iat_return"
    NOC = "noc"
    RETURN = "return"
    TRANSACTION = "transaction"

    def __str__(self) -> str:
        return str(self.value)
