from enum import Enum


class GetBatchesCreateUserType(str, Enum):
    CLIENT = "client"
    MEMBER = "member"

    def __str__(self) -> str:
        return str(self.value)
