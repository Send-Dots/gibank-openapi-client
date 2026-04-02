from enum import Enum


class SubtransactionContractCategory(str, Enum):
    SUBTRANSACTION_CONTRACT = "subtransaction_contract"

    def __str__(self) -> str:
        return str(self.value)
