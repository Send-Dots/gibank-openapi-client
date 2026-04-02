from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any
from typing import TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.comment_fields_create_user_type import CommentFieldsCreateUserType
from ..models.comment_fields_update_user_type import CommentFieldsUpdateUserType
from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="CommentFields")


@_attrs_define
class CommentFields:
    """
    Attributes:
        id (int | Unset): The comment ID Example: 1.
        comment (str | Unset): The comment text Example: Test Comment.
        create_user_full_name (str | Unset): The full name of the create user Example: Max Mustermann.
        create_user_type (CommentFieldsCreateUserType | Unset): The type of the create user Example: client.
        update_user_full_name (str | Unset): The full name of the update user Example: Max Mustermann.
        update_user_type (CommentFieldsUpdateUserType | Unset): The type of the update user Example: client.
        create_date_time (datetime.datetime | Unset): The date and time when the comment was created (Stored as UTC,
            formatted as zero UTC offset (Zulu) format) Example: 2024-02-04T23:00:00.000Z.
        update_date_time (datetime.datetime | Unset): The date and time when the comment was last updated (Stored as
            UTC, formatted as zero UTC offset (Zulu) format) Example: 2024-02-04T23:00:00.000Z.
        create_user_id (int | Unset): The ID of the user who created the comment Example: 1.
        update_user_id (int | Unset): The ID of the user who last updated the comment Example: 1.
    """

    id: int | Unset = UNSET
    comment: str | Unset = UNSET
    create_user_full_name: str | Unset = UNSET
    create_user_type: CommentFieldsCreateUserType | Unset = UNSET
    update_user_full_name: str | Unset = UNSET
    update_user_type: CommentFieldsUpdateUserType | Unset = UNSET
    create_date_time: datetime.datetime | Unset = UNSET
    update_date_time: datetime.datetime | Unset = UNSET
    create_user_id: int | Unset = UNSET
    update_user_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        comment = self.comment

        create_user_full_name = self.create_user_full_name

        create_user_type: str | Unset = UNSET
        if not isinstance(self.create_user_type, Unset):
            create_user_type = self.create_user_type.value

        update_user_full_name = self.update_user_full_name

        update_user_type: str | Unset = UNSET
        if not isinstance(self.update_user_type, Unset):
            update_user_type = self.update_user_type.value

        create_date_time: str | Unset = UNSET
        if not isinstance(self.create_date_time, Unset):
            create_date_time = self.create_date_time.isoformat()

        update_date_time: str | Unset = UNSET
        if not isinstance(self.update_date_time, Unset):
            update_date_time = self.update_date_time.isoformat()

        create_user_id = self.create_user_id

        update_user_id = self.update_user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if comment is not UNSET:
            field_dict["comment"] = comment
        if create_user_full_name is not UNSET:
            field_dict["create_user_full_name"] = create_user_full_name
        if create_user_type is not UNSET:
            field_dict["create_user_type"] = create_user_type
        if update_user_full_name is not UNSET:
            field_dict["update_user_full_name"] = update_user_full_name
        if update_user_type is not UNSET:
            field_dict["update_user_type"] = update_user_type
        if create_date_time is not UNSET:
            field_dict["create_date_time"] = create_date_time
        if update_date_time is not UNSET:
            field_dict["update_date_time"] = update_date_time
        if create_user_id is not UNSET:
            field_dict["create_user_id"] = create_user_id
        if update_user_id is not UNSET:
            field_dict["update_user_id"] = update_user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        comment = d.pop("comment", UNSET)

        create_user_full_name = d.pop("create_user_full_name", UNSET)

        _create_user_type = d.pop("create_user_type", UNSET)
        create_user_type: CommentFieldsCreateUserType | Unset
        if isinstance(_create_user_type, Unset):
            create_user_type = UNSET
        else:
            create_user_type = CommentFieldsCreateUserType(_create_user_type)

        update_user_full_name = d.pop("update_user_full_name", UNSET)

        _update_user_type = d.pop("update_user_type", UNSET)
        update_user_type: CommentFieldsUpdateUserType | Unset
        if isinstance(_update_user_type, Unset):
            update_user_type = UNSET
        else:
            update_user_type = CommentFieldsUpdateUserType(_update_user_type)

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

        create_user_id = d.pop("create_user_id", UNSET)

        update_user_id = d.pop("update_user_id", UNSET)

        comment_fields = cls(
            id=id,
            comment=comment,
            create_user_full_name=create_user_full_name,
            create_user_type=create_user_type,
            update_user_full_name=update_user_full_name,
            update_user_type=update_user_type,
            create_date_time=create_date_time,
            update_date_time=update_date_time,
            create_user_id=create_user_id,
            update_user_id=update_user_id,
        )

        comment_fields.additional_properties = d
        return comment_fields

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
