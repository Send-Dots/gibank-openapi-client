from __future__ import annotations

from collections.abc import Mapping
from typing import Any
from typing import TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ubo_ownership_prong_confirmation_category import (
    UBOOwnershipProngConfirmationCategory,
)
from ..models.ubo_ownership_prong_confirmation_type import (
    UBOOwnershipProngConfirmationType,
)

T = TypeVar("T", bound="UBOOwnershipProngConfirmation")


@_attrs_define
class UBOOwnershipProngConfirmation:
    """Subclient Owner - UBO - Ownership Prong Confirmation

    Attributes:
        category (UBOOwnershipProngConfirmationCategory): UBO - Ownership Prong Confirmation
        type_ (UBOOwnershipProngConfirmationType): The specific type of document or method used for confirming UBO
            ownership. Possible values include:

            - `capitalization_table` - Document showing the ownership percentages and equity dilution of a company
            (**Document upload only**)
            - `ownership_chart` - Visual representation of the ownership structure of a business (**Document upload only**)
            - `shareholder_register` - Official record of the owners of a company's shares (**Document upload only**)
            - `equity_schedule` - Detailed breakdown of a company's equity ownership (**Document upload only**)
            - `ownership_schedule` - Document detailing the ownership structure of a business (**Document upload only**)
            - `security_register` - Official record of a company's issued securities (**Document upload only**)
            - `other` - Any other document type that confirms UBO ownership (**Document upload only**)
    """

    category: UBOOwnershipProngConfirmationCategory
    type_: UBOOwnershipProngConfirmationType
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
        category = UBOOwnershipProngConfirmationCategory(d.pop("category"))

        type_ = UBOOwnershipProngConfirmationType(d.pop("type"))

        ubo_ownership_prong_confirmation = cls(
            category=category,
            type_=type_,
        )

        ubo_ownership_prong_confirmation.additional_properties = d
        return ubo_ownership_prong_confirmation

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
