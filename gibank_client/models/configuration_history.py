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
    from ..models.configuration_history_data import ConfigurationHistoryData


T = TypeVar("T", bound="ConfigurationHistory")


@_attrs_define
class ConfigurationHistory:
    """
    Attributes:
        id (float | Unset): The configuration history ID Example: 1.
        entity_name (str | Unset): The name of the entity Example: batch.
        entity_pk (str | Unset): The primary key/identifier of the entity Example: 1.
        data (ConfigurationHistoryData | Unset): The data of the configuration that was stored
        create_date_time (datetime.datetime | Unset): The date and time when the configuration history was created
            (Stored as UTC, formatted as zero UTC offset (Zulu) format) Example: 2024-02-04T23:00:00.000Z.
        create_user_id (int | Unset): The ID of the user who created the comment Example: 1.
        create_user_full_name (str | Unset): The full name of the user who created the configuration history Example:
            Max Mustermann.
    """

    id: float | Unset = UNSET
    entity_name: str | Unset = UNSET
    entity_pk: str | Unset = UNSET
    data: ConfigurationHistoryData | Unset = UNSET
    create_date_time: datetime.datetime | Unset = UNSET
    create_user_id: int | Unset = UNSET
    create_user_full_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        entity_name = self.entity_name

        entity_pk = self.entity_pk

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        create_date_time: str | Unset = UNSET
        if not isinstance(self.create_date_time, Unset):
            create_date_time = self.create_date_time.isoformat()

        create_user_id = self.create_user_id

        create_user_full_name = self.create_user_full_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if entity_name is not UNSET:
            field_dict["entity_name"] = entity_name
        if entity_pk is not UNSET:
            field_dict["entity_pk"] = entity_pk
        if data is not UNSET:
            field_dict["data"] = data
        if create_date_time is not UNSET:
            field_dict["create_date_time"] = create_date_time
        if create_user_id is not UNSET:
            field_dict["create_user_id"] = create_user_id
        if create_user_full_name is not UNSET:
            field_dict["create_user_full_name"] = create_user_full_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.configuration_history_data import ConfigurationHistoryData

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        entity_name = d.pop("entity_name", UNSET)

        entity_pk = d.pop("entity_pk", UNSET)

        _data = d.pop("data", UNSET)
        data: ConfigurationHistoryData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = ConfigurationHistoryData.from_dict(_data)

        _create_date_time = d.pop("create_date_time", UNSET)
        create_date_time: datetime.datetime | Unset
        if isinstance(_create_date_time, Unset):
            create_date_time = UNSET
        else:
            create_date_time = isoparse(_create_date_time)

        create_user_id = d.pop("create_user_id", UNSET)

        create_user_full_name = d.pop("create_user_full_name", UNSET)

        configuration_history = cls(
            id=id,
            entity_name=entity_name,
            entity_pk=entity_pk,
            data=data,
            create_date_time=create_date_time,
            create_user_id=create_user_id,
            create_user_full_name=create_user_full_name,
        )

        configuration_history.additional_properties = d
        return configuration_history

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
