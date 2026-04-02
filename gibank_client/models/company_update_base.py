from __future__ import annotations

from collections.abc import Mapping
from typing import Any
from typing import TypeVar
from typing import cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="CompanyUpdateBase")


@_attrs_define
class CompanyUpdateBase:
    """
    Example:
        {'name': 'New Innovations Group'}

    Attributes:
        name (str | Unset): The name of the company Example: ABC Fintech.
        notify_user_id (int | None | Unset): The user ID to send mandatory notifications for the company (e.g., NOC,
            Returns, Outage) Example: 1.
        logo_url (None | str | Unset): Temporary URL of the uploaded logo file (e.g., pre-signed S3 URL from a previous
            upload step). Example: https://s3.amazonaws.com/temp-bucket/some_temp_id/logo.png?AWSAccessKeyId=....
    """

    name: str | Unset = UNSET
    notify_user_id: int | None | Unset = UNSET
    logo_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        notify_user_id: int | None | Unset
        if isinstance(self.notify_user_id, Unset):
            notify_user_id = UNSET
        else:
            notify_user_id = self.notify_user_id

        logo_url: None | str | Unset
        if isinstance(self.logo_url, Unset):
            logo_url = UNSET
        else:
            logo_url = self.logo_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if notify_user_id is not UNSET:
            field_dict["notify_user_id"] = notify_user_id
        if logo_url is not UNSET:
            field_dict["logo_url"] = logo_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_notify_user_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        notify_user_id = _parse_notify_user_id(d.pop("notify_user_id", UNSET))

        def _parse_logo_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        logo_url = _parse_logo_url(d.pop("logo_url", UNSET))

        company_update_base = cls(
            name=name,
            notify_user_id=notify_user_id,
            logo_url=logo_url,
        )

        company_update_base.additional_properties = d
        return company_update_base

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
