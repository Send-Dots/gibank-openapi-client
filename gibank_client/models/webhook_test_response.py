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
    from ..models.webhook_test_response_trigger_item import (
        WebhookTestResponseTriggerItem,
    )


T = TypeVar("T", bound="WebhookTestResponse")


@_attrs_define
class WebhookTestResponse:
    """
    Attributes:
        trigger (list[WebhookTestResponseTriggerItem] | Unset): The list of triggered items
    """

    trigger: list[WebhookTestResponseTriggerItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        trigger: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.trigger, Unset):
            trigger = []
            for trigger_item_data in self.trigger:
                trigger_item = trigger_item_data.to_dict()
                trigger.append(trigger_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if trigger is not UNSET:
            field_dict["trigger"] = trigger

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_test_response_trigger_item import (
            WebhookTestResponseTriggerItem,
        )

        d = dict(src_dict)
        _trigger = d.pop("trigger", UNSET)
        trigger: list[WebhookTestResponseTriggerItem] | Unset = UNSET
        if _trigger is not UNSET:
            trigger = []
            for trigger_item_data in _trigger:
                trigger_item = WebhookTestResponseTriggerItem.from_dict(
                    trigger_item_data
                )

                trigger.append(trigger_item)

        webhook_test_response = cls(
            trigger=trigger,
        )

        webhook_test_response.additional_properties = d
        return webhook_test_response

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
