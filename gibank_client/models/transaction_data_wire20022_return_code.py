from enum import Enum


class TransactionDataWIRE20022ReturnCode(str, Enum):
    AC01 = "AC01"
    AC04 = "AC04"
    AC06 = "AC06"
    AG01 = "AG01"
    AM04 = "AM04"
    AM05 = "AM05"
    BE01 = "BE01"
    BE04 = "BE04"
    CUST = "CUST"
    FOCR = "FOCR"
    FRAD = "FRAD"
    MS03 = "MS03"
    NARR = "NARR"
    RC01 = "RC01"
    RR04 = "RR04"
    RUTA = "RUTA"

    def __str__(self) -> str:
        return str(self.value)
