from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any
from typing import TypeVar
from typing import cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.subclient_account_response_type import SubclientAccountResponseType
from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="SubclientAccountResponse")


@_attrs_define
class SubclientAccountResponse:
    """
    Attributes:
        id (float | Unset): The subclient account ID Example: 1.
        subclient_id (float | Unset): The subclient ID Example: 1.
        routing_number (str | Unset): The routing number of the subclient account Example: 091001322.
        account_number (str | Unset): The account number of the subclient account Example: 1234.
        description (None | str | Unset): The description of the subclient account Example: Test Account.
        active (bool | Unset): Indicates if the subclient account is active Default: True. Example: True.
        core_account_number (None | str | Unset): The core account number associated to the virtual account Example:
            1234.
        create_date_time (datetime.datetime | Unset): The date and time when the subclient account was created (Stored
            as UTC, formatted as zero UTC offset (Zulu) format) Example: 2024-02-04T23:00:00.000Z.
        update_date_time (datetime.datetime | Unset): The date and time when the subclient account was last updated
            (Stored as UTC, formatted as zero UTC offset (Zulu) format) Example: 2024-02-04T23:00:00.000Z.
        create_user_id (float | Unset): The ID of the user who created the subclient account Example: 1.
        update_user_id (float | Unset): The ID of the user who last updated the subclient account Example: 1.
        type_ (SubclientAccountResponseType | Unset): The type of the subclient account Example: virtual.
    """

    id: float | Unset = UNSET
    subclient_id: float | Unset = UNSET
    routing_number: str | Unset = UNSET
    account_number: str | Unset = UNSET
    description: None | str | Unset = UNSET
    active: bool | Unset = True
    core_account_number: None | str | Unset = UNSET
    create_date_time: datetime.datetime | Unset = UNSET
    update_date_time: datetime.datetime | Unset = UNSET
    create_user_id: float | Unset = UNSET
    update_user_id: float | Unset = UNSET
    type_: SubclientAccountResponseType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        subclient_id = self.subclient_id

        routing_number = self.routing_number

        account_number = self.account_number

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        active = self.active

        core_account_number: None | str | Unset
        if isinstance(self.core_account_number, Unset):
            core_account_number = UNSET
        else:
            core_account_number = self.core_account_number

        create_date_time: str | Unset = UNSET
        if not isinstance(self.create_date_time, Unset):
            create_date_time = self.create_date_time.isoformat()

        update_date_time: str | Unset = UNSET
        if not isinstance(self.update_date_time, Unset):
            update_date_time = self.update_date_time.isoformat()

        create_user_id = self.create_user_id

        update_user_id = self.update_user_id

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if subclient_id is not UNSET:
            field_dict["subclient_id"] = subclient_id
        if routing_number is not UNSET:
            field_dict["routing_number"] = routing_number
        if account_number is not UNSET:
            field_dict["account_number"] = account_number
        if description is not UNSET:
            field_dict["description"] = description
        if active is not UNSET:
            field_dict["active"] = active
        if core_account_number is not UNSET:
            field_dict["core_account_number"] = core_account_number
        if create_date_time is not UNSET:
            field_dict["create_date_time"] = create_date_time
        if update_date_time is not UNSET:
            field_dict["update_date_time"] = update_date_time
        if create_user_id is not UNSET:
            field_dict["create_user_id"] = create_user_id
        if update_user_id is not UNSET:
            field_dict["update_user_id"] = update_user_id
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        subclient_id = d.pop("subclient_id", UNSET)

        routing_number = d.pop("routing_number", UNSET)

        account_number = d.pop("account_number", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        active = d.pop("active", UNSET)

        def _parse_core_account_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        core_account_number = _parse_core_account_number(
            d.pop("core_account_number", UNSET)
        )

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

        _type_ = d.pop("type", UNSET)
        type_: SubclientAccountResponseType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = SubclientAccountResponseType(_type_)

        subclient_account_response = cls(
            id=id,
            subclient_id=subclient_id,
            routing_number=routing_number,
            account_number=account_number,
            description=description,
            active=active,
            core_account_number=core_account_number,
            create_date_time=create_date_time,
            update_date_time=update_date_time,
            create_user_id=create_user_id,
            update_user_id=update_user_id,
            type_=type_,
        )

        subclient_account_response.additional_properties = d
        return subclient_account_response

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
