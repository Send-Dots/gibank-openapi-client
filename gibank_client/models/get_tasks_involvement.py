from enum import Enum


class GetTasksInvolvement(str, Enum):
    ASSIGNEE = "assignee"
    CREATOR = "creator"

    def __str__(self) -> str:
        return str(self.value)
