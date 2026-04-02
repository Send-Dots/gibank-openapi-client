from enum import Enum


class DashboardResponseGroupsGROUPTITLESUBGROUPTITLEStepsItemInterest(str, Enum):
    ARCHIVED = "archived"
    DAILY_BUSINESS = "daily_business"

    def __str__(self) -> str:
        return str(self.value)
