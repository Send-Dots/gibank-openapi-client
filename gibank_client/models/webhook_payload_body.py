from __future__ import annotations

from collections.abc import Mapping
from typing import Any
from typing import TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WebhookPayloadBody")


@_attrs_define
class WebhookPayloadBody:
    """Contains information specific about the event type that is being send. For example it can contain the transaction
    information of a transaction that has been created.
      - `.*_transaction_(created|processing|under_review|processed|posted|failed|canceled)`: Contains the whole
    `transaction` structure
      - `.*_transaction_create_failed`: Contains the a special structure
      - `subclient.*`: Contains the whole `subclient` structure

    Additional reason fields are included at the top level of the body (alongside the entity object) in certain events:
      - `.*_transaction_(failed|canceled)`: Includes `state_change_reason` (string)
      - `.*_transaction_updated` (when deleted changes): Includes `deleted_change_reason` (string)

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        webhook_payload_body = cls()

        webhook_payload_body.additional_properties = d
        return webhook_payload_body

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
