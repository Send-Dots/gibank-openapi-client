from __future__ import annotations

from collections.abc import Mapping
from typing import Any
from typing import TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ubo_identification_number_category import UBOIdentificationNumberCategory
from ..models.ubo_identification_number_type import UBOIdentificationNumberType

T = TypeVar("T", bound="UBOIdentificationNumber")


@_attrs_define
class UBOIdentificationNumber:
    """Subclient Owner - UBO - Identification Number

    Attributes:
        category (UBOIdentificationNumberCategory): UBO - Identification Number
        type_ (UBOIdentificationNumberType): The specific type of identification number or verification method used for
            a UBO. Possible values include:

            - `ssn` - Social Security Number issued by the United States government for a UBO (**Text input only**)
            - `tin` - Taxpayer Identification Number for a UBO (**Text input only**)
            - `passport` - Passport number from a government-issued passport for a UBO (**Text input only**)
            - `government_issued_photo_id` - Identification number from a government-issued photo ID for a UBO (**Text input
            only**)
            - `vendor_output` - Third-party verification result of the UBO's identification number (**Text input only**)
    """

    category: UBOIdentificationNumberCategory
    type_: UBOIdentificationNumberType
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
        category = UBOIdentificationNumberCategory(d.pop("category"))

        type_ = UBOIdentificationNumberType(d.pop("type"))

        ubo_identification_number = cls(
            category=category,
            type_=type_,
        )

        ubo_identification_number.additional_properties = d
        return ubo_identification_number

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
