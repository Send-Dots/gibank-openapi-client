from enum import Enum


class CreateFailedWebhookBodyType(str, Enum):
    ACH = "ach"
    BOOK = "book"
    ICL = "icl"
    WIRE = "wire"
    WIRE20022 = "wire20022"

    def __str__(self) -> str:
        return str(self.value)
