from __future__ import annotations

from collections.abc import Mapping
from typing import Any
from typing import TypeVar
from typing import cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.relationship import Relationship
from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="UserUpdateBase")


@_attrs_define
class UserUpdateBase:
    """
    Example:
        {'full_name': 'Updated User Name', 'role_id': 6}

    Attributes:
        full_name (str | Unset): The full name of the user Example: Max Mustermann.
        title (None | str | Unset): The title of the user Example: Dr.
        active (bool | Unset): Indicates if the user is active Example: True.
        department (None | str | Unset): The department of the user Example: Engineering.
        phone_number (None | str | Unset): The phone number of the user Example: +1456985346.
        relationship (Relationship | Unset): The relationship of the user in the company Example: employee.
        role_id (int | Unset): The RBAC role ID Example: 1.
        profile_picture_url (None | str | Unset): Temporary URL of the uploaded file (e.g., pre-signed S3 URL from a
            previous upload step). Example: https://s3.amazonaws.com/temp-bucket/some_temp_id/john.jpeg?AWSAccessKeyId=....
    """

    full_name: str | Unset = UNSET
    title: None | str | Unset = UNSET
    active: bool | Unset = UNSET
    department: None | str | Unset = UNSET
    phone_number: None | str | Unset = UNSET
    relationship: Relationship | Unset = UNSET
    role_id: int | Unset = UNSET
    profile_picture_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        full_name = self.full_name

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        active = self.active

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

        profile_picture_url: None | str | Unset
        if isinstance(self.profile_picture_url, Unset):
            profile_picture_url = UNSET
        else:
            profile_picture_url = self.profile_picture_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if full_name is not UNSET:
            field_dict["full_name"] = full_name
        if title is not UNSET:
            field_dict["title"] = title
        if active is not UNSET:
            field_dict["active"] = active
        if department is not UNSET:
            field_dict["department"] = department
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if relationship is not UNSET:
            field_dict["relationship"] = relationship
        if role_id is not UNSET:
            field_dict["role_id"] = role_id
        if profile_picture_url is not UNSET:
            field_dict["profile_picture_url"] = profile_picture_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        full_name = d.pop("full_name", UNSET)

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        active = d.pop("active", UNSET)

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

        def _parse_profile_picture_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        profile_picture_url = _parse_profile_picture_url(
            d.pop("profile_picture_url", UNSET)
        )

        user_update_base = cls(
            full_name=full_name,
            title=title,
            active=active,
            department=department,
            phone_number=phone_number,
            relationship=relationship,
            role_id=role_id,
            profile_picture_url=profile_picture_url,
        )

        user_update_base.additional_properties = d
        return user_update_base

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
