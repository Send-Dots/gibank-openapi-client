from enum import Enum


class GetTasksState(str, Enum):
    CANCELLED = "cancelled"
    DONE = "done"
    TODO = "todo"

    def __str__(self) -> str:
        return str(self.value)
