from enum import Enum


class ProductionHistoryLevel(str, Enum):
    DEBUG = "debug"
    INFO = "info"

    def __str__(self) -> str:
        return str(self.value)
