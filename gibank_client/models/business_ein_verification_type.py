from enum import Enum


class BusinessEINVerificationType(str, Enum):
    IRS_EIN_VERIFICATION_LETTER = "irs_ein_verification_letter"
    IRS_FORM_SS4 = "irs_form_ss4"
    IRS_FORM_W9 = "irs_form_w9"
    IRS_TAX_RETURN = "irs_tax_return"
    OTHER = "other"
    VENDOR_OUTPUT = "vendor_output"

    def __str__(self) -> str:
        return str(self.value)
