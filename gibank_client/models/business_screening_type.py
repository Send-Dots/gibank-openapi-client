from enum import Enum


class BusinessScreeningType(str, Enum):
    ADVERSE_MEDIA_SCREENING = "adverse_media_screening"
    SANCTIONS_SCREENING = "sanctions_screening"

    def __str__(self) -> str:
        return str(self.value)
