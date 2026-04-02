from __future__ import annotations

from collections.abc import Mapping
from typing import Any
from typing import TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.batch_files_response_processed_raw_type_0_url_malware_protection_status import (
    BatchFilesResponseProcessedRawType0UrlMalwareProtectionStatus,
)
from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="BatchFilesResponseProcessedRawType0")


@_attrs_define
class BatchFilesResponseProcessedRawType0:
    """
    Attributes:
        url (str | Unset): The URL to download the processed file content
        url_malware_protection_status (BatchFilesResponseProcessedRawType0UrlMalwareProtectionStatus | Unset): The
            malware protection status of the file (if applicable)
    """

    url: str | Unset = UNSET
    url_malware_protection_status: (
        BatchFilesResponseProcessedRawType0UrlMalwareProtectionStatus | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        url_malware_protection_status: str | Unset = UNSET
        if not isinstance(self.url_malware_protection_status, Unset):
            url_malware_protection_status = self.url_malware_protection_status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if url_malware_protection_status is not UNSET:
            field_dict["url_malware_protection_status"] = url_malware_protection_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url", UNSET)

        _url_malware_protection_status = d.pop("url_malware_protection_status", UNSET)
        url_malware_protection_status: (
            BatchFilesResponseProcessedRawType0UrlMalwareProtectionStatus | Unset
        )
        if isinstance(_url_malware_protection_status, Unset):
            url_malware_protection_status = UNSET
        else:
            url_malware_protection_status = (
                BatchFilesResponseProcessedRawType0UrlMalwareProtectionStatus(
                    _url_malware_protection_status
                )
            )

        batch_files_response_processed_raw_type_0 = cls(
            url=url,
            url_malware_protection_status=url_malware_protection_status,
        )

        batch_files_response_processed_raw_type_0.additional_properties = d
        return batch_files_response_processed_raw_type_0

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
