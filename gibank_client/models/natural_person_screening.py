from __future__ import annotations

from collections.abc import Mapping
from typing import Any
from typing import TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.natural_person_screening_category import NaturalPersonScreeningCategory
from ..models.natural_person_screening_type import NaturalPersonScreeningType

T = TypeVar("T", bound="NaturalPersonScreening")


@_attrs_define
class NaturalPersonScreening:
    """Subclient - Natural Person - Screening

    Attributes:
        category (NaturalPersonScreeningCategory): Natural Person - Screening
        type_ (NaturalPersonScreeningType): The specific type of screening performed for a natural person. Possible
            values include:

            - `sanctions_screening` - Results of checking against sanctions lists (**Text input only**)
            - `pep_screening` - Results of checking if the person is politically exposed (**Text input only**)
            - `adverse_media_screening` - Results of checking for negative news or information about the person (**Text
            input only**)
    """

    category: NaturalPersonScreeningCategory
    type_: NaturalPersonScreeningType
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
        category = NaturalPersonScreeningCategory(d.pop("category"))

        type_ = NaturalPersonScreeningType(d.pop("type"))

        natural_person_screening = cls(
            category=category,
            type_=type_,
        )

        natural_person_screening.additional_properties = d
        return natural_person_screening

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
