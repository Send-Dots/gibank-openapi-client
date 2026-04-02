from enum import Enum


class ClientReconciliationAccountType(str, Enum):
    ACCOUNT = "account"

    def __str__(self) -> str:
        return str(self.value)
