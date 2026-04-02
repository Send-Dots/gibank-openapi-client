from __future__ import annotations

from collections.abc import Mapping
from typing import Any
from typing import TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_failed_webhook_body_type import CreateFailedWebhookBodyType
from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="CreateFailedWebhookBody")


@_attrs_define
class CreateFailedWebhookBody:
    """
    Attributes:
        batch_id (float | Unset): The prepared batch ID to search for created transactions Example: 4.
        type_ (CreateFailedWebhookBodyType | Unset): The type of the transaction Example: icl.
        test (bool | Unset): Indicates if the transaction is a test transaction Example: True.
        transfer_key (float | Unset): The transfer key of the transaction in the batch that failed Example: 1.
        error (str | Unset): Contains the exception message
    """

    batch_id: float | Unset = UNSET
    type_: CreateFailedWebhookBodyType | Unset = UNSET
    test: bool | Unset = UNSET
    transfer_key: float | Unset = UNSET
    error: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        batch_id = self.batch_id

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        test = self.test

        transfer_key = self.transfer_key

        error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if batch_id is not UNSET:
            field_dict["batch_id"] = batch_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if test is not UNSET:
            field_dict["test"] = test
        if transfer_key is not UNSET:
            field_dict["transfer_key"] = transfer_key
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        batch_id = d.pop("batch_id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: CreateFailedWebhookBodyType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = CreateFailedWebhookBodyType(_type_)

        test = d.pop("test", UNSET)

        transfer_key = d.pop("transfer_key", UNSET)

        error = d.pop("error", UNSET)

        create_failed_webhook_body = cls(
            batch_id=batch_id,
            type_=type_,
            test=test,
            transfer_key=transfer_key,
            error=error,
        )

        create_failed_webhook_body.additional_properties = d
        return create_failed_webhook_body

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
