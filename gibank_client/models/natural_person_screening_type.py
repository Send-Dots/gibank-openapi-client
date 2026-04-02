from enum import Enum


class NaturalPersonScreeningType(str, Enum):
    ADVERSE_MEDIA_SCREENING = "adverse_media_screening"
    PEP_SCREENING = "pep_screening"
    SANCTIONS_SCREENING = "sanctions_screening"

    def __str__(self) -> str:
        return str(self.value)
