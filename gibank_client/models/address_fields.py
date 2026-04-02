from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any
from typing import TypeVar
from typing import cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="AddressFields")


@_attrs_define
class AddressFields:
    """
    Attributes:
        id (float | Unset): The address ID Example: 1.
        country_id (float | Unset): The internal country ID (Not needed during creations/updates; feel free to use the
            ISO code) Example: 1.
        country_alpha_2_code (str | Unset): The country ISO 3166-1 alpha-2 code Example: US.
        type_ (str | Unset): The address type Example: default.
        street_address_1 (str | Unset): The address street (1). If there is no possible value, use 'NA' Example: Test
            Street 1.
        street_address_2 (None | str | Unset): The address street (2) Example: Sample Value.
        city (str | Unset): The city Example: New York.
        state_province (str | Unset): The state/province Example: NY.
        postal_code (str | Unset): The postal code. If there is no possible value, use '0' Example: 10001.
        create_date_time (datetime.datetime | Unset): The date and time when the address was created (Stored as UTC,
            formatted as zero UTC offset (Zulu) format) Example: 2024-02-04T23:00:00.000Z.
        update_date_time (datetime.datetime | Unset): The date and time when the address was last updated (Stored as
            UTC, formatted as zero UTC offset (Zulu) format) Example: 2024-02-04T23:00:00.000Z.
        create_user_id (float | Unset): The ID of the user who created the address Example: 1.
        update_user_id (float | Unset): The ID of the user who last updated the address Example: 1.
    """

    id: float | Unset = UNSET
    country_id: float | Unset = UNSET
    country_alpha_2_code: str | Unset = UNSET
    type_: str | Unset = UNSET
    street_address_1: str | Unset = UNSET
    street_address_2: None | str | Unset = UNSET
    city: str | Unset = UNSET
    state_province: str | Unset = UNSET
    postal_code: str | Unset = UNSET
    create_date_time: datetime.datetime | Unset = UNSET
    update_date_time: datetime.datetime | Unset = UNSET
    create_user_id: float | Unset = UNSET
    update_user_id: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        country_id = self.country_id

        country_alpha_2_code = self.country_alpha_2_code

        type_ = self.type_

        street_address_1 = self.street_address_1

        street_address_2: None | str | Unset
        if isinstance(self.street_address_2, Unset):
            street_address_2 = UNSET
        else:
            street_address_2 = self.street_address_2

        city = self.city

        state_province = self.state_province

        postal_code = self.postal_code

        create_date_time: str | Unset = UNSET
        if not isinstance(self.create_date_time, Unset):
            create_date_time = self.create_date_time.isoformat()

        update_date_time: str | Unset = UNSET
        if not isinstance(self.update_date_time, Unset):
            update_date_time = self.update_date_time.isoformat()

        create_user_id = self.create_user_id

        update_user_id = self.update_user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if country_id is not UNSET:
            field_dict["country_id"] = country_id
        if country_alpha_2_code is not UNSET:
            field_dict["country_alpha_2_code"] = country_alpha_2_code
        if type_ is not UNSET:
            field_dict["type"] = type_
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
        if create_date_time is not UNSET:
            field_dict["create_date_time"] = create_date_time
        if update_date_time is not UNSET:
            field_dict["update_date_time"] = update_date_time
        if create_user_id is not UNSET:
            field_dict["create_user_id"] = create_user_id
        if update_user_id is not UNSET:
            field_dict["update_user_id"] = update_user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        country_id = d.pop("country_id", UNSET)

        country_alpha_2_code = d.pop("country_alpha_2_code", UNSET)

        type_ = d.pop("type", UNSET)

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

        _create_date_time = d.pop("create_date_time", UNSET)
        create_date_time: datetime.datetime | Unset
        if isinstance(_create_date_time, Unset):
            create_date_time = UNSET
        else:
            create_date_time = isoparse(_create_date_time)

        _update_date_time = d.pop("update_date_time", UNSET)
        update_date_time: datetime.datetime | Unset
        if isinstance(_update_date_time, Unset):
            update_date_time = UNSET
        else:
            update_date_time = isoparse(_update_date_time)

        create_user_id = d.pop("create_user_id", UNSET)

        update_user_id = d.pop("update_user_id", UNSET)

        address_fields = cls(
            id=id,
            country_id=country_id,
            country_alpha_2_code=country_alpha_2_code,
            type_=type_,
            street_address_1=street_address_1,
            street_address_2=street_address_2,
            city=city,
            state_province=state_province,
            postal_code=postal_code,
            create_date_time=create_date_time,
            update_date_time=update_date_time,
            create_user_id=create_user_id,
            update_user_id=update_user_id,
        )

        address_fields.additional_properties = d
        return address_fields

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
