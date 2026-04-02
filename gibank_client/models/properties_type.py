from enum import Enum


class PropertiesType(str, Enum):
    SUBCLIENT_PENDING = "subclient_pending"

    def __str__(self) -> str:
        return str(self.value)
