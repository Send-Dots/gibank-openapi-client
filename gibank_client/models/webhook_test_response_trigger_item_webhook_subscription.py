from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any
from typing import TypeVar
from typing import cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="WebhookTestResponseTriggerItemWebhookSubscription")


@_attrs_define
class WebhookTestResponseTriggerItemWebhookSubscription:
    """The Webhook Subscription that matched and has been triggered

    Attributes:
        id (float | Unset): The Webhook Subscription ID Example: 1.
        company_id (int | None | Unset): The company ID Example: 1.
        company_name (None | str | Unset): The company name Example: ABC Fintech.
        name (str | Unset): The name of the Webhook Subscription Example: Outbound ICL transaction create.
        url (str | Unset): The webhook URL. Must be the `https` protocol. A `HTTP-PUT` will be done on this URL.
            Example: https://www.toptal.com/developers/postbin/1693040028605-6554007045925.
        active (bool | Unset): Indicates if the Webhook Subscription is active Default: True. Example: True.
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
        secret_key_sha256_b64 (str | Unset): The SHA256 secret key, encoded as base64 string for the HMAC computation of
            the webhook payload Example: M...A==.
        create_date_time (datetime.datetime | Unset): The date and time when the webhook subscription was created
            (Stored as UTC, formatted as zero UTC offset (Zulu) format) Example: 2024-02-04T23:00:00.000Z.
        update_date_time (datetime.datetime | Unset): The date and time when the webhook subscription was last updated
            (Stored as UTC, formatted as zero UTC offset (Zulu) format) Example: 2024-02-04T23:00:00.000Z.
        create_user_id (float | Unset): The ID of the user who created the webhook subscription Example: 1.
        update_user_id (float | Unset): The ID of the user who last updated the webhook subscription Example: 1.
    """

    id: float | Unset = UNSET
    company_id: int | None | Unset = UNSET
    company_name: None | str | Unset = UNSET
    name: str | Unset = UNSET
    url: str | Unset = UNSET
    active: bool | Unset = True
    event_type_filter: str | Unset = UNSET
    secret_key_sha256_b64: str | Unset = UNSET
    create_date_time: datetime.datetime | Unset = UNSET
    update_date_time: datetime.datetime | Unset = UNSET
    create_user_id: float | Unset = UNSET
    update_user_id: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        company_id: int | None | Unset
        if isinstance(self.company_id, Unset):
            company_id = UNSET
        else:
            company_id = self.company_id

        company_name: None | str | Unset
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        else:
            company_name = self.company_name

        name = self.name

        url = self.url

        active = self.active

        event_type_filter = self.event_type_filter

        secret_key_sha256_b64 = self.secret_key_sha256_b64

        create_date_time: str | Unset = UNSET
        if not isinstance(self.create_date_time, Unset):
            create_date_time = self.create_date_time.isoformat()

        update_date_time: str | Unset = UNSET
        if not isinstance(self.update_date_time, Unset):
            update_date_time = self.update_date_time.isoformat()

        create_user_id = self.create_user_id

        update_user_id = self.update_user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if company_id is not UNSET:
            field_dict["company_id"] = company_id
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if name is not UNSET:
            field_dict["name"] = name
        if url is not UNSET:
            field_dict["url"] = url
        if active is not UNSET:
            field_dict["active"] = active
        if event_type_filter is not UNSET:
            field_dict["event_type_filter"] = event_type_filter
        if secret_key_sha256_b64 is not UNSET:
            field_dict["secret_key_sha256_b64"] = secret_key_sha256_b64
        if create_date_time is not UNSET:
            field_dict["create_date_time"] = create_date_time
        if update_date_time is not UNSET:
            field_dict["update_date_time"] = update_date_time
        if create_user_id is not UNSET:
            field_dict["create_user_id"] = create_user_id
        if update_user_id is not UNSET:
            field_dict["update_user_id"] = update_user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_company_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        company_id = _parse_company_id(d.pop("company_id", UNSET))

        def _parse_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_name = _parse_company_name(d.pop("company_name", UNSET))

        name = d.pop("name", UNSET)

        url = d.pop("url", UNSET)

        active = d.pop("active", UNSET)

        event_type_filter = d.pop("event_type_filter", UNSET)

        secret_key_sha256_b64 = d.pop("secret_key_sha256_b64", UNSET)

        _create_date_time = d.pop("create_date_time", UNSET)
        create_date_time: datetime.datetime | Unset
        if isinstance(_create_date_time, Unset):
            create_date_time = UNSET
        else:
            create_date_time = isoparse(_create_date_time)

        _update_date_time = d.pop("update_date_time", UNSET)
        update_date_time: datetime.datetime | Unset
        if isinstance(_update_date_time, Unset):
            update_date_time = UNSET
        else:
            update_date_time = isoparse(_update_date_time)

        create_user_id = d.pop("create_user_id", UNSET)

        update_user_id = d.pop("update_user_id", UNSET)

        webhook_test_response_trigger_item_webhook_subscription = cls(
            id=id,
            company_id=company_id,
            company_name=company_name,
            name=name,
            url=url,
            active=active,
            event_type_filter=event_type_filter,
            secret_key_sha256_b64=secret_key_sha256_b64,
            create_date_time=create_date_time,
            update_date_time=update_date_time,
            create_user_id=create_user_id,
            update_user_id=update_user_id,
        )

        webhook_test_response_trigger_item_webhook_subscription.additional_properties = d
        return webhook_test_response_trigger_item_webhook_subscription

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
