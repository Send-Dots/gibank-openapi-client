from __future__ import annotations

from collections.abc import Mapping
from typing import Any
from typing import TypeVar
from typing import cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="ApiKeyUpdate")


@_attrs_define
class ApiKeyUpdate:
    """
    Example:
        {'description': 'Nightly batch processing script (Revoked)', 'active': False}

    Attributes:
        description (str | Unset): The description of the API Key Example: Auto submit script.
        active (bool | Unset): Indicates if the API Key is active Example: True.
        ip_whitelist (str | Unset): The IP addresses that are allowed to use the API Key Example: 172.217.22.14,
            172.217.22.13.
        ip_blacklist (None | str | Unset): The IP addresses that are blocked to use the API Key Example: 172.217.22.12,
            172.217.22.11.
    """

    description: str | Unset = UNSET
    active: bool | Unset = UNSET
    ip_whitelist: str | Unset = UNSET
    ip_blacklist: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        active = self.active

        ip_whitelist = self.ip_whitelist

        ip_blacklist: None | str | Unset
        if isinstance(self.ip_blacklist, Unset):
            ip_blacklist = UNSET
        else:
            ip_blacklist = self.ip_blacklist

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if active is not UNSET:
            field_dict["active"] = active
        if ip_whitelist is not UNSET:
            field_dict["ip_whitelist"] = ip_whitelist
        if ip_blacklist is not UNSET:
            field_dict["ip_blacklist"] = ip_blacklist

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
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

        api_key_update = cls(
            description=description,
            active=active,
            ip_whitelist=ip_whitelist,
            ip_blacklist=ip_blacklist,
        )

        api_key_update.additional_properties = d
        return api_key_update

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
