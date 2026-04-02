from enum import Enum


class BatchClientUpdateState(str, Enum):
    CANCELED = "canceled"

    def __str__(self) -> str:
        return str(self.value)
