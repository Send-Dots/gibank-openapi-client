from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any
from typing import TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="GetBankingDaysOverviewResponse200DaysItem")


@_attrs_define
class GetBankingDaysOverviewResponse200DaysItem:
    """
    Attributes:
        date (datetime.date | Unset): The date of the banking day Example: 2024-02-04.
        is_weekend (bool | Unset): If the day is a weekend
        is_banking_day (bool | Unset): If the day is a banking day
    """

    date: datetime.date | Unset = UNSET
    is_weekend: bool | Unset = UNSET
    is_banking_day: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        is_weekend = self.is_weekend

        is_banking_day = self.is_banking_day

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if is_weekend is not UNSET:
            field_dict["is_weekend"] = is_weekend
        if is_banking_day is not UNSET:
            field_dict["is_banking_day"] = is_banking_day

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _date = d.pop("date", UNSET)
        date: datetime.date | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        is_weekend = d.pop("is_weekend", UNSET)

        is_banking_day = d.pop("is_banking_day", UNSET)

        get_banking_days_overview_response_200_days_item = cls(
            date=date,
            is_weekend=is_weekend,
            is_banking_day=is_banking_day,
        )

        get_banking_days_overview_response_200_days_item.additional_properties = d
        return get_banking_days_overview_response_200_days_item

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
