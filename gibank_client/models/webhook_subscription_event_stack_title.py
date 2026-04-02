from enum import Enum


class WebhookSubscriptionEventStackTitle(str, Enum):
    PRODUCTION = "Production"
    SANDBOX = "Sandbox"

    def __str__(self) -> str:
        return str(self.value)
