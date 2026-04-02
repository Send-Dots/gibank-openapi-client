from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING
from typing import Any
from typing import TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhook_event_types import WebhookEventTypes
from ..types import UNSET
from ..types import Unset

if TYPE_CHECKING:
    from ..models.test_webhook_body_body import TestWebhookBodyBody


T = TypeVar("T", bound="TestWebhookBody")


@_attrs_define
class TestWebhookBody:
    """
    Attributes:
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
        incl_non_active (bool | Unset): Include non active Webhook Subscriptions
        direct_invoke (bool | Unset): In normal cases, events that trigger webhooks will create a queue system to ensure
            the the retry mechanism with exponential backoff is used.
            However, direct invoke means that we don't use the queue system but want to trigger the webhook directly. This
            option is only available in our test endpoint and is useful to get a direct feedback about the call, so if it
            worked correctly or not.
        body (TestWebhookBodyBody | Unset): A body object that you want to get back into your webhook
    """

    event_type: WebhookEventTypes | Unset = UNSET
    incl_non_active: bool | Unset = UNSET
    direct_invoke: bool | Unset = UNSET
    body: TestWebhookBodyBody | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_type: str | Unset = UNSET
        if not isinstance(self.event_type, Unset):
            event_type = self.event_type.value

        incl_non_active = self.incl_non_active

        direct_invoke = self.direct_invoke

        body: dict[str, Any] | Unset = UNSET
        if not isinstance(self.body, Unset):
            body = self.body.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event_type is not UNSET:
            field_dict["event_type"] = event_type
        if incl_non_active is not UNSET:
            field_dict["incl_non_active"] = incl_non_active
        if direct_invoke is not UNSET:
            field_dict["direct_invoke"] = direct_invoke
        if body is not UNSET:
            field_dict["body"] = body

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.test_webhook_body_body import TestWebhookBodyBody

        d = dict(src_dict)
        _event_type = d.pop("event_type", UNSET)
        event_type: WebhookEventTypes | Unset
        if isinstance(_event_type, Unset):
            event_type = UNSET
        else:
            event_type = WebhookEventTypes(_event_type)

        incl_non_active = d.pop("incl_non_active", UNSET)

        direct_invoke = d.pop("direct_invoke", UNSET)

        _body = d.pop("body", UNSET)
        body: TestWebhookBodyBody | Unset
        if isinstance(_body, Unset):
            body = UNSET
        else:
            body = TestWebhookBodyBody.from_dict(_body)

        test_webhook_body = cls(
            event_type=event_type,
            incl_non_active=incl_non_active,
            direct_invoke=direct_invoke,
            body=body,
        )

        test_webhook_body.additional_properties = d
        return test_webhook_body

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
