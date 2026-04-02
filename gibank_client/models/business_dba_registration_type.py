from enum import Enum


class BusinessDBARegistrationType(str, Enum):
    BUSINESS_LICENSE = "business_license"
    BUSINESS_PERMIT = "business_permit"
    CERTIFICATE_OF_ASSUMED_NAME = "certificate_of_assumed_name"
    CERTIFICATE_OF_TRADE_NAME = "certificate_of_trade_name"
    DBA_CERTIFICATE = "dba_certificate"
    DBA_REGISTRATION_CONFIRMATION_LETTER = "dba_registration_confirmation_letter"

    def __str__(self) -> str:
        return str(self.value)
