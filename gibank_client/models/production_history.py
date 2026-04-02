from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any
from typing import TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.production_history_action import ProductionHistoryAction
from ..models.production_history_level import ProductionHistoryLevel
from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="ProductionHistory")


@_attrs_define
class ProductionHistory:
    """
    Attributes:
        action (ProductionHistoryAction | Unset): The action that has been done Example: create.
        create_user_id (int | Unset): The ID of the user who created the comment Example: 1.
        create_date_time (datetime.datetime | Unset): The date and time when the history was created (Stored as UTC,
            formatted as zero UTC offset (Zulu) format) Example: 2024-02-04T23:00:00.000Z.
        create_user_full_name (str | Unset): The full name of the user who created the history Example: Max Mustermann.
        level (ProductionHistoryLevel | Unset): The log level of the history Example: info.
        data (str | Unset): The additional data related to the history Example: User source: accounts.
    """

    action: ProductionHistoryAction | Unset = UNSET
    create_user_id: int | Unset = UNSET
    create_date_time: datetime.datetime | Unset = UNSET
    create_user_full_name: str | Unset = UNSET
    level: ProductionHistoryLevel | Unset = UNSET
    data: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action: str | Unset = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.value

        create_user_id = self.create_user_id

        create_date_time: str | Unset = UNSET
        if not isinstance(self.create_date_time, Unset):
            create_date_time = self.create_date_time.isoformat()

        create_user_full_name = self.create_user_full_name

        level: str | Unset = UNSET
        if not isinstance(self.level, Unset):
            level = self.level.value

        data = self.data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action
        if create_user_id is not UNSET:
            field_dict["create_user_id"] = create_user_id
        if create_date_time is not UNSET:
            field_dict["create_date_time"] = create_date_time
        if create_user_full_name is not UNSET:
            field_dict["create_user_full_name"] = create_user_full_name
        if level is not UNSET:
            field_dict["level"] = level
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _action = d.pop("action", UNSET)
        action: ProductionHistoryAction | Unset
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = ProductionHistoryAction(_action)

        create_user_id = d.pop("create_user_id", UNSET)

        _create_date_time = d.pop("create_date_time", UNSET)
        create_date_time: datetime.datetime | Unset
        if isinstance(_create_date_time, Unset):
            create_date_time = UNSET
        else:
            create_date_time = isoparse(_create_date_time)

        create_user_full_name = d.pop("create_user_full_name", UNSET)

        _level = d.pop("level", UNSET)
        level: ProductionHistoryLevel | Unset
        if isinstance(_level, Unset):
            level = UNSET
        else:
            level = ProductionHistoryLevel(_level)

        data = d.pop("data", UNSET)

        production_history = cls(
            action=action,
            create_user_id=create_user_id,
            create_date_time=create_date_time,
            create_user_full_name=create_user_full_name,
            level=level,
            data=data,
        )

        production_history.additional_properties = d
        return production_history

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
