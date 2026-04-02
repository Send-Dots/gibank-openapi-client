from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any
from typing import TypeVar
from typing import cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.state import State
from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="TaskUpdate")


@_attrs_define
class TaskUpdate:
    """
    Attributes:
        state (State | Unset): The state of the task. Can only be put to `done` when `wfcontrol_done` is `manually`
            Example: todo.
        assignee_user_id (int | None | Unset): The user ID of the assignee Example: 1.
        assignee_company_id (int | None | Unset): The company ID of the assignee (Only for clients) Example: 1.
        assignee_role_id (int | None | Unset): The role ID of the assignee (Only of type `member`) Example: 1.
        due_date_time (datetime.datetime | None | Unset): The due date and time for the task (Stored as UTC, formatted
            as zero UTC offset (Zulu) format) Example: 2024-08-20T12:00:00.000Z.
    """

    state: State | Unset = UNSET
    assignee_user_id: int | None | Unset = UNSET
    assignee_company_id: int | None | Unset = UNSET
    assignee_role_id: int | None | Unset = UNSET
    due_date_time: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        assignee_user_id: int | None | Unset
        if isinstance(self.assignee_user_id, Unset):
            assignee_user_id = UNSET
        else:
            assignee_user_id = self.assignee_user_id

        assignee_company_id: int | None | Unset
        if isinstance(self.assignee_company_id, Unset):
            assignee_company_id = UNSET
        else:
            assignee_company_id = self.assignee_company_id

        assignee_role_id: int | None | Unset
        if isinstance(self.assignee_role_id, Unset):
            assignee_role_id = UNSET
        else:
            assignee_role_id = self.assignee_role_id

        due_date_time: None | str | Unset
        if isinstance(self.due_date_time, Unset):
            due_date_time = UNSET
        elif isinstance(self.due_date_time, datetime.datetime):
            due_date_time = self.due_date_time.isoformat()
        else:
            due_date_time = self.due_date_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if assignee_user_id is not UNSET:
            field_dict["assignee_user_id"] = assignee_user_id
        if assignee_company_id is not UNSET:
            field_dict["assignee_company_id"] = assignee_company_id
        if assignee_role_id is not UNSET:
            field_dict["assignee_role_id"] = assignee_role_id
        if due_date_time is not UNSET:
            field_dict["due_date_time"] = due_date_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _state = d.pop("state", UNSET)
        state: State | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = State(_state)

        def _parse_assignee_user_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        assignee_user_id = _parse_assignee_user_id(d.pop("assignee_user_id", UNSET))

        def _parse_assignee_company_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        assignee_company_id = _parse_assignee_company_id(
            d.pop("assignee_company_id", UNSET)
        )

        def _parse_assignee_role_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        assignee_role_id = _parse_assignee_role_id(d.pop("assignee_role_id", UNSET))

        def _parse_due_date_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemasdue_date_time_type_0 = isoparse(data)

                return componentsschemasdue_date_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        due_date_time = _parse_due_date_time(d.pop("due_date_time", UNSET))

        task_update = cls(
            state=state,
            assignee_user_id=assignee_user_id,
            assignee_company_id=assignee_company_id,
            assignee_role_id=assignee_role_id,
            due_date_time=due_date_time,
        )

        task_update.additional_properties = d
        return task_update

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
