from __future__ import annotations

from collections.abc import Mapping
from typing import Any
from typing import TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.natural_person_identification_category import (
    NaturalPersonIdentificationCategory,
)
from ..models.natural_person_identification_type import NaturalPersonIdentificationType

T = TypeVar("T", bound="NaturalPersonIdentification")


@_attrs_define
class NaturalPersonIdentification:
    """Subclient - Natural Person - Identification

    Attributes:
        category (NaturalPersonIdentificationCategory): Natural Person - Identification
        type_ (NaturalPersonIdentificationType): The specific type of document used for natural person identification.
            Possible values include:

            - `government_issued_photo_id` - Official identification document with a photo issued by a government entity
            (**Document upload only**)
            - `passport` - Official document issued by a country to its citizens for international travel (**Document upload
            only**)
            - `state_id_card` - Identification card issued by a state government (**Document upload only**)
            - `other` - Any other document type that identifies a natural person (**Document upload only**)
    """

    category: NaturalPersonIdentificationCategory
    type_: NaturalPersonIdentificationType
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
        category = NaturalPersonIdentificationCategory(d.pop("category"))

        type_ = NaturalPersonIdentificationType(d.pop("type"))

        natural_person_identification = cls(
            category=category,
            type_=type_,
        )

        natural_person_identification.additional_properties = d
        return natural_person_identification

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
