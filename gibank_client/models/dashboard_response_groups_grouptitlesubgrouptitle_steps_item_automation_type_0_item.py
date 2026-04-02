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

T = TypeVar(
    "T",
    bound="DashboardResponseGroupsGROUPTITLESUBGROUPTITLEStepsItemAutomationType0Item",
)


@_attrs_define
class DashboardResponseGroupsGROUPTITLESUBGROUPTITLEStepsItemAutomationType0Item:
    """
    Attributes:
        enabled (bool | Unset): If the next step automation is currently enabled
        date_time (datetime.datetime | None | Unset): The date and time when the automation should be triggered the next
            time (Stored as UTC, formatted as zero UTC offset (Zulu) format) Example: 2024-02-04T23:00:00.000Z.
    """

    enabled: bool | Unset = UNSET
    date_time: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        date_time: None | str | Unset
        if isinstance(self.date_time, Unset):
            date_time = UNSET
        elif isinstance(self.date_time, datetime.datetime):
            date_time = self.date_time.isoformat()
        else:
            date_time = self.date_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if date_time is not UNSET:
            field_dict["date_time"] = date_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        def _parse_date_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_time_type_0 = isoparse(data)

                return date_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_time = _parse_date_time(d.pop("date_time", UNSET))

        dashboard_response_groups_grouptitlesubgrouptitle_steps_item_automation_type_0_item = cls(
            enabled=enabled,
            date_time=date_time,
        )

        dashboard_response_groups_grouptitlesubgrouptitle_steps_item_automation_type_0_item.additional_properties = d
        return dashboard_response_groups_grouptitlesubgrouptitle_steps_item_automation_type_0_item

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
