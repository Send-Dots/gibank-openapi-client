from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any
from typing import TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.role_fields_type import RoleFieldsType
from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="RoleFields")


@_attrs_define
class RoleFields:
    """
    Attributes:
        id (int | Unset): The RBAC role ID Example: 1.
        key (str | Unset): The key of the RBAC role Example: client.
        name (str | Unset): The name of the RBAC role Example: Client.
        description (str | Unset): The description of the RBAC role Example: Client role with access to their own data.
        type_ (RoleFieldsType | Unset): The type of the RBAC role Example: member.
        active (bool | Unset): Indicates if the RBAC role is active Default: True. Example: True.
        create_date_time (datetime.datetime | Unset): The date and time when the RBAC role was created (Stored as UTC,
            formatted as zero UTC offset (Zulu) format) Example: 2024-02-04T23:00:00.000Z.
        update_date_time (datetime.datetime | Unset): The date and time when the RBAC role was last updated (Stored as
            UTC, formatted as zero UTC offset (Zulu) format) Example: 2024-02-04T23:00:00.000Z.
    """

    id: int | Unset = UNSET
    key: str | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    type_: RoleFieldsType | Unset = UNSET
    active: bool | Unset = True
    create_date_time: datetime.datetime | Unset = UNSET
    update_date_time: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        key = self.key

        name = self.name

        description = self.description

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        active = self.active

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
        if key is not UNSET:
            field_dict["key"] = key
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if type_ is not UNSET:
            field_dict["type"] = type_
        if active is not UNSET:
            field_dict["active"] = active
        if create_date_time is not UNSET:
            field_dict["create_date_time"] = create_date_time
        if update_date_time is not UNSET:
            field_dict["update_date_time"] = update_date_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        key = d.pop("key", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: RoleFieldsType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RoleFieldsType(_type_)

        active = d.pop("active", UNSET)

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

        role_fields = cls(
            id=id,
            key=key,
            name=name,
            description=description,
            type_=type_,
            active=active,
            create_date_time=create_date_time,
            update_date_time=update_date_time,
        )

        role_fields.additional_properties = d
        return role_fields

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
