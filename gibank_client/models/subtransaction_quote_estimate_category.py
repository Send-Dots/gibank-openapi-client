from enum import Enum


class SubtransactionQuoteEstimateCategory(str, Enum):
    SUBTRANSACTION_QUOTE_ESTIMATE = "subtransaction_quote_estimate"

    def __str__(self) -> str:
        return str(self.value)
