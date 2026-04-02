from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any
from typing import TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.account_balance_fields_type import AccountBalanceFieldsType
from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="AccountBalanceFields")


@_attrs_define
class AccountBalanceFields:
    """
    Attributes:
        account_number (str | Unset): The account number of the account Example: 1234.
        type_ (AccountBalanceFieldsType | Unset): The type of the subclient account Example: core.
        pending_balance_credit (float | Unset): The total amount of processed credits that have not yet posted. Example:
            1234.
        pending_balance_debit (float | Unset): The total amount of processed debits that have not yet posted. Example:
            1234.
        available_balance_credit (float | Unset): The total amount of processed credits that have been posted. Example:
            1234.
        available_balance_debit (float | Unset): The total amount of processed debits that have been posted. Example:
            1234.
        create_date_time (datetime.datetime | Unset): The date and time when the balance cache was first set for this
            account (Stored as UTC, formatted as zero UTC offset (Zulu) format) Example: 2024-02-04T23:00:00.000Z.
        update_date_time (datetime.datetime | Unset): The date and time when the balance cache was last updated for this
            account (Stored as UTC, formatted as zero UTC offset (Zulu) format) Example: 2024-02-04T23:00:00.000Z.
    """

    account_number: str | Unset = UNSET
    type_: AccountBalanceFieldsType | Unset = UNSET
    pending_balance_credit: float | Unset = UNSET
    pending_balance_debit: float | Unset = UNSET
    available_balance_credit: float | Unset = UNSET
    available_balance_debit: float | Unset = UNSET
    create_date_time: datetime.datetime | Unset = UNSET
    update_date_time: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_number = self.account_number

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        pending_balance_credit = self.pending_balance_credit

        pending_balance_debit = self.pending_balance_debit

        available_balance_credit = self.available_balance_credit

        available_balance_debit = self.available_balance_debit

        create_date_time: str | Unset = UNSET
        if not isinstance(self.create_date_time, Unset):
            create_date_time = self.create_date_time.isoformat()

        update_date_time: str | Unset = UNSET
        if not isinstance(self.update_date_time, Unset):
            update_date_time = self.update_date_time.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_number is not UNSET:
            field_dict["account_number"] = account_number
        if type_ is not UNSET:
            field_dict["type"] = type_
        if pending_balance_credit is not UNSET:
            field_dict["pending_balance_credit"] = pending_balance_credit
        if pending_balance_debit is not UNSET:
            field_dict["pending_balance_debit"] = pending_balance_debit
        if available_balance_credit is not UNSET:
            field_dict["available_balance_credit"] = available_balance_credit
        if available_balance_debit is not UNSET:
            field_dict["available_balance_debit"] = available_balance_debit
        if create_date_time is not UNSET:
            field_dict["create_date_time"] = create_date_time
        if update_date_time is not UNSET:
            field_dict["update_date_time"] = update_date_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_number = d.pop("account_number", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: AccountBalanceFieldsType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AccountBalanceFieldsType(_type_)

        pending_balance_credit = d.pop("pending_balance_credit", UNSET)

        pending_balance_debit = d.pop("pending_balance_debit", UNSET)

        available_balance_credit = d.pop("available_balance_credit", UNSET)

        available_balance_debit = d.pop("available_balance_debit", UNSET)

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

        account_balance_fields = cls(
            account_number=account_number,
            type_=type_,
            pending_balance_credit=pending_balance_credit,
            pending_balance_debit=pending_balance_debit,
            available_balance_credit=available_balance_credit,
            available_balance_debit=available_balance_debit,
            create_date_time=create_date_time,
            update_date_time=update_date_time,
        )

        account_balance_fields.additional_properties = d
        return account_balance_fields

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
