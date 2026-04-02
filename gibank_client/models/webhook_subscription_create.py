from __future__ import annotations

from collections.abc import Mapping
from typing import Any
from typing import TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="WebhookSubscriptionCreate")


@_attrs_define
class WebhookSubscriptionCreate:
    """
    Example:
        {'name': 'My Transaction Processing Webhook', 'url': 'https://webhooks.mydomain.com/listener',
            'event_type_filter': '.*_transaction_processed', 'active': True}

    Attributes:
        name (str): The name of the Webhook Subscription Example: Outbound ICL transaction create.
        url (str): The webhook URL. Must be the `https` protocol. A `HTTP-PUT` will be done on this URL. Example:
            https://www.toptal.com/developers/postbin/1693040028605-6554007045925.
        event_type_filter (str): The webhook event filter as regular expression.
            Specifies the regular expression to define which event types you are subscribing to.
            For possible event type values, see the enum here above.

            Examples:
              - `.*_icl_transaction_created` to subscribe to all ICL created transaction events
              - `.*_icl_.*` to subscribe to all ICL events
              - `.*_transaction_processed` to subscribe to all transaction processed events
              - `subclient_approved` to subscribe to all subclient approved events
              - `.*` to subscribe any event
             Example: outbound_icl_transaction_created.
        active (bool | Unset): Indicates if the Webhook Subscription is active Example: True.
    """

    name: str
    url: str
    event_type_filter: str
    active: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        url = self.url

        event_type_filter = self.event_type_filter

        active = self.active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "url": url,
                "event_type_filter": event_type_filter,
            }
        )
        if active is not UNSET:
            field_dict["active"] = active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        url = d.pop("url")

        event_type_filter = d.pop("event_type_filter")

        active = d.pop("active", UNSET)

        webhook_subscription_create = cls(
            name=name,
            url=url,
            event_type_filter=event_type_filter,
            active=active,
        )

        webhook_subscription_create.additional_properties = d
        return webhook_subscription_create

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
