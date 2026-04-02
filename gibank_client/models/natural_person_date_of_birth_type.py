from enum import Enum


class NaturalPersonDateOfBirthType(str, Enum):
    BIRTH_CERTIFICATE = "birth_certificate"
    OTHER = "other"
    PASSPORT = "passport"
    STATE_ID_CARD = "state_id_card"

    def __str__(self) -> str:
        return str(self.value)
