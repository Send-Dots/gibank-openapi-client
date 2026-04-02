from enum import Enum


class CheckHealthComponentComponent(str, Enum):
    ACH_AUTOMATION = "ach_automation"
    ACH_SERVICE = "ach_service"
    BALANCES = "balances"
    CORE = "core"
    DATABASE = "database"
    ICL_AUTOMATION = "icl_automation"
    ICL_SERVICE = "icl_service"
    WIRE_SERVICE = "wire_service"

    def __str__(self) -> str:
        return str(self.value)
