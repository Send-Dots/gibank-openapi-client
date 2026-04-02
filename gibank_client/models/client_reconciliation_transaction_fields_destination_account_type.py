from enum import Enum


class ClientReconciliationTransactionFieldsDestinationAccountType(str, Enum):
    CORE = "core"
    VIRTUAL = "virtual"

    def __str__(self) -> str:
        return str(self.value)
