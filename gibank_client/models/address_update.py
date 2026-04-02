from __future__ import annotations

from collections.abc import Mapping
from typing import Any
from typing import TypeVar
from typing import cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="AddressUpdate")


@_attrs_define
class AddressUpdate:
    """
    Example:
        {'street_address_1': 'Hauptstraße 5 (Updated)', 'postal_code': '10115'}

    Attributes:
        country_alpha_2_code (str | Unset): The country ISO 3166-1 alpha-2 code Example: US.
        street_address_1 (str | Unset): The address street (1). If there is no possible value, use 'NA' Example: Test
            Street 1.
        street_address_2 (None | str | Unset): The address street (2) Example: Sample Value.
        city (str | Unset): The city Example: New York.
        state_province (str | Unset): The state/province Example: NY.
        postal_code (str | Unset): The postal code. If there is no possible value, use '0' Example: 10001.
    """

    country_alpha_2_code: str | Unset = UNSET
    street_address_1: str | Unset = UNSET
    street_address_2: None | str | Unset = UNSET
    city: str | Unset = UNSET
    state_province: str | Unset = UNSET
    postal_code: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        country_alpha_2_code = self.country_alpha_2_code

        street_address_1 = self.street_address_1

        street_address_2: None | str | Unset
        if isinstance(self.street_address_2, Unset):
            street_address_2 = UNSET
        else:
            street_address_2 = self.street_address_2

        city = self.city

        state_province = self.state_province

        postal_code = self.postal_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if country_alpha_2_code is not UNSET:
            field_dict["country_alpha_2_code"] = country_alpha_2_code
        if street_address_1 is not UNSET:
            field_dict["street_address_1"] = street_address_1
        if street_address_2 is not UNSET:
            field_dict["street_address_2"] = street_address_2
        if city is not UNSET:
            field_dict["city"] = city
        if state_province is not UNSET:
            field_dict["state_province"] = state_province
        if postal_code is not UNSET:
            field_dict["postal_code"] = postal_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        country_alpha_2_code = d.pop("country_alpha_2_code", UNSET)

        street_address_1 = d.pop("street_address_1", UNSET)

        def _parse_street_address_2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        street_address_2 = _parse_street_address_2(d.pop("street_address_2", UNSET))

        city = d.pop("city", UNSET)

        state_province = d.pop("state_province", UNSET)

        postal_code = d.pop("postal_code", UNSET)

        address_update = cls(
            country_alpha_2_code=country_alpha_2_code,
            street_address_1=street_address_1,
            street_address_2=street_address_2,
            city=city,
            state_province=state_province,
            postal_code=postal_code,
        )

        address_update.additional_properties = d
        return address_update

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
