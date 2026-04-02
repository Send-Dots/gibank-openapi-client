from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING
from typing import Any
from typing import TypeVar
from typing import cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.properties_type import PropertiesType
from ..models.state import State
from ..models.wfcontrol_done import WfcontrolDone
from ..types import UNSET
from ..types import Unset

if TYPE_CHECKING:
    from ..models.search_json_type_0 import SearchJsonType0


T = TypeVar("T", bound="TaskCreate")


@_attrs_define
class TaskCreate:
    """
    Attributes:
        title (str): The title of the task Example: Review subclient application.
        type_ (PropertiesType): The type of the task Example: subclient_pending.
        wfcontrol_done (WfcontrolDone): Controls how the task is marked as done Example: manually.
        state (State): The state of the task. Can only be put to `done` when `wfcontrol_done` is `manually` Example:
            todo.
        assignee_user_id (int | None | Unset): The user ID of the assignee Example: 1.
        assignee_company_id (int | None | Unset): The company ID of the assignee (Only for clients) Example: 1.
        assignee_role_id (int | None | Unset): The role ID of the assignee (Only of type `member`) Example: 1.
        entity_name (None | str | Unset): The name of the related entity Example: subclient.
        entity_pk (None | str | Unset): The primary key of the related entity Example: 123.
        search_json (None | SearchJsonType0 | Unset): A JSON object for search purposes Example: {'key': 'value'}.
        due_date_time (datetime.datetime | None | Unset): The due date and time for the task (Stored as UTC, formatted
            as zero UTC offset (Zulu) format) Example: 2024-08-20T12:00:00.000Z.
    """

    title: str
    type_: PropertiesType
    wfcontrol_done: WfcontrolDone
    state: State
    assignee_user_id: int | None | Unset = UNSET
    assignee_company_id: int | None | Unset = UNSET
    assignee_role_id: int | None | Unset = UNSET
    entity_name: None | str | Unset = UNSET
    entity_pk: None | str | Unset = UNSET
    search_json: None | SearchJsonType0 | Unset = UNSET
    due_date_time: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.search_json_type_0 import SearchJsonType0

        title = self.title

        type_ = self.type_.value

        wfcontrol_done = self.wfcontrol_done.value

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

        entity_name: None | str | Unset
        if isinstance(self.entity_name, Unset):
            entity_name = UNSET
        else:
            entity_name = self.entity_name

        entity_pk: None | str | Unset
        if isinstance(self.entity_pk, Unset):
            entity_pk = UNSET
        else:
            entity_pk = self.entity_pk

        search_json: dict[str, Any] | None | Unset
        if isinstance(self.search_json, Unset):
            search_json = UNSET
        elif isinstance(self.search_json, SearchJsonType0):
            search_json = self.search_json.to_dict()
        else:
            search_json = self.search_json

        due_date_time: None | str | Unset
        if isinstance(self.due_date_time, Unset):
            due_date_time = UNSET
        elif isinstance(self.due_date_time, datetime.datetime):
            due_date_time = self.due_date_time.isoformat()
        else:
            due_date_time = self.due_date_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "type": type_,
                "wfcontrol_done": wfcontrol_done,
                "state": state,
            }
        )
        if assignee_user_id is not UNSET:
            field_dict["assignee_user_id"] = assignee_user_id
        if assignee_company_id is not UNSET:
            field_dict["assignee_company_id"] = assignee_company_id
        if assignee_role_id is not UNSET:
            field_dict["assignee_role_id"] = assignee_role_id
        if entity_name is not UNSET:
            field_dict["entity_name"] = entity_name
        if entity_pk is not UNSET:
            field_dict["entity_pk"] = entity_pk
        if search_json is not UNSET:
            field_dict["search_json"] = search_json
        if due_date_time is not UNSET:
            field_dict["due_date_time"] = due_date_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_json_type_0 import SearchJsonType0

        d = dict(src_dict)
        title = d.pop("title")

        type_ = PropertiesType(d.pop("type"))

        wfcontrol_done = WfcontrolDone(d.pop("wfcontrol_done"))

        state = State(d.pop("state"))

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

        def _parse_entity_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        entity_name = _parse_entity_name(d.pop("entity_name", UNSET))

        def _parse_entity_pk(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        entity_pk = _parse_entity_pk(d.pop("entity_pk", UNSET))

        def _parse_search_json(data: object) -> None | SearchJsonType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemassearch_json_type_0 = SearchJsonType0.from_dict(data)

                return componentsschemassearch_json_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SearchJsonType0 | Unset, data)

        search_json = _parse_search_json(d.pop("search_json", UNSET))

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

        task_create = cls(
            title=title,
            type_=type_,
            wfcontrol_done=wfcontrol_done,
            state=state,
            assignee_user_id=assignee_user_id,
            assignee_company_id=assignee_company_id,
            assignee_role_id=assignee_role_id,
            entity_name=entity_name,
            entity_pk=entity_pk,
            search_json=search_json,
            due_date_time=due_date_time,
        )

        task_create.additional_properties = d
        return task_create

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
