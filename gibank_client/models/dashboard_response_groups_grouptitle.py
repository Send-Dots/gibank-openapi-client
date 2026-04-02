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
    from ..models.dashboard_response_groups_grouptitlesubgrouptitle import (
        DashboardResponseGroupsGROUPTITLESUBGROUPTITLE,
    )


T = TypeVar("T", bound="DashboardResponseGroupsGROUPTITLE")


@_attrs_define
class DashboardResponseGroupsGROUPTITLE:
    """Information about ABC dashboard item groups (Just an example, there can be many)

    Attributes:
        subgroup_title (DashboardResponseGroupsGROUPTITLESUBGROUPTITLE | Unset): Information about ABC dashboard items
            (Just an example, there can be many)
    """

    subgroup_title: DashboardResponseGroupsGROUPTITLESUBGROUPTITLE | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subgroup_title: dict[str, Any] | Unset = UNSET
        if not isinstance(self.subgroup_title, Unset):
            subgroup_title = self.subgroup_title.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if subgroup_title is not UNSET:
            field_dict["SUBGROUP_TITLE"] = subgroup_title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_response_groups_grouptitlesubgrouptitle import (
            DashboardResponseGroupsGROUPTITLESUBGROUPTITLE,
        )

        d = dict(src_dict)
        _subgroup_title = d.pop("SUBGROUP_TITLE", UNSET)
        subgroup_title: DashboardResponseGroupsGROUPTITLESUBGROUPTITLE | Unset
        if isinstance(_subgroup_title, Unset):
            subgroup_title = UNSET
        else:
            subgroup_title = DashboardResponseGroupsGROUPTITLESUBGROUPTITLE.from_dict(
                _subgroup_title
            )

        dashboard_response_groups_grouptitle = cls(
            subgroup_title=subgroup_title,
        )

        dashboard_response_groups_grouptitle.additional_properties = d
        return dashboard_response_groups_grouptitle

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
