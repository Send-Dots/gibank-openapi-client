from enum import Enum


class SubclientFieldsState(str, Enum):
    APPROVED = "approved"
    CREATED = "created"
    PENDING = "pending"
    REJECTED = "rejected"

    def __str__(self) -> str:
        return str(self.value)
