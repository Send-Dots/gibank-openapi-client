from enum import Enum


class GetRoutingNumberInfoResponse200ItemType(str, Enum):
    BIC = "bic"
    ROUTING = "routing"

    def __str__(self) -> str:
        return str(self.value)
