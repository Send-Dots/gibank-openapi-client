from enum import Enum


class ClientReconciliationTransactionFieldsOriginAccountType(str, Enum):
    CORE = "core"
    VIRTUAL = "virtual"

    def __str__(self) -> str:
        return str(self.value)
