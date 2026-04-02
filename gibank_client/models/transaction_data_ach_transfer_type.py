from enum import Enum


class TransactionDataACHTransferType(str, Enum):
    BATCH = "batch"
    IAT_BATCH = "iat_batch"
    IAT_RETURN = "iat_return"
    NOC = "noc"
    RETURN = "return"

    def __str__(self) -> str:
        return str(self.value)
