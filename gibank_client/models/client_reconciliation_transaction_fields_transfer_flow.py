from enum import Enum


class ClientReconciliationTransactionFieldsTransferFlow(str, Enum):
    PULL = "pull"
    PUSH = "push"

    def __str__(self) -> str:
        return str(self.value)
