from enum import Enum


class NaturalPersonIdentificationType(str, Enum):
    GOVERNMENT_ISSUED_PHOTO_ID = "government_issued_photo_id"
    OTHER = "other"
    PASSPORT = "passport"
    STATE_ID_CARD = "state_id_card"

    def __str__(self) -> str:
        return str(self.value)
