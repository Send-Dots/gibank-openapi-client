from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING
from typing import Any
from typing import TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.webhook_event_types import WebhookEventTypes
from ..types import UNSET
from ..types import Unset

if TYPE_CHECKING:
    from ..models.webhook_payload_body import WebhookPayloadBody


T = TypeVar("T", bound="WebhookPayload")


@_attrs_define
class WebhookPayload:
    """
    Attributes:
        webhook_subscription_id (float | Unset): The Webhook Subscription ID Example: 1.
        event_type (WebhookEventTypes | Unset): The webhook event type. Possible values include:

            - `outbound_icl_transaction_created` - An outbound ICL transaction has been created
            - `outbound_ach_transaction_created` - An outbound ACH transaction has been created
            - `outbound_wire_transaction_created` - An outbound WIRE transaction has been created
            - `outbound_book_transaction_created` - An outbound BOOK transaction has been created
            - `outbound_wire20022_transaction_created` - An outbound WIRE20022 transaction has been created
            - `inbound_icl_transaction_created` - An inbound ICL transaction has been created
            - `inbound_ach_transaction_created` - An inbound ACH transaction has been created
            - `inbound_wire_transaction_created` - An inbound WIRE transaction has been created
            - `inbound_book_transaction_created` - An inbound BOOK transaction has been created
            - `inbound_wire20022_transaction_created` - An inbound WIRE20022 transaction has been created

            - `outbound_icl_transaction_processing` - An outbound ICL transaction is being processed
            - `outbound_ach_transaction_processing` - An outbound ACH transaction is being processed
            - `outbound_wire_transaction_processing` - An outbound WIRE transaction is being processed
            - `outbound_book_transaction_processing` - An outbound BOOK transaction is being processed
            - `outbound_wire20022_transaction_processing` - An outbound WIRE20022 transaction is being processed
            - `inbound_icl_transaction_processing` - An inbound ICL transaction is being processed
            - `inbound_ach_transaction_processing` - An inbound ACH transaction is being processed
            - `inbound_wire_transaction_processing` - An inbound WIRE transaction is being processed
            - `inbound_book_transaction_processing` - An inbound BOOK transaction is being processed
            - `inbound_wire20022_transaction_processing` - An inbound WIRE20022 transaction is being processed

            - `outbound_icl_transaction_processed` - An outbound ICL transaction has been processed
            - `outbound_ach_transaction_processed` - An outbound ACH transaction has been processed
            - `outbound_wire_transaction_processed` - An outbound WIRE transaction has been processed
            - `outbound_book_transaction_processed` - An outbound BOOK transaction has been processed
            - `outbound_wire20022_transaction_processed` - An outbound WIRE20022 transaction has been processed
            - `inbound_icl_transaction_processed` - An inbound ICL transaction has been processed
            - `inbound_ach_transaction_processed` - An inbound ACH transaction has been processed
            - `inbound_wire_transaction_processed` - An inbound WIRE transaction has been processed
            - `inbound_book_transaction_processed` - An inbound BOOK transaction has been processed
            - `inbound_wire20022_transaction_processed` - An inbound WIRE20022 transaction has been processed

            - `outbound_icl_transaction_posted` - An outbound ICL transaction has been posted
            - `outbound_ach_transaction_posted` - An outbound ACH transaction has been posted
            - `outbound_wire_transaction_posted` - An outbound WIRE transaction has been posted
            - `outbound_book_transaction_posted` - An outbound BOOK transaction has been posted
            - `outbound_wire20022_transaction_posted` - An outbound WIRE20022 transaction has been posted
            - `inbound_icl_transaction_posted` - An inbound ICL transaction has been posted
            - `inbound_ach_transaction_posted` - An inbound ACH transaction has been posted
            - `inbound_wire_transaction_posted` - An inbound WIRE transaction has been posted
            - `inbound_book_transaction_posted` - An inbound BOOK transaction has been posted
            - `inbound_wire20022_transaction_posted` - An inbound WIRE20022 transaction has been posted

            - `outbound_icl_transaction_updated` - An outbound ICL transaction has been updated manually
            - `outbound_ach_transaction_updated` - An outbound ACH transaction has been updated manually
            - `outbound_wire_transaction_updated` - An outbound WIRE transaction has been updated manually
            - `outbound_book_transaction_updated` - An outbound BOOK transaction has been updated manually
            - `outbound_wire20022_transaction_updated` - An outbound WIRE20022 transaction has been updated manually
            - `inbound_icl_transaction_updated` - An inbound ICL transaction has been updated manually
            - `inbound_ach_transaction_updated` - An inbound ACH transaction has been updated manually
            - `inbound_wire_transaction_updated` - An inbound WIRE transaction has been updated manually
            - `inbound_book_transaction_updated` - An inbound BOOK transaction has been updated manually
            - `inbound_wire20022_transaction_updated` - An inbound WIRE20022 transaction has been updated manually

            - `outbound_icl_transaction_failed` - An outbound ICL transaction has failed (manually set)
            - `outbound_ach_transaction_failed` - An outbound ACH transaction has failed (manually set)
            - `outbound_wire_transaction_failed` - An outbound WIRE transaction has failed (manually set)
            - `outbound_book_transaction_failed` - An outbound BOOK transaction has failed (manually set)
            - `outbound_wire20022_transaction_failed` - An outbound WIRE20022 transaction has failed (manually set)
            - `inbound_icl_transaction_failed` - An inbound ICL transaction has failed (manually set)
            - `inbound_ach_transaction_failed` - An inbound ACH transaction has failed (manually set)
            - `inbound_wire_transaction_failed` - An inbound WIRE transaction has failed (manually set)
            - `inbound_book_transaction_failed` - An inbound BOOK transaction has failed (manually set)
            - `inbound_wire20022_transaction_failed` - An inbound WIRE20022 transaction has failed (manually set)

            - `outbound_icl_transaction_canceled` - An outbound ICL transaction has been canceled (manually set)
            - `outbound_ach_transaction_canceled` - An outbound ACH transaction has been canceled (manually set)
            - `outbound_wire_transaction_canceled` - An outbound wire transaction has been canceled (manually set)
            - `outbound_book_transaction_canceled` - An outbound book transaction has been canceled (manually set)
            - `outbound_wire20022_transaction_canceled` - An outbound wire20022 transaction has been canceled (manually set)
            - `inbound_icl_transaction_canceled` - An inbound ICL transaction has been canceled (manually set)
            - `inbound_ach_transaction_canceled` - An inbound ACH transaction has been canceled (manually set)
            - `inbound_wire_transaction_canceled` - An inbound wire transaction has been canceled (manually set)
            - `inbound_book_transaction_canceled` - An inbound book transaction has been canceled (manually set)
            - `inbound_wire20022_transaction_canceled` - An inbound wire20022 transaction has been canceled (manually set)

            - `outbound_icl_transaction_under_review` - An outbound ICL transaction has been under_review (manually set)
            - `outbound_ach_transaction_under_review` - An outbound ACH transaction has been under_review (manually set)
            - `outbound_wire_transaction_under_review` - An outbound wire transaction has been under_review (manually set)
            - `outbound_book_transaction_under_review` - An outbound book transaction has been under_review (manually set)
            - `outbound_wire20022_transaction_under_review` - An outbound wire20022 transaction has been under_review
            (manually set)
            - `inbound_icl_transaction_under_review` - An inbound ICL transaction has been under_review (manually set)
            - `inbound_ach_transaction_under_review` - An inbound ACH transaction has been under_review (manually set)
            - `inbound_wire_transaction_under_review` - An inbound wire transaction has been under_review (manually set)
            - `inbound_book_transaction_under_review` - An inbound book transaction has been under_review (manually set)
            - `inbound_wire20022_transaction_under_review` - An inbound wire20022 transaction has been under_review
            (manually set)

            - `icl_transaction_create_failed` - Creation of an ICL transaction has failed (direction unknown in bulk fail)
            - `ach_transaction_create_failed` - Creation of an ACH transaction has failed (direction unknown in bulk fail)
            - `wire_transaction_create_failed` - Creation of a WIRE transaction has failed (direction unknown in bulk fail)
            - `book_transaction_create_failed` - Creation of a BOOK transaction has failed (direction unknown in bulk fail)
            - `wire20022_transaction_create_failed` - Creation of a WIRE20022 transaction has failed (direction unknown in
            bulk fail)

            - `subclient_created` - A subclient has been created
            - `subclient_pending` - A subclient is pending
            - `subclient_approved` - A subclient has been approved
            - `subclient_rejected` - A subclient has been rejected
            - `subclient_updated` - A subclient has been updated
        url (str | Unset): The invoked webhook URL Example:
            https://www.toptal.com/developers/postbin/1693040028605-6554007045925.
        try_ (float | Unset): The number of tries to deliver the webhook Example: 1.
        request_origin (str | Unset): The origin who did the API call that resulted in the webhook event Example:
            10.11.12.13.
        create_date_time (datetime.datetime | Unset): The date and time when the request has been sent (Stored as UTC,
            formatted as zero UTC offset (Zulu) format) Example: 2024-02-04T23:00:00.000Z.
        body (WebhookPayloadBody | Unset): Contains information specific about the event type that is being send. For
            example it can contain the transaction information of a transaction that has been created.
              - `.*_transaction_(created|processing|under_review|processed|posted|failed|canceled)`: Contains the whole
            `transaction` structure
              - `.*_transaction_create_failed`: Contains the a special structure
              - `subclient.*`: Contains the whole `subclient` structure

            Additional reason fields are included at the top level of the body (alongside the entity object) in certain
            events:
              - `.*_transaction_(failed|canceled)`: Includes `state_change_reason` (string)
              - `.*_transaction_updated` (when deleted changes): Includes `deleted_change_reason` (string)
    """

    webhook_subscription_id: float | Unset = UNSET
    event_type: WebhookEventTypes | Unset = UNSET
    url: str | Unset = UNSET
    try_: float | Unset = UNSET
    request_origin: str | Unset = UNSET
    create_date_time: datetime.datetime | Unset = UNSET
    body: WebhookPayloadBody | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        webhook_subscription_id = self.webhook_subscription_id

        event_type: str | Unset = UNSET
        if not isinstance(self.event_type, Unset):
            event_type = self.event_type.value

        url = self.url

        try_ = self.try_

        request_origin = self.request_origin

        create_date_time: str | Unset = UNSET
        if not isinstance(self.create_date_time, Unset):
            create_date_time = self.create_date_time.isoformat()

        body: dict[str, Any] | Unset = UNSET
        if not isinstance(self.body, Unset):
            body = self.body.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if webhook_subscription_id is not UNSET:
            field_dict["webhook_subscription_id"] = webhook_subscription_id
        if event_type is not UNSET:
            field_dict["event_type"] = event_type
        if url is not UNSET:
            field_dict["url"] = url
        if try_ is not UNSET:
            field_dict["try"] = try_
        if request_origin is not UNSET:
            field_dict["request_origin"] = request_origin
        if create_date_time is not UNSET:
            field_dict["create_date_time"] = create_date_time
        if body is not UNSET:
            field_dict["body"] = body

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_payload_body import WebhookPayloadBody

        d = dict(src_dict)
        webhook_subscription_id = d.pop("webhook_subscription_id", UNSET)

        _event_type = d.pop("event_type", UNSET)
        event_type: WebhookEventTypes | Unset
        if isinstance(_event_type, Unset):
            event_type = UNSET
        else:
            event_type = WebhookEventTypes(_event_type)

        url = d.pop("url", UNSET)

        try_ = d.pop("try", UNSET)

        request_origin = d.pop("request_origin", UNSET)

        _create_date_time = d.pop("create_date_time", UNSET)
        create_date_time: datetime.datetime | Unset
        if isinstance(_create_date_time, Unset):
            create_date_time = UNSET
        else:
            create_date_time = isoparse(_create_date_time)

        _body = d.pop("body", UNSET)
        body: WebhookPayloadBody | Unset
        if isinstance(_body, Unset):
            body = UNSET
        else:
            body = WebhookPayloadBody.from_dict(_body)

        webhook_payload = cls(
            webhook_subscription_id=webhook_subscription_id,
            event_type=event_type,
            url=url,
            try_=try_,
            request_origin=request_origin,
            create_date_time=create_date_time,
            body=body,
        )

        webhook_payload.additional_properties = d
        return webhook_payload

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
