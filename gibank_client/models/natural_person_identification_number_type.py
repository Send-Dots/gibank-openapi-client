from enum import Enum


class NaturalPersonIdentificationNumberType(str, Enum):
    GOVERNMENT_ISSUED_PHOTO_ID = "government_issued_photo_id"
    PASSPORT = "passport"
    SSN = "ssn"
    TIN = "tin"
    VENDOR_OUTPUT = "vendor_output"

    def __str__(self) -> str:
        return str(self.value)
