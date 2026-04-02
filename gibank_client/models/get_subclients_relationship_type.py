from enum import Enum


class GetSubclientsRelationshipType(str, Enum):
    AFFILIATE = "affiliate"
    BENEFICIARY = "beneficiary"
    COUNTERPARTY = "counterparty"
    CUSTOMER = "customer"
    PAYMENT_SERVICE_PROVIDER = "payment_service_provider"
    ROOT = "root"

    def __str__(self) -> str:
        return str(self.value)
