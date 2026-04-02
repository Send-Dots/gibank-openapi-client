from __future__ import annotations

from collections.abc import Mapping
from typing import Any
from typing import TypeVar
from typing import cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.subclient_account_create_external_type import (
    SubclientAccountCreateExternalType,
)
from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="SubclientAccountCreateExternal")


@_attrs_define
class SubclientAccountCreateExternal:
    """Create a Subclient Account of type External

    Example:
        {'type': 'external', 'routing_number': '091001322', 'account_number': '5678NEW', 'description': 'New external
            account', 'active': True}

    Attributes:
        type_ (SubclientAccountCreateExternalType): The type of the subclient account Example: external.
        routing_number (str): The routing number of the subclient account Example: 091001322.
        account_number (str): The account number of the subclient account Example: 1234.
        description (None | str | Unset): The description of the subclient account Example: Test Account.
        active (bool | Unset): Indicates if the subclient account is active Example: True.
    """

    type_: SubclientAccountCreateExternalType
    routing_number: str
    account_number: str
    description: None | str | Unset = UNSET
    active: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        routing_number = self.routing_number

        account_number = self.account_number

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        active = self.active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "routing_number": routing_number,
                "account_number": account_number,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if active is not UNSET:
            field_dict["active"] = active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = SubclientAccountCreateExternalType(d.pop("type"))

        routing_number = d.pop("routing_number")

        account_number = d.pop("account_number")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        active = d.pop("active", UNSET)

        subclient_account_create_external = cls(
            type_=type_,
            routing_number=routing_number,
            account_number=account_number,
            description=description,
            active=active,
        )

        subclient_account_create_external.additional_properties = d
        return subclient_account_create_external

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
