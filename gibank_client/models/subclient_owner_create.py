from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING
from typing import Any
from typing import TypeVar
from typing import cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET
from ..types import Unset

if TYPE_CHECKING:
    from ..models.address_create import AddressCreate


T = TypeVar("T", bound="SubclientOwnerCreate")


@_attrs_define
class SubclientOwnerCreate:
    """
    Example:
        {'name': 'Alice Wonderland', 'title': 'Shareholder', 'active': True, 'external_key': 'AW001', 'birth_date':
            '1985-07-12', 'prong_ownership': True, 'prong_percentage': 30, 'prong_control': False, 'address':
            {'street_address_1': '123 Rabbit Hole Lane', 'city': 'Curious City', 'postal_code': 'CR123',
            'country_alpha_2_code': 'GB'}}

    Attributes:
        name (str): The name of the subclient UBO Example: Ian Crease.
        title (None | str | Unset): The title of the subclient UBO in the company Example: CEO.
        active (bool | Unset): Indicates if the subclient UBO is active Example: True.
        external_key (None | str | Unset): An external identifier for the subclient UBO Example: IVAC0001.
        birth_date (datetime.date | None | Unset): The date of birth (Stored as UTC, formatted as zero UTC offset (Zulu)
            format) Example: 2024-02-04.
        prong_ownership (bool | None | Unset): If Ownership Prong Example: True.
        prong_control (bool | None | Unset): If Control Prong
        prong_percentage (float | None | Unset): The percentage of Ownership (Required if ownership prong) Example: 25.
        address (AddressCreate | Unset):  Example: {'country_alpha_2_code': 'DE', 'street_address_1': 'Musterstraße 10',
            'city': 'Berlin', 'postal_code': '10117'}.
    """

    name: str
    title: None | str | Unset = UNSET
    active: bool | Unset = UNSET
    external_key: None | str | Unset = UNSET
    birth_date: datetime.date | None | Unset = UNSET
    prong_ownership: bool | None | Unset = UNSET
    prong_control: bool | None | Unset = UNSET
    prong_percentage: float | None | Unset = UNSET
    address: AddressCreate | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        active = self.active

        external_key: None | str | Unset
        if isinstance(self.external_key, Unset):
            external_key = UNSET
        else:
            external_key = self.external_key

        birth_date: None | str | Unset
        if isinstance(self.birth_date, Unset):
            birth_date = UNSET
        elif isinstance(self.birth_date, datetime.date):
            birth_date = self.birth_date.isoformat()
        else:
            birth_date = self.birth_date

        prong_ownership: bool | None | Unset
        if isinstance(self.prong_ownership, Unset):
            prong_ownership = UNSET
        else:
            prong_ownership = self.prong_ownership

        prong_control: bool | None | Unset
        if isinstance(self.prong_control, Unset):
            prong_control = UNSET
        else:
            prong_control = self.prong_control

        prong_percentage: float | None | Unset
        if isinstance(self.prong_percentage, Unset):
            prong_percentage = UNSET
        else:
            prong_percentage = self.prong_percentage

        address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if active is not UNSET:
            field_dict["active"] = active
        if external_key is not UNSET:
            field_dict["external_key"] = external_key
        if birth_date is not UNSET:
            field_dict["birth_date"] = birth_date
        if prong_ownership is not UNSET:
            field_dict["prong_ownership"] = prong_ownership
        if prong_control is not UNSET:
            field_dict["prong_control"] = prong_control
        if prong_percentage is not UNSET:
            field_dict["prong_percentage"] = prong_percentage
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address_create import AddressCreate

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        active = d.pop("active", UNSET)

        def _parse_external_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_key = _parse_external_key(d.pop("external_key", UNSET))

        def _parse_birth_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemasbirth_date_type_0 = isoparse(data).date()

                return componentsschemasbirth_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        birth_date = _parse_birth_date(d.pop("birth_date", UNSET))

        def _parse_prong_ownership(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        prong_ownership = _parse_prong_ownership(d.pop("prong_ownership", UNSET))

        def _parse_prong_control(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        prong_control = _parse_prong_control(d.pop("prong_control", UNSET))

        def _parse_prong_percentage(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        prong_percentage = _parse_prong_percentage(d.pop("prong_percentage", UNSET))

        _address = d.pop("address", UNSET)
        address: AddressCreate | Unset
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = AddressCreate.from_dict(_address)

        subclient_owner_create = cls(
            name=name,
            title=title,
            active=active,
            external_key=external_key,
            birth_date=birth_date,
            prong_ownership=prong_ownership,
            prong_control=prong_control,
            prong_percentage=prong_percentage,
            address=address,
        )

        subclient_owner_create.additional_properties = d
        return subclient_owner_create

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
