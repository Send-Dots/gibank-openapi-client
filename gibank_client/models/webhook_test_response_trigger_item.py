from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING
from typing import Any
from typing import TypeVar
from typing import cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET
from ..types import Unset

if TYPE_CHECKING:
    from ..models.webhook_test_response_trigger_item_webhook_subscription import (
        WebhookTestResponseTriggerItemWebhookSubscription,
    )


T = TypeVar("T", bound="WebhookTestResponseTriggerItem")


@_attrs_define
class WebhookTestResponseTriggerItem:
    """
    Attributes:
        webhook_subscription (WebhookTestResponseTriggerItemWebhookSubscription | Unset): The Webhook Subscription that
            matched and has been triggered
        error (None | str | Unset): The error message in case an error occured. Only returned in case of a direkt
            invokation
    """

    webhook_subscription: WebhookTestResponseTriggerItemWebhookSubscription | Unset = (
        UNSET
    )
    error: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        webhook_subscription: dict[str, Any] | Unset = UNSET
        if not isinstance(self.webhook_subscription, Unset):
            webhook_subscription = self.webhook_subscription.to_dict()

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if webhook_subscription is not UNSET:
            field_dict["webhook_subscription"] = webhook_subscription
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_test_response_trigger_item_webhook_subscription import (
            WebhookTestResponseTriggerItemWebhookSubscription,
        )

        d = dict(src_dict)
        _webhook_subscription = d.pop("webhook_subscription", UNSET)
        webhook_subscription: WebhookTestResponseTriggerItemWebhookSubscription | Unset
        if isinstance(_webhook_subscription, Unset):
            webhook_subscription = UNSET
        else:
            webhook_subscription = (
                WebhookTestResponseTriggerItemWebhookSubscription.from_dict(
                    _webhook_subscription
                )
            )

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        webhook_test_response_trigger_item = cls(
            webhook_subscription=webhook_subscription,
            error=error,
        )

        webhook_test_response_trigger_item.additional_properties = d
        return webhook_test_response_trigger_item

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
