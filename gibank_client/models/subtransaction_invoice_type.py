from enum import Enum


class SubtransactionInvoiceType(str, Enum):
    CUSTOMER_INVOICE = "customer_invoice"
    PROFORMA_INVOICE = "proforma_invoice"
    SUPPLIER_INVOICE = "supplier_invoice"

    def __str__(self) -> str:
        return str(self.value)
