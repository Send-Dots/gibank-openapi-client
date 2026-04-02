from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING
from typing import Any
from typing import TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET
from ..types import Unset

if TYPE_CHECKING:
    from ..models.get_file_upload_url_response_200_headers import (
        GetFileUploadUrlResponse200Headers,
    )


T = TypeVar("T", bound="GetFileUploadUrlResponse200")


@_attrs_define
class GetFileUploadUrlResponse200:
    """
    Attributes:
        url (str | Unset): The request URL to use to upload the file
        headers (GetFileUploadUrlResponse200Headers | Unset): The request headers to use to upload the file
    """

    url: str | Unset = UNSET
    headers: GetFileUploadUrlResponse200Headers | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if headers is not UNSET:
            field_dict["headers"] = headers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_file_upload_url_response_200_headers import (
            GetFileUploadUrlResponse200Headers,
        )

        d = dict(src_dict)
        url = d.pop("url", UNSET)

        _headers = d.pop("headers", UNSET)
        headers: GetFileUploadUrlResponse200Headers | Unset
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = GetFileUploadUrlResponse200Headers.from_dict(_headers)

        get_file_upload_url_response_200 = cls(
            url=url,
            headers=headers,
        )

        get_file_upload_url_response_200.additional_properties = d
        return get_file_upload_url_response_200

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
