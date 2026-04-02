from enum import Enum


class TransactionDataWIRE20022Type(str, Enum):
    WIRE20022 = "wire20022"

    def __str__(self) -> str:
        return str(self.value)
