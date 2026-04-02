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

T = TypeVar("T", bound="ApiKeyFields")


@_attrs_define
class ApiKeyFields:
    """
    Attributes:
        id (float | Unset): The API Key ID Example: 1.
        user_id (float | Unset): The user ID Example: 1.
        description (str | Unset): The description of the API Key Example: Auto submit script.
        active (bool | Unset): Indicates if the API Key is active Default: True. Example: True.
        ip_whitelist (str | Unset): The IP addresses that are allowed to use the API Key Example: 172.217.22.14,
            172.217.22.13.
        ip_blacklist (None | str | Unset): The IP addresses that are blocked to use the API Key Example: 172.217.22.12,
            172.217.22.11.
        api_key (str | Unset): The API Key Example: ey....
        expiration_date_time (datetime.datetime | None | Unset): The date time when the API Key expires (Stored as UTC,
            formatted as zero UTC offset (Zulu) format) Example: 2024-02-04T23:00:00.000Z.
        expired (bool | Unset): If the key is expired
        last_used_date (datetime.date | None | Unset): The date when the API Key was last used (Stored as UTC, formatted
            as zero UTC offset (Zulu) format) Example: 2024-02-04.
        create_date_time (datetime.datetime | Unset): The date and time when the API Key was created (Stored as UTC,
            formatted as zero UTC offset (Zulu) format) Example: 2024-02-04T23:00:00.000Z.
        update_date_time (datetime.datetime | Unset): The date and time when the API Key was last updated (Stored as
            UTC, formatted as zero UTC offset (Zulu) format) Example: 2024-02-04T23:00:00.000Z.
    """

    id: float | Unset = UNSET
    user_id: float | Unset = UNSET
    description: str | Unset = UNSET
    active: bool | Unset = True
    ip_whitelist: str | Unset = UNSET
    ip_blacklist: None | str | Unset = UNSET
    api_key: str | Unset = UNSET
    expiration_date_time: datetime.datetime | None | Unset = UNSET
    expired: bool | Unset = UNSET
    last_used_date: datetime.date | None | Unset = UNSET
    create_date_time: datetime.datetime | Unset = UNSET
    update_date_time: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user_id = self.user_id

        description = self.description

        active = self.active

        ip_whitelist = self.ip_whitelist

        ip_blacklist: None | str | Unset
        if isinstance(self.ip_blacklist, Unset):
            ip_blacklist = UNSET
        else:
            ip_blacklist = self.ip_blacklist

        api_key = self.api_key

        expiration_date_time: None | str | Unset
        if isinstance(self.expiration_date_time, Unset):
            expiration_date_time = UNSET
        elif isinstance(self.expiration_date_time, datetime.datetime):
            expiration_date_time = self.expiration_date_time.isoformat()
        else:
            expiration_date_time = self.expiration_date_time

        expired = self.expired

        last_used_date: None | str | Unset
        if isinstance(self.last_used_date, Unset):
            last_used_date = UNSET
        elif isinstance(self.last_used_date, datetime.date):
            last_used_date = self.last_used_date.isoformat()
        else:
            last_used_date = self.last_used_date

        create_date_time: str | Unset = UNSET
        if not isinstance(self.create_date_time, Unset):
            create_date_time = self.create_date_time.isoformat()

        update_date_time: str | Unset = UNSET
        if not isinstance(self.update_date_time, Unset):
            update_date_time = self.update_date_time.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if description is not UNSET:
            field_dict["description"] = description
        if active is not UNSET:
            field_dict["active"] = active
        if ip_whitelist is not UNSET:
            field_dict["ip_whitelist"] = ip_whitelist
        if ip_blacklist is not UNSET:
            field_dict["ip_blacklist"] = ip_blacklist
        if api_key is not UNSET:
            field_dict["api_key"] = api_key
        if expiration_date_time is not UNSET:
            field_dict["expiration_date_time"] = expiration_date_time
        if expired is not UNSET:
            field_dict["expired"] = expired
        if last_used_date is not UNSET:
            field_dict["last_used_date"] = last_used_date
        if create_date_time is not UNSET:
            field_dict["create_date_time"] = create_date_time
        if update_date_time is not UNSET:
            field_dict["update_date_time"] = update_date_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        user_id = d.pop("user_id", UNSET)

        description = d.pop("description", UNSET)

        active = d.pop("active", UNSET)

        ip_whitelist = d.pop("ip_whitelist", UNSET)

        def _parse_ip_blacklist(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ip_blacklist = _parse_ip_blacklist(d.pop("ip_blacklist", UNSET))

        api_key = d.pop("api_key", UNSET)

        def _parse_expiration_date_time(
            data: object,
        ) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expiration_date_time_type_0 = isoparse(data)

                return expiration_date_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expiration_date_time = _parse_expiration_date_time(
            d.pop("expiration_date_time", UNSET)
        )

        expired = d.pop("expired", UNSET)

        def _parse_last_used_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_used_date_type_0 = isoparse(data).date()

                return last_used_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        last_used_date = _parse_last_used_date(d.pop("last_used_date", UNSET))

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

        api_key_fields = cls(
            id=id,
            user_id=user_id,
            description=description,
            active=active,
            ip_whitelist=ip_whitelist,
            ip_blacklist=ip_blacklist,
            api_key=api_key,
            expiration_date_time=expiration_date_time,
            expired=expired,
            last_used_date=last_used_date,
            create_date_time=create_date_time,
            update_date_time=update_date_time,
        )

        api_key_fields.additional_properties = d
        return api_key_fields

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
