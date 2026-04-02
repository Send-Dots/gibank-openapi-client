from enum import Enum


class BusinessNameVerificationType(str, Enum):
    ARTICLES_OF_INCORPORATION = "articles_of_incorporation"
    ARTICLES_OF_ORGANIZATION = "articles_of_organization"
    BUSINESS_LICENSE = "business_license"
    BUSINESS_TAX_RETURN = "business_tax_return"
    CERTIFICATE_OF_FORMATION = "certificate_of_formation"
    IRS_EIN_VERIFICATION_LETTER = "irs_ein_verification_letter"
    OTHER = "other"
    STATE_CERTIFICATE_OF_GOOD_STANDING = "state_certificate_of_good_standing"

    def __str__(self) -> str:
        return str(self.value)
