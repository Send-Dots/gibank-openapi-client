from enum import Enum


class UBOIdentificationType(str, Enum):
    GOVERNMENT_ISSUED_PHOTO_ID = "government_issued_photo_id"
    PASSPORT = "passport"
    STATE_ID_CARD = "state_id_card"

    def __str__(self) -> str:
        return str(self.value)
