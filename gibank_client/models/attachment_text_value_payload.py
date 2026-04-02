from __future__ import annotations

from collections.abc import Mapping
from typing import Any
from typing import TypeVar
from typing import cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AttachmentTextValuePayload")


@_attrs_define
class AttachmentTextValuePayload:
    """Details required when the attachment is text-based.

    Attributes:
        text_value (None | str): The text value of the attachment Example: 123456789.
    """

    text_value: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text_value: None | str
        text_value = self.text_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text_value": text_value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_text_value(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        text_value = _parse_text_value(d.pop("text_value"))

        attachment_text_value_payload = cls(
            text_value=text_value,
        )

        attachment_text_value_payload.additional_properties = d
        return attachment_text_value_payload

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
