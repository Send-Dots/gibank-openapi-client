from enum import Enum


class BusinessOwnershipStructureVerificationType(str, Enum):
    CAPITALIZATION_TABLE = "capitalization_table"
    EQUITY_SCHEDULE = "equity_schedule"
    OTHER = "other"
    OWNERSHIP_CHART = "ownership_chart"
    OWNERSHIP_SCHEDULE = "ownership_schedule"
    SECURITY_REGISTER = "security_register"
    SHAREHOLDER_REGISTER = "shareholder_register"

    def __str__(self) -> str:
        return str(self.value)
