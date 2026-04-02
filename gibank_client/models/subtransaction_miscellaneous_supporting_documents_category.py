from enum import Enum


class SubtransactionMiscellaneousSupportingDocumentsCategory(str, Enum):
    SUBTRANSACTION_MISCELLANEOUS_SUPPORTING_DOCUMENTS = (
        "subtransaction_miscellaneous_supporting_documents"
    )

    def __str__(self) -> str:
        return str(self.value)
