from enum import Enum


class SubtransactionContractType(str, Enum):
    PURCHASE_ORDER = "purchase_order"
    SALES_CONTRACT = "sales_contract"
    SERVICE_AGREEMENT = "service_agreement"

    def __str__(self) -> str:
        return str(self.value)
