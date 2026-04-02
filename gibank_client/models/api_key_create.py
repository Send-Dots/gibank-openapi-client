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

T = TypeVar("T", bound="ApiKeyCreate")


@_attrs_define
class ApiKeyCreate:
    """
    Example:
        {'description': 'Nightly batch processing script', 'active': True, 'expiration_date_time':
            '2026-01-01T00:00:00.000Z', 'ip_whitelist': '203.0.113.42, 198.51.100.0/24', 'ip_blacklist': '192.0.2.10'}

    Attributes:
        description (str): The description of the API Key Example: Auto submit script.
        ip_whitelist (str): The IP addresses that are allowed to use the API Key Example: 172.217.22.14, 172.217.22.13.
        active (bool | Unset): Indicates if the API Key is active Example: True.
        expiration_date_time (datetime.datetime | None | Unset): The date time when the API Key expires (Stored as UTC,
            formatted as zero UTC offset (Zulu) format) Example: 2024-02-04T23:00:00.000Z.
        ip_blacklist (None | str | Unset): The IP addresses that are blocked to use the API Key Example: 172.217.22.12,
            172.217.22.11.
    """

    description: str
    ip_whitelist: str
    active: bool | Unset = UNSET
    expiration_date_time: datetime.datetime | None | Unset = UNSET
    ip_blacklist: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        ip_whitelist = self.ip_whitelist

        active = self.active

        expiration_date_time: None | str | Unset
        if isinstance(self.expiration_date_time, Unset):
            expiration_date_time = UNSET
        elif isinstance(self.expiration_date_time, datetime.datetime):
            expiration_date_time = self.expiration_date_time.isoformat()
        else:
            expiration_date_time = self.expiration_date_time

        ip_blacklist: None | str | Unset
        if isinstance(self.ip_blacklist, Unset):
            ip_blacklist = UNSET
        else:
            ip_blacklist = self.ip_blacklist

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "ip_whitelist": ip_whitelist,
            }
        )
        if active is not UNSET:
            field_dict["active"] = active
        if expiration_date_time is not UNSET:
            field_dict["expiration_date_time"] = expiration_date_time
        if ip_blacklist is not UNSET:
            field_dict["ip_blacklist"] = ip_blacklist

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description")

        ip_whitelist = d.pop("ip_whitelist")

        active = d.pop("active", UNSET)

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
                componentsschemasexpiration_date_time_type_0 = isoparse(data)

                return componentsschemasexpiration_date_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expiration_date_time = _parse_expiration_date_time(
            d.pop("expiration_date_time", UNSET)
        )

        def _parse_ip_blacklist(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ip_blacklist = _parse_ip_blacklist(d.pop("ip_blacklist", UNSET))

        api_key_create = cls(
            description=description,
            ip_whitelist=ip_whitelist,
            active=active,
            expiration_date_time=expiration_date_time,
            ip_blacklist=ip_blacklist,
        )

        api_key_create.additional_properties = d
        return api_key_create

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
