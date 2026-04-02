from enum import Enum


class TransactionDataBOOKTransferCode(str, Enum):
    VALUE_0 = "22"
    VALUE_1 = "23"
    VALUE_2 = "27"
    VALUE_3 = "28"
    VALUE_4 = "32"
    VALUE_5 = "33"
    VALUE_6 = "37"
    VALUE_7 = "38"

    def __str__(self) -> str:
        return str(self.value)
