from enum import Enum


class BusinessDBARegistrationCategory(str, Enum):
    BUSINESS_DBA_REGISTRATION = "business_dba_registration"

    def __str__(self) -> str:
        return str(self.value)
