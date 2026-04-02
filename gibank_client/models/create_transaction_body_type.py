from enum import Enum


class CreateTransactionBodyType(str, Enum):
    ACH = "ach"
    BOOK = "book"

    def __str__(self) -> str:
        return str(self.value)
