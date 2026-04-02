from __future__ import annotations

from collections.abc import Mapping
from typing import Any
from typing import TypeVar
from typing import cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="AddressCreate")


@_attrs_define
class AddressCreate:
    """
    Example:
        {'country_alpha_2_code': 'DE', 'street_address_1': 'Musterstraße 10', 'city': 'Berlin', 'postal_code': '10117'}

    Attributes:
        country_alpha_2_code (str): The country ISO 3166-1 alpha-2 code Example: US.
        street_address_1 (str): The address street (1). If there is no possible value, use 'NA' Example: Test Street 1.
        city (str): The city Example: New York.
        postal_code (str): The postal code. If there is no possible value, use '0' Example: 10001.
        street_address_2 (None | str | Unset): The address street (2) Example: Sample Value.
        state_province (str | Unset): The state/province Example: NY.
    """

    country_alpha_2_code: str
    street_address_1: str
    city: str
    postal_code: str
    street_address_2: None | str | Unset = UNSET
    state_province: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        country_alpha_2_code = self.country_alpha_2_code

        street_address_1 = self.street_address_1

        city = self.city

        postal_code = self.postal_code

        street_address_2: None | str | Unset
        if isinstance(self.street_address_2, Unset):
            street_address_2 = UNSET
        else:
            street_address_2 = self.street_address_2

        state_province = self.state_province

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "country_alpha_2_code": country_alpha_2_code,
                "street_address_1": street_address_1,
                "city": city,
                "postal_code": postal_code,
            }
        )
        if street_address_2 is not UNSET:
            field_dict["street_address_2"] = street_address_2
        if state_province is not UNSET:
            field_dict["state_province"] = state_province

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        country_alpha_2_code = d.pop("country_alpha_2_code")

        street_address_1 = d.pop("street_address_1")

        city = d.pop("city")

        postal_code = d.pop("postal_code")

        def _parse_street_address_2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        street_address_2 = _parse_street_address_2(d.pop("street_address_2", UNSET))

        state_province = d.pop("state_province", UNSET)

        address_create = cls(
            country_alpha_2_code=country_alpha_2_code,
            street_address_1=street_address_1,
            city=city,
            postal_code=postal_code,
            street_address_2=street_address_2,
            state_province=state_province,
        )

        address_create.additional_properties = d
        return address_create

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
