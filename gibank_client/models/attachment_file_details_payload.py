from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any
from typing import TypeVar
from typing import cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="AttachmentFileDetailsPayload")


@_attrs_define
class AttachmentFileDetailsPayload:
    """Details required when the attachment is a file.

    Attributes:
        url (str): Temporary URL of the uploaded file (e.g., pre-signed S3 URL from a previous upload step). Example:
            https://s3.amazonaws.com/temp-bucket/some_temp_id/passport.pdf?AWSAccessKeyId=....
        file_name_original (None | str): The original file name Example: passport_scan.pdf.
        file_extension (None | str): The file extension Example: pdf.
        file_create_date_time (datetime.datetime | None): The date and time when the file was created (if applicable)
            (Stored as UTC, formatted as zero UTC offset (Zulu) format) Example: 2024-02-04T23:00:00.000Z.
    """

    url: str
    file_name_original: None | str
    file_extension: None | str
    file_create_date_time: datetime.datetime | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        file_name_original: None | str
        file_name_original = self.file_name_original

        file_extension: None | str
        file_extension = self.file_extension

        file_create_date_time: None | str
        if isinstance(self.file_create_date_time, datetime.datetime):
            file_create_date_time = self.file_create_date_time.isoformat()
        else:
            file_create_date_time = self.file_create_date_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "file_name_original": file_name_original,
                "file_extension": file_extension,
                "file_create_date_time": file_create_date_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        def _parse_file_name_original(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        file_name_original = _parse_file_name_original(d.pop("file_name_original"))

        def _parse_file_extension(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        file_extension = _parse_file_extension(d.pop("file_extension"))

        def _parse_file_create_date_time(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemasfile_create_date_time_type_0 = isoparse(data)

                return componentsschemasfile_create_date_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        file_create_date_time = _parse_file_create_date_time(
            d.pop("file_create_date_time")
        )

        attachment_file_details_payload = cls(
            url=url,
            file_name_original=file_name_original,
            file_extension=file_extension,
            file_create_date_time=file_create_date_time,
        )

        attachment_file_details_payload.additional_properties = d
        return attachment_file_details_payload

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
