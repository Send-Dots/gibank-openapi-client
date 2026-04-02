from __future__ import annotations

from collections.abc import Mapping
from typing import Any
from typing import TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.client_reconciliation_transaction_fields_destination_account_type import (
    ClientReconciliationTransactionFieldsDestinationAccountType,
)
from ..models.client_reconciliation_transaction_fields_origin_account_type import (
    ClientReconciliationTransactionFieldsOriginAccountType,
)
from ..models.client_reconciliation_transaction_fields_transfer_flow import (
    ClientReconciliationTransactionFieldsTransferFlow,
)
from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="ClientReconciliationTransactionFields")


@_attrs_define
class ClientReconciliationTransactionFields:
    """
    Attributes:
        transaction_id (float | Unset): The ID for the GIB API transaction associated with this transaction, if any.
            Example: 1234.
        origin_routing_number (str | Unset): The origin routing number Example: 091001322.
        origin_account_number (str | Unset): The origin account number Example: 12345.
        origin_account_type (ClientReconciliationTransactionFieldsOriginAccountType | Unset): The origin account type
        destination_routing_number (str | Unset): The destination routing number Example: 091001322.
        destination_account_number (str | Unset): The destination account number Example: 12345.
        destination_account_type (ClientReconciliationTransactionFieldsDestinationAccountType | Unset): The origin
            account type
        amount (float | Unset): The amount of USD, in cents, the transaction is for Example: 1000.
        transfer_flow (ClientReconciliationTransactionFieldsTransferFlow | Unset): If the transaction credits (push) or
            debits (pull) the destination account.
    """

    transaction_id: float | Unset = UNSET
    origin_routing_number: str | Unset = UNSET
    origin_account_number: str | Unset = UNSET
    origin_account_type: (
        ClientReconciliationTransactionFieldsOriginAccountType | Unset
    ) = UNSET
    destination_routing_number: str | Unset = UNSET
    destination_account_number: str | Unset = UNSET
    destination_account_type: (
        ClientReconciliationTransactionFieldsDestinationAccountType | Unset
    ) = UNSET
    amount: float | Unset = UNSET
    transfer_flow: ClientReconciliationTransactionFieldsTransferFlow | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        transaction_id = self.transaction_id

        origin_routing_number = self.origin_routing_number

        origin_account_number = self.origin_account_number

        origin_account_type: str | Unset = UNSET
        if not isinstance(self.origin_account_type, Unset):
            origin_account_type = self.origin_account_type.value

        destination_routing_number = self.destination_routing_number

        destination_account_number = self.destination_account_number

        destination_account_type: str | Unset = UNSET
        if not isinstance(self.destination_account_type, Unset):
            destination_account_type = self.destination_account_type.value

        amount = self.amount

        transfer_flow: str | Unset = UNSET
        if not isinstance(self.transfer_flow, Unset):
            transfer_flow = self.transfer_flow.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if transaction_id is not UNSET:
            field_dict["transaction_id"] = transaction_id
        if origin_routing_number is not UNSET:
            field_dict["origin_routing_number"] = origin_routing_number
        if origin_account_number is not UNSET:
            field_dict["origin_account_number"] = origin_account_number
        if origin_account_type is not UNSET:
            field_dict["origin_account_type"] = origin_account_type
        if destination_routing_number is not UNSET:
            field_dict["destination_routing_number"] = destination_routing_number
        if destination_account_number is not UNSET:
            field_dict["destination_account_number"] = destination_account_number
        if destination_account_type is not UNSET:
            field_dict["destination_account_type"] = destination_account_type
        if amount is not UNSET:
            field_dict["amount"] = amount
        if transfer_flow is not UNSET:
            field_dict["transfer_flow"] = transfer_flow

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        transaction_id = d.pop("transaction_id", UNSET)

        origin_routing_number = d.pop("origin_routing_number", UNSET)

        origin_account_number = d.pop("origin_account_number", UNSET)

        _origin_account_type = d.pop("origin_account_type", UNSET)
        origin_account_type: (
            ClientReconciliationTransactionFieldsOriginAccountType | Unset
        )
        if isinstance(_origin_account_type, Unset):
            origin_account_type = UNSET
        else:
            origin_account_type = (
                ClientReconciliationTransactionFieldsOriginAccountType(
                    _origin_account_type
                )
            )

        destination_routing_number = d.pop("destination_routing_number", UNSET)

        destination_account_number = d.pop("destination_account_number", UNSET)

        _destination_account_type = d.pop("destination_account_type", UNSET)
        destination_account_type: (
            ClientReconciliationTransactionFieldsDestinationAccountType | Unset
        )
        if isinstance(_destination_account_type, Unset):
            destination_account_type = UNSET
        else:
            destination_account_type = (
                ClientReconciliationTransactionFieldsDestinationAccountType(
                    _destination_account_type
                )
            )

        amount = d.pop("amount", UNSET)

        _transfer_flow = d.pop("transfer_flow", UNSET)
        transfer_flow: ClientReconciliationTransactionFieldsTransferFlow | Unset
        if isinstance(_transfer_flow, Unset):
            transfer_flow = UNSET
        else:
            transfer_flow = ClientReconciliationTransactionFieldsTransferFlow(
                _transfer_flow
            )

        client_reconciliation_transaction_fields = cls(
            transaction_id=transaction_id,
            origin_routing_number=origin_routing_number,
            origin_account_number=origin_account_number,
            origin_account_type=origin_account_type,
            destination_routing_number=destination_routing_number,
            destination_account_number=destination_account_number,
            destination_account_type=destination_account_type,
            amount=amount,
            transfer_flow=transfer_flow,
        )

        client_reconciliation_transaction_fields.additional_properties = d
        return client_reconciliation_transaction_fields

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
