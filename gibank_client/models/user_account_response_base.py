from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any
from typing import TypeVar
from typing import cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="UserAccountResponseBase")


@_attrs_define
class UserAccountResponseBase:
    """
    Attributes:
        id (float | Unset): The user account ID Example: 1.
        user_id (float | Unset): The user ID Example: 1.
        active (bool | Unset): Indicates if the user account is active Example: True.
        account_number (str | Unset): The account number of the user account Example: 1234.
        description (None | str | Unset): The description of the user account Example: Test Account.
        virtual_count (float | Unset): The count of virtual accounts associated with this account Example: 100.
        create_date_time (datetime.datetime | Unset): The date and time when the user account was created (Stored as
            UTC, formatted as zero UTC offset (Zulu) format) Example: 2024-02-04T23:00:00.000Z.
        update_date_time (datetime.datetime | Unset): The date and time when the user account was last updated (Stored
            as UTC, formatted as zero UTC offset (Zulu) format) Example: 2024-02-04T23:00:00.000Z.
    """

    id: float | Unset = UNSET
    user_id: float | Unset = UNSET
    active: bool | Unset = UNSET
    account_number: str | Unset = UNSET
    description: None | str | Unset = UNSET
    virtual_count: float | Unset = UNSET
    create_date_time: datetime.datetime | Unset = UNSET
    update_date_time: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user_id = self.user_id

        active = self.active

        account_number = self.account_number

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        virtual_count = self.virtual_count

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
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if active is not UNSET:
            field_dict["active"] = active
        if account_number is not UNSET:
            field_dict["account_number"] = account_number
        if description is not UNSET:
            field_dict["description"] = description
        if virtual_count is not UNSET:
            field_dict["virtual_count"] = virtual_count
        if create_date_time is not UNSET:
            field_dict["create_date_time"] = create_date_time
        if update_date_time is not UNSET:
            field_dict["update_date_time"] = update_date_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        user_id = d.pop("user_id", UNSET)

        active = d.pop("active", UNSET)

        account_number = d.pop("account_number", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        virtual_count = d.pop("virtual_count", UNSET)

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

        user_account_response_base = cls(
            id=id,
            user_id=user_id,
            active=active,
            account_number=account_number,
            description=description,
            virtual_count=virtual_count,
            create_date_time=create_date_time,
            update_date_time=update_date_time,
        )

        user_account_response_base.additional_properties = d
        return user_account_response_base

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
