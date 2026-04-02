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
    from ..models.dashboard_response_groups import DashboardResponseGroups


T = TypeVar("T", bound="DashboardResponse")


@_attrs_define
class DashboardResponse:
    """
    Attributes:
        groups (DashboardResponseGroups | Unset): Information about dashboard items
    """

    groups: DashboardResponseGroups | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        groups: dict[str, Any] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if groups is not UNSET:
            field_dict["groups"] = groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_response_groups import DashboardResponseGroups

        d = dict(src_dict)
        _groups = d.pop("groups", UNSET)
        groups: DashboardResponseGroups | Unset
        if isinstance(_groups, Unset):
            groups = UNSET
        else:
            groups = DashboardResponseGroups.from_dict(_groups)

        dashboard_response = cls(
            groups=groups,
        )

        dashboard_response.additional_properties = d
        return dashboard_response

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
