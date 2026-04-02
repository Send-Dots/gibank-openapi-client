from __future__ import annotations

from collections.abc import Mapping
from typing import Any
from typing import TypeVar
from typing import cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.session_response_user_profile_picture_url_malware_protection_status import (
    SessionResponseUserProfilePictureUrlMalwareProtectionStatus,
)
from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="SessionResponseUser")


@_attrs_define
class SessionResponseUser:
    """
    Attributes:
        id (int | Unset): The user ID Example: 1.
        email (str | Unset): The email address of the user Example: your-email@example.com.
        full_name (str | Unset): The full name of the user Example: Max Mustermann.
        profile_picture_url (None | str | Unset): The URL to download the profile picture (if applicable)
        profile_picture_url_malware_protection_status (SessionResponseUserProfilePictureUrlMalwareProtectionStatus |
            Unset): The malware protection status of the file (if applicable)
        external_key_novu (None | str | Unset): The external key used by notification system Novu Example: 123e4567.
    """

    id: int | Unset = UNSET
    email: str | Unset = UNSET
    full_name: str | Unset = UNSET
    profile_picture_url: None | str | Unset = UNSET
    profile_picture_url_malware_protection_status: (
        SessionResponseUserProfilePictureUrlMalwareProtectionStatus | Unset
    ) = UNSET
    external_key_novu: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        email = self.email

        full_name = self.full_name

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

        external_key_novu: None | str | Unset
        if isinstance(self.external_key_novu, Unset):
            external_key_novu = UNSET
        else:
            external_key_novu = self.external_key_novu

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if email is not UNSET:
            field_dict["email"] = email
        if full_name is not UNSET:
            field_dict["full_name"] = full_name
        if profile_picture_url is not UNSET:
            field_dict["profile_picture_url"] = profile_picture_url
        if profile_picture_url_malware_protection_status is not UNSET:
            field_dict["profile_picture_url_malware_protection_status"] = (
                profile_picture_url_malware_protection_status
            )
        if external_key_novu is not UNSET:
            field_dict["external_key_novu"] = external_key_novu

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        email = d.pop("email", UNSET)

        full_name = d.pop("full_name", UNSET)

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
            SessionResponseUserProfilePictureUrlMalwareProtectionStatus | Unset
        )
        if isinstance(_profile_picture_url_malware_protection_status, Unset):
            profile_picture_url_malware_protection_status = UNSET
        else:
            profile_picture_url_malware_protection_status = (
                SessionResponseUserProfilePictureUrlMalwareProtectionStatus(
                    _profile_picture_url_malware_protection_status
                )
            )

        def _parse_external_key_novu(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_key_novu = _parse_external_key_novu(d.pop("external_key_novu", UNSET))

        session_response_user = cls(
            id=id,
            email=email,
            full_name=full_name,
            profile_picture_url=profile_picture_url,
            profile_picture_url_malware_protection_status=profile_picture_url_malware_protection_status,
            external_key_novu=external_key_novu,
        )

        session_response_user.additional_properties = d
        return session_response_user

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
