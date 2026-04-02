from enum import Enum


class SubtransactionQuoteEstimateType(str, Enum):
    VENDOR_QUOTE = "vendor_quote"
    WORK_ORDER = "work_order"

    def __str__(self) -> str:
        return str(self.value)
