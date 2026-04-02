from __future__ import annotations

from collections.abc import Mapping
from typing import Any
from typing import TypeVar
from typing import cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="AttachmentUpdate")


@_attrs_define
class AttachmentUpdate:
    """
    Example:
        {'description': "John Doe's Passport Scan (verified)", 'active': True}

    Attributes:
        description (None | str | Unset): A description of the attachment Example: User's passport scan.
        active (bool | Unset): Indicates if the attachment is active Example: True.
        language_alpha_3_code (None | str | Unset): The ISO 639-2 code for the lanuage the document is in Example: eng.
    """

    description: None | str | Unset = UNSET
    active: bool | Unset = UNSET
    language_alpha_3_code: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        active = self.active

        language_alpha_3_code: None | str | Unset
        if isinstance(self.language_alpha_3_code, Unset):
            language_alpha_3_code = UNSET
        else:
            language_alpha_3_code = self.language_alpha_3_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if active is not UNSET:
            field_dict["active"] = active
        if language_alpha_3_code is not UNSET:
            field_dict["language_alpha_3_code"] = language_alpha_3_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        active = d.pop("active", UNSET)

        def _parse_language_alpha_3_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        language_alpha_3_code = _parse_language_alpha_3_code(
            d.pop("language_alpha_3_code", UNSET)
        )

        attachment_update = cls(
            description=description,
            active=active,
            language_alpha_3_code=language_alpha_3_code,
        )

        attachment_update.additional_properties = d
        return attachment_update

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
