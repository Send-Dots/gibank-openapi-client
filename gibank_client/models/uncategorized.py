from __future__ import annotations

from collections.abc import Mapping
from typing import Any
from typing import TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.uncategorized_category import UncategorizedCategory
from ..models.uncategorized_type import UncategorizedType

T = TypeVar("T", bound="Uncategorized")


@_attrs_define
class Uncategorized:
    """Uncategorized

    Attributes:
        category (UncategorizedCategory): Uncategorized
        type_ (UncategorizedType): The specific type of document or verification method used for uncategorized purposes.
            Possible values include:

            - `uncategorized` - Any uncategorized document type (**Document upload or text input**)
    """

    category: UncategorizedCategory
    type_: UncategorizedType
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
        category = UncategorizedCategory(d.pop("category"))

        type_ = UncategorizedType(d.pop("type"))

        uncategorized = cls(
            category=category,
            type_=type_,
        )

        uncategorized.additional_properties = d
        return uncategorized

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
