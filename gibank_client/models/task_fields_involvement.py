from enum import Enum


class TaskFieldsInvolvement(str, Enum):
    ASSIGNEE = "assignee"
    OWNER = "owner"

    def __str__(self) -> str:
        return str(self.value)
