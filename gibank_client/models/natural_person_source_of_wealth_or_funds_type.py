from enum import Enum


class NaturalPersonSourceOfWealthOrFundsType(str, Enum):
    BANK_STATEMENT = "bank_statement"
    EMPLOYMENT_CONTRACT = "employment_contract"
    INVESTMENT_ACCOUNT_STATEMENTS = "investment_account_statements"
    PAYSLIP = "payslip"
    TAX_RETURN = "tax_return"

    def __str__(self) -> str:
        return str(self.value)
