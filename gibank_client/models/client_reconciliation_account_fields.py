from __future__ import annotations

from collections.abc import Mapping
from typing import Any
from typing import TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.client_reconciliation_account_fields_account_type import (
    ClientReconciliationAccountFieldsAccountType,
)
from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="ClientReconciliationAccountFields")


@_attrs_define
class ClientReconciliationAccountFields:
    """
    Attributes:
        account_number (str | Unset): The account number of the account Example: 1234.
        account_type (ClientReconciliationAccountFieldsAccountType | Unset): The account type
        balance (float | Unset): The USD balance of the account, in cents Example: 10000.
    """

    account_number: str | Unset = UNSET
    account_type: ClientReconciliationAccountFieldsAccountType | Unset = UNSET
    balance: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_number = self.account_number

        account_type: str | Unset = UNSET
        if not isinstance(self.account_type, Unset):
            account_type = self.account_type.value

        balance = self.balance

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_number is not UNSET:
            field_dict["account_number"] = account_number
        if account_type is not UNSET:
            field_dict["account_type"] = account_type
        if balance is not UNSET:
            field_dict["balance"] = balance

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_number = d.pop("account_number", UNSET)

        _account_type = d.pop("account_type", UNSET)
        account_type: ClientReconciliationAccountFieldsAccountType | Unset
        if isinstance(_account_type, Unset):
            account_type = UNSET
        else:
            account_type = ClientReconciliationAccountFieldsAccountType(_account_type)

        balance = d.pop("balance", UNSET)

        client_reconciliation_account_fields = cls(
            account_number=account_number,
            account_type=account_type,
            balance=balance,
        )

        client_reconciliation_account_fields.additional_properties = d
        return client_reconciliation_account_fields

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
