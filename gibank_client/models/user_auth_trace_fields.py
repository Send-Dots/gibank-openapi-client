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

T = TypeVar("T", bound="UserAuthTraceFields")


@_attrs_define
class UserAuthTraceFields:
    """
    Attributes:
        id (int | Unset): The auth trace ID Example: 1.
        user_id (int | Unset): The user ID Example: 1.
        user_apikey_id (int | None | Unset): The API Key ID, if authentication was performed via an API key (null for
            Cognito auth) Example: 3.
        success (bool | Unset): Whether the authentication attempt was successful Example: True.
        failure_reason (None | str | Unset): The reason for the authentication failure, if applicable Example: API Key
            expired (User API Key ID: 3).
        source_ip (None | str | Unset): The source IP address of the request Example: 203.0.113.42.
        user_agent (None | str | Unset): The User-Agent header of the request Example: Mozilla/5.0 (Macintosh; Intel Mac
            OS X 10_15_7).
        http_method (None | str | Unset): The HTTP method of the request being authorized Example: POST.
        resource_path (None | str | Unset): The API resource path being authorized Example: /transactions.
        create_date_time (datetime.datetime | Unset): The date and time of the authentication attempt (Stored as UTC,
            formatted as zero UTC offset (Zulu) format) Example: 2024-02-04T23:00:00.000Z.
        user_full_name (None | str | Unset): The full name of the user who performed the authentication attempt Example:
            John Doe.
        company_name (None | str | Unset): The company name of the user Example: Acme Corp.
    """

    id: int | Unset = UNSET
    user_id: int | Unset = UNSET
    user_apikey_id: int | None | Unset = UNSET
    success: bool | Unset = UNSET
    failure_reason: None | str | Unset = UNSET
    source_ip: None | str | Unset = UNSET
    user_agent: None | str | Unset = UNSET
    http_method: None | str | Unset = UNSET
    resource_path: None | str | Unset = UNSET
    create_date_time: datetime.datetime | Unset = UNSET
    user_full_name: None | str | Unset = UNSET
    company_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user_id = self.user_id

        user_apikey_id: int | None | Unset
        if isinstance(self.user_apikey_id, Unset):
            user_apikey_id = UNSET
        else:
            user_apikey_id = self.user_apikey_id

        success = self.success

        failure_reason: None | str | Unset
        if isinstance(self.failure_reason, Unset):
            failure_reason = UNSET
        else:
            failure_reason = self.failure_reason

        source_ip: None | str | Unset
        if isinstance(self.source_ip, Unset):
            source_ip = UNSET
        else:
            source_ip = self.source_ip

        user_agent: None | str | Unset
        if isinstance(self.user_agent, Unset):
            user_agent = UNSET
        else:
            user_agent = self.user_agent

        http_method: None | str | Unset
        if isinstance(self.http_method, Unset):
            http_method = UNSET
        else:
            http_method = self.http_method

        resource_path: None | str | Unset
        if isinstance(self.resource_path, Unset):
            resource_path = UNSET
        else:
            resource_path = self.resource_path

        create_date_time: str | Unset = UNSET
        if not isinstance(self.create_date_time, Unset):
            create_date_time = self.create_date_time.isoformat()

        user_full_name: None | str | Unset
        if isinstance(self.user_full_name, Unset):
            user_full_name = UNSET
        else:
            user_full_name = self.user_full_name

        company_name: None | str | Unset
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        else:
            company_name = self.company_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if user_apikey_id is not UNSET:
            field_dict["user_apikey_id"] = user_apikey_id
        if success is not UNSET:
            field_dict["success"] = success
        if failure_reason is not UNSET:
            field_dict["failure_reason"] = failure_reason
        if source_ip is not UNSET:
            field_dict["source_ip"] = source_ip
        if user_agent is not UNSET:
            field_dict["user_agent"] = user_agent
        if http_method is not UNSET:
            field_dict["http_method"] = http_method
        if resource_path is not UNSET:
            field_dict["resource_path"] = resource_path
        if create_date_time is not UNSET:
            field_dict["create_date_time"] = create_date_time
        if user_full_name is not UNSET:
            field_dict["user_full_name"] = user_full_name
        if company_name is not UNSET:
            field_dict["company_name"] = company_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        user_id = d.pop("user_id", UNSET)

        def _parse_user_apikey_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        user_apikey_id = _parse_user_apikey_id(d.pop("user_apikey_id", UNSET))

        success = d.pop("success", UNSET)

        def _parse_failure_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        failure_reason = _parse_failure_reason(d.pop("failure_reason", UNSET))

        def _parse_source_ip(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_ip = _parse_source_ip(d.pop("source_ip", UNSET))

        def _parse_user_agent(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_agent = _parse_user_agent(d.pop("user_agent", UNSET))

        def _parse_http_method(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        http_method = _parse_http_method(d.pop("http_method", UNSET))

        def _parse_resource_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_path = _parse_resource_path(d.pop("resource_path", UNSET))

        _create_date_time = d.pop("create_date_time", UNSET)
        create_date_time: datetime.datetime | Unset
        if isinstance(_create_date_time, Unset):
            create_date_time = UNSET
        else:
            create_date_time = isoparse(_create_date_time)

        def _parse_user_full_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_full_name = _parse_user_full_name(d.pop("user_full_name", UNSET))

        def _parse_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_name = _parse_company_name(d.pop("company_name", UNSET))

        user_auth_trace_fields = cls(
            id=id,
            user_id=user_id,
            user_apikey_id=user_apikey_id,
            success=success,
            failure_reason=failure_reason,
            source_ip=source_ip,
            user_agent=user_agent,
            http_method=http_method,
            resource_path=resource_path,
            create_date_time=create_date_time,
            user_full_name=user_full_name,
            company_name=company_name,
        )

        user_auth_trace_fields.additional_properties = d
        return user_auth_trace_fields

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
