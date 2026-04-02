from __future__ import annotations

from collections.abc import Mapping
from typing import Any
from typing import TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.batch_client_update_state import BatchClientUpdateState
from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="BatchClientUpdate")


@_attrs_define
class BatchClientUpdate:
    """
    Attributes:
        state (BatchClientUpdateState | Unset): The state of the batch Example: canceled.
        state_change_reason (str | Unset): The reason for the state change (required when state is set to `canceled`)
            Example: No longer needed.
    """

    state: BatchClientUpdateState | Unset = UNSET
    state_change_reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        state_change_reason = self.state_change_reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if state_change_reason is not UNSET:
            field_dict["state_change_reason"] = state_change_reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _state = d.pop("state", UNSET)
        state: BatchClientUpdateState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = BatchClientUpdateState(_state)

        state_change_reason = d.pop("state_change_reason", UNSET)

        batch_client_update = cls(
            state=state,
            state_change_reason=state_change_reason,
        )

        batch_client_update.additional_properties = d
        return batch_client_update

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
