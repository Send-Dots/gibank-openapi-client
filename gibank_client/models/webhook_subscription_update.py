from __future__ import annotations

from collections.abc import Mapping
from typing import Any
from typing import TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="WebhookSubscriptionUpdate")


@_attrs_define
class WebhookSubscriptionUpdate:
    """
    Example:
        {'name': 'My Transaction Processing Webhook (Updated)', 'active': False}

    Attributes:
        name (str | Unset): The name of the Webhook Subscription Example: Outbound ICL transaction create.
        url (str | Unset): The webhook URL. Must be the `https` protocol. A `HTTP-PUT` will be done on this URL.
            Example: https://www.toptal.com/developers/postbin/1693040028605-6554007045925.
        active (bool | Unset): Indicates if the Webhook Subscription is active Example: True.
        event_type_filter (str | Unset): The webhook event filter as regular expression.
            Specifies the regular expression to define which event types you are subscribing to.
            For possible event type values, see the enum here above.

            Examples:
              - `.*_icl_transaction_created` to subscribe to all ICL created transaction events
              - `.*_icl_.*` to subscribe to all ICL events
              - `.*_transaction_processed` to subscribe to all transaction processed events
              - `subclient_approved` to subscribe to all subclient approved events
              - `.*` to subscribe any event
             Example: outbound_icl_transaction_created.
    """

    name: str | Unset = UNSET
    url: str | Unset = UNSET
    active: bool | Unset = UNSET
    event_type_filter: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        url = self.url

        active = self.active

        event_type_filter = self.event_type_filter

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if url is not UNSET:
            field_dict["url"] = url
        if active is not UNSET:
            field_dict["active"] = active
        if event_type_filter is not UNSET:
            field_dict["event_type_filter"] = event_type_filter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        url = d.pop("url", UNSET)

        active = d.pop("active", UNSET)

        event_type_filter = d.pop("event_type_filter", UNSET)

        webhook_subscription_update = cls(
            name=name,
            url=url,
            active=active,
            event_type_filter=event_type_filter,
        )

        webhook_subscription_update.additional_properties = d
        return webhook_subscription_update

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
