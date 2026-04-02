from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING
from typing import Any
from typing import TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET
from ..types import Unset

if TYPE_CHECKING:
    from ..models.dashboard_response_groups_grouptitlesubgrouptitle_steps_item import (
        DashboardResponseGroupsGROUPTITLESUBGROUPTITLEStepsItem,
    )


T = TypeVar("T", bound="DashboardResponseGroupsGROUPTITLESUBGROUPTITLE")


@_attrs_define
class DashboardResponseGroupsGROUPTITLESUBGROUPTITLE:
    """Information about ABC dashboard items (Just an example, there can be many)

    Attributes:
        steps (list[DashboardResponseGroupsGROUPTITLESUBGROUPTITLEStepsItem] | Unset): The list of dashboard items to
            display
    """

    steps: list[DashboardResponseGroupsGROUPTITLESUBGROUPTITLEStepsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        steps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.steps, Unset):
            steps = []
            for steps_item_data in self.steps:
                steps_item = steps_item_data.to_dict()
                steps.append(steps_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if steps is not UNSET:
            field_dict["steps"] = steps

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_response_groups_grouptitlesubgrouptitle_steps_item import (
            DashboardResponseGroupsGROUPTITLESUBGROUPTITLEStepsItem,
        )

        d = dict(src_dict)
        _steps = d.pop("steps", UNSET)
        steps: list[DashboardResponseGroupsGROUPTITLESUBGROUPTITLEStepsItem] | Unset = (
            UNSET
        )
        if _steps is not UNSET:
            steps = []
            for steps_item_data in _steps:
                steps_item = (
                    DashboardResponseGroupsGROUPTITLESUBGROUPTITLEStepsItem.from_dict(
                        steps_item_data
                    )
                )

                steps.append(steps_item)

        dashboard_response_groups_grouptitlesubgrouptitle = cls(
            steps=steps,
        )

        dashboard_response_groups_grouptitlesubgrouptitle.additional_properties = d
        return dashboard_response_groups_grouptitlesubgrouptitle

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
