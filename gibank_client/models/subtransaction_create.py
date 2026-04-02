from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any
from typing import TypeVar
from typing import cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.transfer_direction import TransferDirection
from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="SubtransactionCreate")


@_attrs_define
class SubtransactionCreate:
    """
    Example:
        {'transaction_id': 101, 'external_key': 'MY-TX-007', 'subclient_origin_id': 1, 'subclient_destination_id': 2,
            'amount': 25075, 'currency': 'USD', 'fees': 250, 'purpose': 'Consulting services Q1', 'transfer_direction':
            'outbound', 'reference': 'INV-2025-Q1-003', 'date_time': '2025-02-10T10:30:00.000Z'}

    Attributes:
        subclient_origin_id (int): The ID of the origin subclient Example: 1.
        subclient_destination_id (int): The ID of the destination subclient Example: 2.
        amount (float): The amount of the transaction (Number of cents) Example: 100050.
        currency (str): The ISO-4217 code for the Transaction's currency Example: USD.
        transfer_direction (TransferDirection): The direction of the transfer. `outbound` means money left your account,
            `inbound` means money was added to your account. Only for information, in general always `outbound` for sending
            transfers from origin to destination. Example: outbound.
        date_time (datetime.datetime): The date and time of the subtransaction (Stored as UTC, formatted as zero UTC
            offset (Zulu) format) Example: 2024-02-04T23:00:00.000Z.
        transaction_id (int | None | Unset): The ID of the associated transaction. If you need more, please use the
            dedicated `link` endpoints. The value is not returned. Example: 1.
        external_key (None | str | Unset): The external key used by bank customer to refer to transactions it maintains
            using its own systems Example: EXT12345.
        fees (float | Unset): Fees charged by Bank client (Number of cents) Example: 500.
        purpose (None | str | Unset): The purpose of the transaction Example: Payment for services.
        reference (None | str | Unset): The subtransaction reference Example: 123456789.
    """

    subclient_origin_id: int
    subclient_destination_id: int
    amount: float
    currency: str
    transfer_direction: TransferDirection
    date_time: datetime.datetime
    transaction_id: int | None | Unset = UNSET
    external_key: None | str | Unset = UNSET
    fees: float | Unset = UNSET
    purpose: None | str | Unset = UNSET
    reference: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subclient_origin_id = self.subclient_origin_id

        subclient_destination_id = self.subclient_destination_id

        amount = self.amount

        currency = self.currency

        transfer_direction = self.transfer_direction.value

        date_time = self.date_time.isoformat()

        transaction_id: int | None | Unset
        if isinstance(self.transaction_id, Unset):
            transaction_id = UNSET
        else:
            transaction_id = self.transaction_id

        external_key: None | str | Unset
        if isinstance(self.external_key, Unset):
            external_key = UNSET
        else:
            external_key = self.external_key

        fees = self.fees

        purpose: None | str | Unset
        if isinstance(self.purpose, Unset):
            purpose = UNSET
        else:
            purpose = self.purpose

        reference: None | str | Unset
        if isinstance(self.reference, Unset):
            reference = UNSET
        else:
            reference = self.reference

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subclient_origin_id": subclient_origin_id,
                "subclient_destination_id": subclient_destination_id,
                "amount": amount,
                "currency": currency,
                "transfer_direction": transfer_direction,
                "date_time": date_time,
            }
        )
        if transaction_id is not UNSET:
            field_dict["transaction_id"] = transaction_id
        if external_key is not UNSET:
            field_dict["external_key"] = external_key
        if fees is not UNSET:
            field_dict["fees"] = fees
        if purpose is not UNSET:
            field_dict["purpose"] = purpose
        if reference is not UNSET:
            field_dict["reference"] = reference

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        subclient_origin_id = d.pop("subclient_origin_id")

        subclient_destination_id = d.pop("subclient_destination_id")

        amount = d.pop("amount")

        currency = d.pop("currency")

        transfer_direction = TransferDirection(d.pop("transfer_direction"))

        date_time = isoparse(d.pop("date_time"))

        def _parse_transaction_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        transaction_id = _parse_transaction_id(d.pop("transaction_id", UNSET))

        def _parse_external_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_key = _parse_external_key(d.pop("external_key", UNSET))

        fees = d.pop("fees", UNSET)

        def _parse_purpose(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        purpose = _parse_purpose(d.pop("purpose", UNSET))

        def _parse_reference(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reference = _parse_reference(d.pop("reference", UNSET))

        subtransaction_create = cls(
            subclient_origin_id=subclient_origin_id,
            subclient_destination_id=subclient_destination_id,
            amount=amount,
            currency=currency,
            transfer_direction=transfer_direction,
            date_time=date_time,
            transaction_id=transaction_id,
            external_key=external_key,
            fees=fees,
            purpose=purpose,
            reference=reference,
        )

        subtransaction_create.additional_properties = d
        return subtransaction_create

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
