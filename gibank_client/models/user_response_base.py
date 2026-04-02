from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any
from typing import TypeVar
from typing import cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.profile_picture_url_malware_protection_status import (
    ProfilePictureUrlMalwareProtectionStatus,
)
from ..models.relationship import Relationship
from ..models.type_ import Type
from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="UserResponseBase")


@_attrs_define
class UserResponseBase:
    """
    Attributes:
        id (int | Unset): The user ID Example: 1.
        email (str | Unset): The email address of the user Example: your-email@example.com.
        type_ (Type | Unset): The type of the user Example: client.
        full_name (str | Unset): The full name of the user Example: Max Mustermann.
        company_id (int | None | Unset): The company ID Example: 1.
        company_name (None | str | Unset): The company name of the user Example: ABC Fintech.
        title (None | str | Unset): The title of the user Example: Dr.
        department (None | str | Unset): The department of the user Example: Engineering.
        phone_number (None | str | Unset): The phone number of the user Example: +1456985346.
        relationship (Relationship | Unset): The relationship of the user in the company Example: employee.
        role_id (int | Unset): The RBAC role ID Example: 1.
        role_key (str | Unset): The role key of the user Example: client.
        role_name (str | Unset): The role name of the user Example: Client.
        profile_picture_url (None | str | Unset): The URL to download the profile picture (if applicable)
        profile_picture_url_malware_protection_status (ProfilePictureUrlMalwareProtectionStatus | Unset): The malware
            protection status of the file (if applicable)
        create_date_time (datetime.datetime | Unset): The date and time when the user was created (Stored as UTC,
            formatted as zero UTC offset (Zulu) format) Example: 2024-02-04T23:00:00.000Z.
        update_date_time (datetime.datetime | Unset): The date and time when the user was last updated (Stored as UTC,
            formatted as zero UTC offset (Zulu) format) Example: 2024-02-04T23:00:00.000Z.
    """

    id: int | Unset = UNSET
    email: str | Unset = UNSET
    type_: Type | Unset = UNSET
    full_name: str | Unset = UNSET
    company_id: int | None | Unset = UNSET
    company_name: None | str | Unset = UNSET
    title: None | str | Unset = UNSET
    department: None | str | Unset = UNSET
    phone_number: None | str | Unset = UNSET
    relationship: Relationship | Unset = UNSET
    role_id: int | Unset = UNSET
    role_key: str | Unset = UNSET
    role_name: str | Unset = UNSET
    profile_picture_url: None | str | Unset = UNSET
    profile_picture_url_malware_protection_status: (
        ProfilePictureUrlMalwareProtectionStatus | Unset
    ) = UNSET
    create_date_time: datetime.datetime | Unset = UNSET
    update_date_time: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        email = self.email

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        full_name = self.full_name

        company_id: int | None | Unset
        if isinstance(self.company_id, Unset):
            company_id = UNSET
        else:
            company_id = self.company_id

        company_name: None | str | Unset
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        else:
            company_name = self.company_name

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        department: None | str | Unset
        if isinstance(self.department, Unset):
            department = UNSET
        else:
            department = self.department

        phone_number: None | str | Unset
        if isinstance(self.phone_number, Unset):
            phone_number = UNSET
        else:
            phone_number = self.phone_number

        relationship: str | Unset = UNSET
        if not isinstance(self.relationship, Unset):
            relationship = self.relationship.value

        role_id = self.role_id

        role_key = self.role_key

        role_name = self.role_name

        profile_picture_url: None | str | Unset
        if isinstance(self.profile_picture_url, Unset):
            profile_picture_url = UNSET
        else:
            profile_picture_url = self.profile_picture_url

        profile_picture_url_malware_protection_status: str | Unset = UNSET
        if not isinstance(self.profile_picture_url_malware_protection_status, Unset):
            profile_picture_url_malware_protection_status = (
                self.profile_picture_url_malware_protection_status.value
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
        if email is not UNSET:
            field_dict["email"] = email
        if type_ is not UNSET:
            field_dict["type"] = type_
        if full_name is not UNSET:
            field_dict["full_name"] = full_name
        if company_id is not UNSET:
            field_dict["company_id"] = company_id
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if title is not UNSET:
            field_dict["title"] = title
        if department is not UNSET:
            field_dict["department"] = department
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if relationship is not UNSET:
            field_dict["relationship"] = relationship
        if role_id is not UNSET:
            field_dict["role_id"] = role_id
        if role_key is not UNSET:
            field_dict["role_key"] = role_key
        if role_name is not UNSET:
            field_dict["role_name"] = role_name
        if profile_picture_url is not UNSET:
            field_dict["profile_picture_url"] = profile_picture_url
        if profile_picture_url_malware_protection_status is not UNSET:
            field_dict["profile_picture_url_malware_protection_status"] = (
                profile_picture_url_malware_protection_status
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

        email = d.pop("email", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Type | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = Type(_type_)

        full_name = d.pop("full_name", UNSET)

        def _parse_company_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        company_id = _parse_company_id(d.pop("company_id", UNSET))

        def _parse_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_name = _parse_company_name(d.pop("company_name", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_department(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        department = _parse_department(d.pop("department", UNSET))

        def _parse_phone_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone_number = _parse_phone_number(d.pop("phone_number", UNSET))

        _relationship = d.pop("relationship", UNSET)
        relationship: Relationship | Unset
        if isinstance(_relationship, Unset):
            relationship = UNSET
        else:
            relationship = Relationship(_relationship)

        role_id = d.pop("role_id", UNSET)

        role_key = d.pop("role_key", UNSET)

        role_name = d.pop("role_name", UNSET)

        def _parse_profile_picture_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        profile_picture_url = _parse_profile_picture_url(
            d.pop("profile_picture_url", UNSET)
        )

        _profile_picture_url_malware_protection_status = d.pop(
            "profile_picture_url_malware_protection_status", UNSET
        )
        profile_picture_url_malware_protection_status: (
            ProfilePictureUrlMalwareProtectionStatus | Unset
        )
        if isinstance(_profile_picture_url_malware_protection_status, Unset):
            profile_picture_url_malware_protection_status = UNSET
        else:
            profile_picture_url_malware_protection_status = (
                ProfilePictureUrlMalwareProtectionStatus(
                    _profile_picture_url_malware_protection_status
                )
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

        user_response_base = cls(
            id=id,
            email=email,
            type_=type_,
            full_name=full_name,
            company_id=company_id,
            company_name=company_name,
            title=title,
            department=department,
            phone_number=phone_number,
            relationship=relationship,
            role_id=role_id,
            role_key=role_key,
            role_name=role_name,
            profile_picture_url=profile_picture_url,
            profile_picture_url_malware_protection_status=profile_picture_url_malware_protection_status,
            create_date_time=create_date_time,
            update_date_time=update_date_time,
        )

        user_response_base.additional_properties = d
        return user_response_base

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
