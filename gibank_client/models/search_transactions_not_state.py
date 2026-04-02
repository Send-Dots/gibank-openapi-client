from enum import Enum


class SearchTransactionsNotState(str, Enum):
    CANCELED = "canceled"
    CREATED = "created"
    FAILED = "failed"
    POSTED = "posted"
    PROCESSED = "processed"
    PROCESSING = "processing"
    UNDER_REVIEW = "under_review"

    def __str__(self) -> str:
        return str(self.value)
