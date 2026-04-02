from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING
from typing import Any
from typing import TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.health_result_status import HealthResultStatus
from ..types import UNSET
from ..types import Unset

if TYPE_CHECKING:
    from ..models.health_result_details import HealthResultDetails


T = TypeVar("T", bound="HealthResult")


@_attrs_define
class HealthResult:
    """
    Attributes:
        status (HealthResultStatus | Unset):
        latency_ms (int | Unset): Response latency in milliseconds
        details (HealthResultDetails | Unset): Component-specific details
        error (str | Unset): Error message if status is unknown, degraded or unhealthy
    """

    status: HealthResultStatus | Unset = UNSET
    latency_ms: int | Unset = UNSET
    details: HealthResultDetails | Unset = UNSET
    error: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        latency_ms = self.latency_ms

        details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if latency_ms is not UNSET:
            field_dict["latency_ms"] = latency_ms
        if details is not UNSET:
            field_dict["details"] = details
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.health_result_details import HealthResultDetails

        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: HealthResultStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = HealthResultStatus(_status)

        latency_ms = d.pop("latency_ms", UNSET)

        _details = d.pop("details", UNSET)
        details: HealthResultDetails | Unset
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = HealthResultDetails.from_dict(_details)

        error = d.pop("error", UNSET)

        health_result = cls(
            status=status,
            latency_ms=latency_ms,
            details=details,
            error=error,
        )

        health_result.additional_properties = d
        return health_result

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
