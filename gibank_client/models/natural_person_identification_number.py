from __future__ import annotations

from collections.abc import Mapping
from typing import Any
from typing import TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.natural_person_identification_number_category import (
    NaturalPersonIdentificationNumberCategory,
)
from ..models.natural_person_identification_number_type import (
    NaturalPersonIdentificationNumberType,
)

T = TypeVar("T", bound="NaturalPersonIdentificationNumber")


@_attrs_define
class NaturalPersonIdentificationNumber:
    """Subclient - Natural Person - Identification Number

    Attributes:
        category (NaturalPersonIdentificationNumberCategory): Natural Person - Identification Number
        type_ (NaturalPersonIdentificationNumberType): The specific type of identification number or verification method
            used for a natural person. Possible values include:

            - `ssn` - Social Security Number issued by the United States government (**Text input only**)
            - `tin` - Taxpayer Identification Number (**Text input only**)
            - `passport` - Passport number from a government-issued passport (**Text input only**)
            - `government_issued_photo_id` - Identification number from a government-issued photo ID (**Text input only**)
            - `vendor_output` - Third-party verification result of the person's identification number (**Text input only**)
    """

    category: NaturalPersonIdentificationNumberCategory
    type_: NaturalPersonIdentificationNumberType
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
        category = NaturalPersonIdentificationNumberCategory(d.pop("category"))

        type_ = NaturalPersonIdentificationNumberType(d.pop("type"))

        natural_person_identification_number = cls(
            category=category,
            type_=type_,
        )

        natural_person_identification_number.additional_properties = d
        return natural_person_identification_number

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
