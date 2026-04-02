from __future__ import annotations

from collections.abc import Mapping
from typing import Any
from typing import TypeVar
from typing import cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.subclient_account_create_core_type import SubclientAccountCreateCoreType
from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="SubclientAccountCreateCore")


@_attrs_define
class SubclientAccountCreateCore:
    """
    Example:
        {'type': 'core', 'routing_number': '091208154', 'account_number': '123123', 'description': 'New core account',
            'active': True}

    Attributes:
        type_ (SubclientAccountCreateCoreType): The type of the subclient account Example: core.
        account_number (str): The account number of the subclient account Example: 1234.
        routing_number (str): The routing number of the subclient account Example: 091001322.
        description (None | str | Unset): The description of the subclient account Example: Test Account.
        active (bool | Unset): Indicates if the subclient account is active Example: True.
    """

    type_: SubclientAccountCreateCoreType
    account_number: str
    routing_number: str
    description: None | str | Unset = UNSET
    active: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        account_number = self.account_number

        routing_number = self.routing_number

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
                "account_number": account_number,
                "routing_number": routing_number,
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
        type_ = SubclientAccountCreateCoreType(d.pop("type"))

        account_number = d.pop("account_number")

        routing_number = d.pop("routing_number")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        active = d.pop("active", UNSET)

        subclient_account_create_core = cls(
            type_=type_,
            account_number=account_number,
            routing_number=routing_number,
            description=description,
            active=active,
        )

        subclient_account_create_core.additional_properties = d
        return subclient_account_create_core

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
