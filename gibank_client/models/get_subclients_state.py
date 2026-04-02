from enum import Enum


class GetSubclientsState(str, Enum):
    APPROVED = "approved"
    CREATED = "created"
    PENDING = "pending"
    REJECTED = "rejected"

    def __str__(self) -> str:
        return str(self.value)
