from enum import Enum


class Relationship(str, Enum):
    EMPLOYEE = "employee"
    EXTERNAL = "external"
    UBO = "ubo"

    def __str__(self) -> str:
        return str(self.value)
