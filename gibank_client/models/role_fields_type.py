from enum import Enum


class RoleFieldsType(str, Enum):
    CLIENT = "client"
    MEMBER = "member"

    def __str__(self) -> str:
        return str(self.value)
