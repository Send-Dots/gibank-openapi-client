from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING
from typing import Any
from typing import TypeVar
from typing import cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dashboard_response_groups_grouptitlesubgrouptitle_steps_item_interest import (
    DashboardResponseGroupsGROUPTITLESUBGROUPTITLEStepsItemInterest,
)
from ..types import UNSET
from ..types import Unset

if TYPE_CHECKING:
    from ..models.dashboard_response_groups_grouptitlesubgrouptitle_steps_item_automation_type_0_item import (
        DashboardResponseGroupsGROUPTITLESUBGROUPTITLEStepsItemAutomationType0Item,
    )
    from ..models.dashboard_response_groups_grouptitlesubgrouptitle_steps_item_search import (
        DashboardResponseGroupsGROUPTITLESUBGROUPTITLEStepsItemSearch,
    )


T = TypeVar("T", bound="DashboardResponseGroupsGROUPTITLESUBGROUPTITLEStepsItem")


@_attrs_define
class DashboardResponseGroupsGROUPTITLESUBGROUPTITLEStepsItem:
    """
    Attributes:
        title (str | Unset): The title of the dashboard items
        sub_title (str | Unset): The sub title of the dashboard items
        search (DashboardResponseGroupsGROUPTITLESUBGROUPTITLEStepsItemSearch | Unset): The search fields
        automation (list[DashboardResponseGroupsGROUPTITLESUBGROUPTITLEStepsItemAutomationType0Item] | None | Unset):
        interest (DashboardResponseGroupsGROUPTITLESUBGROUPTITLEStepsItemInterest | Unset): Helps deciding if the button
            should be displayed by default
    """

    title: str | Unset = UNSET
    sub_title: str | Unset = UNSET
    search: DashboardResponseGroupsGROUPTITLESUBGROUPTITLEStepsItemSearch | Unset = (
        UNSET
    )
    automation: (
        list[DashboardResponseGroupsGROUPTITLESUBGROUPTITLEStepsItemAutomationType0Item]
        | None
        | Unset
    ) = UNSET
    interest: (
        DashboardResponseGroupsGROUPTITLESUBGROUPTITLEStepsItemInterest | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        sub_title = self.sub_title

        search: dict[str, Any] | Unset = UNSET
        if not isinstance(self.search, Unset):
            search = self.search.to_dict()

        automation: list[dict[str, Any]] | None | Unset
        if isinstance(self.automation, Unset):
            automation = UNSET
        elif isinstance(self.automation, list):
            automation = []
            for automation_type_0_item_data in self.automation:
                automation_type_0_item = automation_type_0_item_data.to_dict()
                automation.append(automation_type_0_item)

        else:
            automation = self.automation

        interest: str | Unset = UNSET
        if not isinstance(self.interest, Unset):
            interest = self.interest.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if sub_title is not UNSET:
            field_dict["sub_title"] = sub_title
        if search is not UNSET:
            field_dict["search"] = search
        if automation is not UNSET:
            field_dict["automation"] = automation
        if interest is not UNSET:
            field_dict["interest"] = interest

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_response_groups_grouptitlesubgrouptitle_steps_item_automation_type_0_item import (
            DashboardResponseGroupsGROUPTITLESUBGROUPTITLEStepsItemAutomationType0Item,
        )
        from ..models.dashboard_response_groups_grouptitlesubgrouptitle_steps_item_search import (
            DashboardResponseGroupsGROUPTITLESUBGROUPTITLEStepsItemSearch,
        )

        d = dict(src_dict)
        title = d.pop("title", UNSET)

        sub_title = d.pop("sub_title", UNSET)

        _search = d.pop("search", UNSET)
        search: DashboardResponseGroupsGROUPTITLESUBGROUPTITLEStepsItemSearch | Unset
        if isinstance(_search, Unset):
            search = UNSET
        else:
            search = (
                DashboardResponseGroupsGROUPTITLESUBGROUPTITLEStepsItemSearch.from_dict(
                    _search
                )
            )

        def _parse_automation(
            data: object,
        ) -> (
            list[
                DashboardResponseGroupsGROUPTITLESUBGROUPTITLEStepsItemAutomationType0Item
            ]
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                automation_type_0 = []
                _automation_type_0 = data
                for automation_type_0_item_data in _automation_type_0:
                    automation_type_0_item = DashboardResponseGroupsGROUPTITLESUBGROUPTITLEStepsItemAutomationType0Item.from_dict(
                        automation_type_0_item_data
                    )

                    automation_type_0.append(automation_type_0_item)

                return automation_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[
                    DashboardResponseGroupsGROUPTITLESUBGROUPTITLEStepsItemAutomationType0Item
                ]
                | None
                | Unset,
                data,
            )

        automation = _parse_automation(d.pop("automation", UNSET))

        _interest = d.pop("interest", UNSET)
        interest: (
            DashboardResponseGroupsGROUPTITLESUBGROUPTITLEStepsItemInterest | Unset
        )
        if isinstance(_interest, Unset):
            interest = UNSET
        else:
            interest = DashboardResponseGroupsGROUPTITLESUBGROUPTITLEStepsItemInterest(
                _interest
            )

        dashboard_response_groups_grouptitlesubgrouptitle_steps_item = cls(
            title=title,
            sub_title=sub_title,
            search=search,
            automation=automation,
            interest=interest,
        )

        dashboard_response_groups_grouptitlesubgrouptitle_steps_item.additional_properties = d
        return dashboard_response_groups_grouptitlesubgrouptitle_steps_item

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
