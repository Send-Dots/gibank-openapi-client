from enum import Enum


class SubtransactionInvoiceCategory(str, Enum):
    SUBTRANSACTION_INVOICE = "subtransaction_invoice"

    def __str__(self) -> str:
        return str(self.value)
