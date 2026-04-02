from enum import Enum


class TaskFieldsWfcontrolDone(str, Enum):
    AUTOMATICALLY = "automatically"
    MANUALLY = "manually"

    def __str__(self) -> str:
        return str(self.value)
