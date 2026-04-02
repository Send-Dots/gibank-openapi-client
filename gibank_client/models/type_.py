from enum import Enum


class Type(str, Enum):
    CLIENT = "client"
    MEMBER = "member"

    def __str__(self) -> str:
        return str(self.value)
