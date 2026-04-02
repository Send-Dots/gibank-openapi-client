from enum import Enum


class BusinessAddressVerificationType(str, Enum):
    ARTICLES_OF_INCORPORATION = "articles_of_incorporation"
    BANK_STATEMENT = "bank_statement"
    CERTIFICATE_OF_FORMATION = "certificate_of_formation"
    CREDIT_CARD_STATEMENT = "credit_card_statement"
    IRS_EIN_VERIFICATION_LETTER = "irs_ein_verification_letter"
    IRS_TAX_RETURN = "irs_tax_return"
    LEASE_AGREEMENT = "lease_agreement"
    OTHER = "other"
    VENDOR_OUTPUT = "vendor_output"
    WATER_BILL = "water_bill"

    def __str__(self) -> str:
        return str(self.value)
