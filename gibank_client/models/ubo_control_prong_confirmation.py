from __future__ import annotations

from collections.abc import Mapping
from typing import Any
from typing import TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ubo_control_prong_confirmation_category import (
    UBOControlProngConfirmationCategory,
)
from ..models.ubo_control_prong_confirmation_type import UBOControlProngConfirmationType

T = TypeVar("T", bound="UBOControlProngConfirmation")


@_attrs_define
class UBOControlProngConfirmation:
    """Subclient Owner - UBO - Control Prong Confirmation

    Attributes:
        category (UBOControlProngConfirmationCategory): UBO - Control Prong Confirmation
        type_ (UBOControlProngConfirmationType): The specific type of document or method used for confirming UBO
            control. Possible values include:

            - `customer_application` - Application form filled by the customer confirming UBO control (**Document upload or
            text input**)
            - `other` - Any other document type that confirms UBO control (**Document upload or text input**)
    """

    category: UBOControlProngConfirmationCategory
    type_: UBOControlProngConfirmationType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category.value

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category = UBOControlProngConfirmationCategory(d.pop("category"))

        type_ = UBOControlProngConfirmationType(d.pop("type"))

        ubo_control_prong_confirmation = cls(
            category=category,
            type_=type_,
        )

        ubo_control_prong_confirmation.additional_properties = d
        return ubo_control_prong_confirmation

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
