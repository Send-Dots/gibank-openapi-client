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

T = TypeVar("T", bound="SubclientOwnerFields")


@_attrs_define
class SubclientOwnerFields:
    """
    Attributes:
        id (float | Unset): The subclient UBO ID Example: 1.
        subclient_id (float | Unset): The subclient ID, the identifier of the Business associated with the UBO. Example:
            1.
        company_id (float | Unset): The company ID (Same as company ID of Subclient) Example: 1.
        name (str | Unset): The name of the subclient UBO Example: Ian Crease.
        title (None | str | Unset): The title of the subclient UBO in the company Example: CEO.
        active (bool | Unset): Indicates if the subclient UBO is active Default: True. Example: True.
        external_key (None | str | Unset): An external identifier for the subclient UBO Example: IVAC0001.
        birth_date (datetime.date | None | Unset): The date of birth (Stored as UTC, formatted as zero UTC offset (Zulu)
            format) Example: 2024-02-04.
        prong_ownership (bool | None | Unset): If Ownership Prong Example: True.
        prong_control (bool | None | Unset): If Control Prong
        prong_percentage (float | None | Unset): The percentage of Ownership (Required if ownership prong) Example: 25.
        create_date_time (datetime.datetime | Unset): The date and time when the subclient UBO was created (Stored as
            UTC, formatted as zero UTC offset (Zulu) format) Example: 2024-02-04T23:00:00.000Z.
        update_date_time (datetime.datetime | Unset): The date and time when the subclient UBO was last updated (Stored
            as UTC, formatted as zero UTC offset (Zulu) format) Example: 2024-02-04T23:00:00.000Z.
        create_user_id (float | Unset): The ID of the user who created the subclient UBO Example: 1.
        update_user_id (float | Unset): The ID of the user who last updated the subclient UBO Example: 1.
    """

    id: float | Unset = UNSET
    subclient_id: float | Unset = UNSET
    company_id: float | Unset = UNSET
    name: str | Unset = UNSET
    title: None | str | Unset = UNSET
    active: bool | Unset = True
    external_key: None | str | Unset = UNSET
    birth_date: datetime.date | None | Unset = UNSET
    prong_ownership: bool | None | Unset = UNSET
    prong_control: bool | None | Unset = UNSET
    prong_percentage: float | None | Unset = UNSET
    create_date_time: datetime.datetime | Unset = UNSET
    update_date_time: datetime.datetime | Unset = UNSET
    create_user_id: float | Unset = UNSET
    update_user_id: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        subclient_id = self.subclient_id

        company_id = self.company_id

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
        if subclient_id is not UNSET:
            field_dict["subclient_id"] = subclient_id
        if company_id is not UNSET:
            field_dict["company_id"] = company_id
        if name is not UNSET:
            field_dict["name"] = name
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

        subclient_id = d.pop("subclient_id", UNSET)

        company_id = d.pop("company_id", UNSET)

        name = d.pop("name", UNSET)

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
                birth_date_type_0 = isoparse(data).date()

                return birth_date_type_0
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

        subclient_owner_fields = cls(
            id=id,
            subclient_id=subclient_id,
            company_id=company_id,
            name=name,
            title=title,
            active=active,
            external_key=external_key,
            birth_date=birth_date,
            prong_ownership=prong_ownership,
            prong_control=prong_control,
            prong_percentage=prong_percentage,
            create_date_time=create_date_time,
            update_date_time=update_date_time,
            create_user_id=create_user_id,
            update_user_id=update_user_id,
        )

        subclient_owner_fields.additional_properties = d
        return subclient_owner_fields

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
