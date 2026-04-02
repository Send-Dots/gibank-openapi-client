from enum import Enum


class SubtransactionMiscellaneousSupportingDocumentsType(str, Enum):
    CORRESPONDENCE = "correspondence"
    INTERNAL_MEMO = "internal_memo"

    def __str__(self) -> str:
        return str(self.value)
