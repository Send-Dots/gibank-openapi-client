from __future__ import annotations

from collections.abc import Mapping
from typing import Any
from typing import TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.business_ownership_structure_verification_category import (
    BusinessOwnershipStructureVerificationCategory,
)
from ..models.business_ownership_structure_verification_type import (
    BusinessOwnershipStructureVerificationType,
)

T = TypeVar("T", bound="BusinessOwnershipStructureVerification")


@_attrs_define
class BusinessOwnershipStructureVerification:
    """Subclient - Business - Verification of Ownership Structure

    Attributes:
        category (BusinessOwnershipStructureVerificationCategory): Business - Verification of Ownership Structure
        type_ (BusinessOwnershipStructureVerificationType): The specific type of document or verification method used
            for business ownership structure verification. Possible values include:

            - `capitalization_table` - Document showing the ownership percentages and equity dilution of a company
            (**Document upload only**)
            - `ownership_chart` - Visual representation of the ownership structure of a business (**Document upload only**)
            - `shareholder_register` - Official record of the owners of a company's shares (**Document upload only**)
            - `equity_schedule` - Detailed breakdown of a company's equity ownership (**Document upload only**)
            - `ownership_schedule` - Document detailing the ownership structure of a business (**Document upload only**)
            - `security_register` - Official record of a company's issued securities (**Document upload only**)
            - `other` - Any other document type that verifies the business ownership structure (**Document upload only**)
    """

    category: BusinessOwnershipStructureVerificationCategory
    type_: BusinessOwnershipStructureVerificationType
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
        category = BusinessOwnershipStructureVerificationCategory(d.pop("category"))

        type_ = BusinessOwnershipStructureVerificationType(d.pop("type"))

        business_ownership_structure_verification = cls(
            category=category,
            type_=type_,
        )

        business_ownership_structure_verification.additional_properties = d
        return business_ownership_structure_verification

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
