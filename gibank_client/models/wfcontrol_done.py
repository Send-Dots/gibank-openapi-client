from enum import Enum


class WfcontrolDone(str, Enum):
    AUTOMATICALLY = "automatically"
    MANUALLY = "manually"

    def __str__(self) -> str:
        return str(self.value)
