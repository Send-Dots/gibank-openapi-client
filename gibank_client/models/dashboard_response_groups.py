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
    from ..models.dashboard_response_groups_grouptitle import (
        DashboardResponseGroupsGROUPTITLE,
    )


T = TypeVar("T", bound="DashboardResponseGroups")


@_attrs_define
class DashboardResponseGroups:
    """Information about dashboard items

    Attributes:
        group_title (DashboardResponseGroupsGROUPTITLE | Unset): Information about ABC dashboard item groups (Just an
            example, there can be many)
    """

    group_title: DashboardResponseGroupsGROUPTITLE | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group_title: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group_title, Unset):
            group_title = self.group_title.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group_title is not UNSET:
            field_dict["GROUP_TITLE"] = group_title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_response_groups_grouptitle import (
            DashboardResponseGroupsGROUPTITLE,
        )

        d = dict(src_dict)
        _group_title = d.pop("GROUP_TITLE", UNSET)
        group_title: DashboardResponseGroupsGROUPTITLE | Unset
        if isinstance(_group_title, Unset):
            group_title = UNSET
        else:
            group_title = DashboardResponseGroupsGROUPTITLE.from_dict(_group_title)

        dashboard_response_groups = cls(
            group_title=group_title,
        )

        dashboard_response_groups.additional_properties = d
        return dashboard_response_groups

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
