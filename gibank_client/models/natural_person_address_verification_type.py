from enum import Enum


class NaturalPersonAddressVerificationType(str, Enum):
    LEASE_AGREEMENT = "lease_agreement"
    OTHER = "other"
    STATE_ID_CARD = "state_id_card"
    VENDOR_OUTPUT = "vendor_output"
    WATER_BILL = "water_bill"

    def __str__(self) -> str:
        return str(self.value)
