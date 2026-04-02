from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any
from typing import TypeVar
from typing import cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.logo_url_malware_protection_status import LogoUrlMalwareProtectionStatus
from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="CompanyResponseBase")


@_attrs_define
class CompanyResponseBase:
    """
    Attributes:
        id (int | Unset): The company ID Example: 1.
        name (str | Unset): The name of the company Example: ABC Fintech.
        notify_user_id (int | None | Unset): The user ID to send mandatory notifications for the company (e.g., NOC,
            Returns, Outage) Example: 1.
        logo_url (None | str | Unset): The URL to download the company logo (if applicable)
        logo_url_malware_protection_status (LogoUrlMalwareProtectionStatus | Unset): The malware protection status of
            the logo file (if applicable)
        create_date_time (datetime.datetime | Unset): The date and time when the company was created (Stored as UTC,
            formatted as zero UTC offset (Zulu) format) Example: 2024-02-04T23:00:00.000Z.
        update_date_time (datetime.datetime | Unset): The date and time when the company was last updated (Stored as
            UTC, formatted as zero UTC offset (Zulu) format) Example: 2024-02-04T23:00:00.000Z.
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    notify_user_id: int | None | Unset = UNSET
    logo_url: None | str | Unset = UNSET
    logo_url_malware_protection_status: LogoUrlMalwareProtectionStatus | Unset = UNSET
    create_date_time: datetime.datetime | Unset = UNSET
    update_date_time: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

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

        logo_url_malware_protection_status: str | Unset = UNSET
        if not isinstance(self.logo_url_malware_protection_status, Unset):
            logo_url_malware_protection_status = (
                self.logo_url_malware_protection_status.value
            )

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
        if name is not UNSET:
            field_dict["name"] = name
        if notify_user_id is not UNSET:
            field_dict["notify_user_id"] = notify_user_id
        if logo_url is not UNSET:
            field_dict["logo_url"] = logo_url
        if logo_url_malware_protection_status is not UNSET:
            field_dict["logo_url_malware_protection_status"] = (
                logo_url_malware_protection_status
            )
        if create_date_time is not UNSET:
            field_dict["create_date_time"] = create_date_time
        if update_date_time is not UNSET:
            field_dict["update_date_time"] = update_date_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

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

        _logo_url_malware_protection_status = d.pop(
            "logo_url_malware_protection_status", UNSET
        )
        logo_url_malware_protection_status: LogoUrlMalwareProtectionStatus | Unset
        if isinstance(_logo_url_malware_protection_status, Unset):
            logo_url_malware_protection_status = UNSET
        else:
            logo_url_malware_protection_status = LogoUrlMalwareProtectionStatus(
                _logo_url_malware_protection_status
            )

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

        company_response_base = cls(
            id=id,
            name=name,
            notify_user_id=notify_user_id,
            logo_url=logo_url,
            logo_url_malware_protection_status=logo_url_malware_protection_status,
            create_date_time=create_date_time,
            update_date_time=update_date_time,
        )

        company_response_base.additional_properties = d
        return company_response_base

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
