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
    from ..models.health_result import HealthResult


T = TypeVar("T", bound="HealthResponseComponents")


@_attrs_define
class HealthResponseComponents:
    """
    Attributes:
        database (HealthResult | Unset):
        icl_service (HealthResult | Unset):
        icl_automation (HealthResult | Unset):
        ach_service (HealthResult | Unset):
        ach_automation (HealthResult | Unset):
        wire_service (HealthResult | Unset):
        balances (HealthResult | Unset):
        core (HealthResult | Unset):
    """

    database: HealthResult | Unset = UNSET
    icl_service: HealthResult | Unset = UNSET
    icl_automation: HealthResult | Unset = UNSET
    ach_service: HealthResult | Unset = UNSET
    ach_automation: HealthResult | Unset = UNSET
    wire_service: HealthResult | Unset = UNSET
    balances: HealthResult | Unset = UNSET
    core: HealthResult | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        database: dict[str, Any] | Unset = UNSET
        if not isinstance(self.database, Unset):
            database = self.database.to_dict()

        icl_service: dict[str, Any] | Unset = UNSET
        if not isinstance(self.icl_service, Unset):
            icl_service = self.icl_service.to_dict()

        icl_automation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.icl_automation, Unset):
            icl_automation = self.icl_automation.to_dict()

        ach_service: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ach_service, Unset):
            ach_service = self.ach_service.to_dict()

        ach_automation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ach_automation, Unset):
            ach_automation = self.ach_automation.to_dict()

        wire_service: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wire_service, Unset):
            wire_service = self.wire_service.to_dict()

        balances: dict[str, Any] | Unset = UNSET
        if not isinstance(self.balances, Unset):
            balances = self.balances.to_dict()

        core: dict[str, Any] | Unset = UNSET
        if not isinstance(self.core, Unset):
            core = self.core.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if database is not UNSET:
            field_dict["database"] = database
        if icl_service is not UNSET:
            field_dict["icl_service"] = icl_service
        if icl_automation is not UNSET:
            field_dict["icl_automation"] = icl_automation
        if ach_service is not UNSET:
            field_dict["ach_service"] = ach_service
        if ach_automation is not UNSET:
            field_dict["ach_automation"] = ach_automation
        if wire_service is not UNSET:
            field_dict["wire_service"] = wire_service
        if balances is not UNSET:
            field_dict["balances"] = balances
        if core is not UNSET:
            field_dict["core"] = core

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.health_result import HealthResult

        d = dict(src_dict)
        _database = d.pop("database", UNSET)
        database: HealthResult | Unset
        if isinstance(_database, Unset):
            database = UNSET
        else:
            database = HealthResult.from_dict(_database)

        _icl_service = d.pop("icl_service", UNSET)
        icl_service: HealthResult | Unset
        if isinstance(_icl_service, Unset):
            icl_service = UNSET
        else:
            icl_service = HealthResult.from_dict(_icl_service)

        _icl_automation = d.pop("icl_automation", UNSET)
        icl_automation: HealthResult | Unset
        if isinstance(_icl_automation, Unset):
            icl_automation = UNSET
        else:
            icl_automation = HealthResult.from_dict(_icl_automation)

        _ach_service = d.pop("ach_service", UNSET)
        ach_service: HealthResult | Unset
        if isinstance(_ach_service, Unset):
            ach_service = UNSET
        else:
            ach_service = HealthResult.from_dict(_ach_service)

        _ach_automation = d.pop("ach_automation", UNSET)
        ach_automation: HealthResult | Unset
        if isinstance(_ach_automation, Unset):
            ach_automation = UNSET
        else:
            ach_automation = HealthResult.from_dict(_ach_automation)

        _wire_service = d.pop("wire_service", UNSET)
        wire_service: HealthResult | Unset
        if isinstance(_wire_service, Unset):
            wire_service = UNSET
        else:
            wire_service = HealthResult.from_dict(_wire_service)

        _balances = d.pop("balances", UNSET)
        balances: HealthResult | Unset
        if isinstance(_balances, Unset):
            balances = UNSET
        else:
            balances = HealthResult.from_dict(_balances)

        _core = d.pop("core", UNSET)
        core: HealthResult | Unset
        if isinstance(_core, Unset):
            core = UNSET
        else:
            core = HealthResult.from_dict(_core)

        health_response_components = cls(
            database=database,
            icl_service=icl_service,
            icl_automation=icl_automation,
            ach_service=ach_service,
            ach_automation=ach_automation,
            wire_service=wire_service,
            balances=balances,
            core=core,
        )

        health_response_components.additional_properties = d
        return health_response_components

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
