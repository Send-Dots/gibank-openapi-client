from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING
from typing import Any
from typing import TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET
from ..types import Unset

if TYPE_CHECKING:
    from ..models.get_banking_days_overview_response_200_days_item import (
        GetBankingDaysOverviewResponse200DaysItem,
    )


T = TypeVar("T", bound="GetBankingDaysOverviewResponse200")


@_attrs_define
class GetBankingDaysOverviewResponse200:
    """
    Attributes:
        from_date (datetime.date | Unset): The date of the banking days overview Example: 2024-02-04.
        to_date (datetime.date | Unset): The date of the banking days overview Example: 2024-02-04.
        days (list[GetBankingDaysOverviewResponse200DaysItem] | Unset):
    """

    from_date: datetime.date | Unset = UNSET
    to_date: datetime.date | Unset = UNSET
    days: list[GetBankingDaysOverviewResponse200DaysItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_date: str | Unset = UNSET
        if not isinstance(self.from_date, Unset):
            from_date = self.from_date.isoformat()

        to_date: str | Unset = UNSET
        if not isinstance(self.to_date, Unset):
            to_date = self.to_date.isoformat()

        days: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.days, Unset):
            days = []
            for days_item_data in self.days:
                days_item = days_item_data.to_dict()
                days.append(days_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_date is not UNSET:
            field_dict["from_date"] = from_date
        if to_date is not UNSET:
            field_dict["to_date"] = to_date
        if days is not UNSET:
            field_dict["days"] = days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_banking_days_overview_response_200_days_item import (
            GetBankingDaysOverviewResponse200DaysItem,
        )

        d = dict(src_dict)
        _from_date = d.pop("from_date", UNSET)
        from_date: datetime.date | Unset
        if isinstance(_from_date, Unset):
            from_date = UNSET
        else:
            from_date = isoparse(_from_date).date()

        _to_date = d.pop("to_date", UNSET)
        to_date: datetime.date | Unset
        if isinstance(_to_date, Unset):
            to_date = UNSET
        else:
            to_date = isoparse(_to_date).date()

        _days = d.pop("days", UNSET)
        days: list[GetBankingDaysOverviewResponse200DaysItem] | Unset = UNSET
        if _days is not UNSET:
            days = []
            for days_item_data in _days:
                days_item = GetBankingDaysOverviewResponse200DaysItem.from_dict(
                    days_item_data
                )

                days.append(days_item)

        get_banking_days_overview_response_200 = cls(
            from_date=from_date,
            to_date=to_date,
            days=days,
        )

        get_banking_days_overview_response_200.additional_properties = d
        return get_banking_days_overview_response_200

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
