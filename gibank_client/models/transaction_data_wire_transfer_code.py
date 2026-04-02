from enum import Enum


class TransactionDataWIRETransferCode(str, Enum):
    VALUE_0 = "00"
    VALUE_1 = "01"
    VALUE_2 = "02"
    VALUE_3 = "07"
    VALUE_4 = "08"
    VALUE_5 = "31"
    VALUE_6 = "32"
    VALUE_7 = "33"
    VALUE_8 = "90"

    def __str__(self) -> str:
        return str(self.value)
