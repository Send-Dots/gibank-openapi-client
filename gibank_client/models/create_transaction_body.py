from __future__ import annotations

from collections.abc import Mapping
from typing import Any
from typing import TypeVar
from typing import cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_transaction_body_type import CreateTransactionBodyType
from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="CreateTransactionBody")


@_attrs_define
class CreateTransactionBody:
    """
    Attributes:
        type_ (CreateTransactionBodyType | Unset): The type of transaction to make, currently only ach and book
            available Example: book.
        origin_subclient_id (int | None | Unset): The ID of the origin subclient. Subclient must have one and only one
            active account Example: 1.
        origin_subclient_account_id (int | None | Unset): The ID of the origin subclient account Example: 1.
        destination_subclient_id (int | None | Unset): The ID of the destination subclient. Subclient must have one and
            only one active account Example: 2.
        destination_subclient_account_id (int | None | Unset): The ID of the destination subclient account Example: 2.
        external_key (None | str | Unset): The external key used by bank customer to refer to transactions it maintains
            using its own systems Example: EXT12345.
        amount (float | Unset): The amount of the transaction (Number of cents). Example: 100050.
        true_sender_subclient_id (int | None | Unset): The ID of the subclient for the true sender. A subtransaction
            will be created if specified. Example: 1.
        ultimate_beneficiary_subclient_id (int | None | Unset): The ID of the subclient for the ultimate beneficiary. A
            subtransaction will be created if specified. Example: 1.
        fees (float | None | Unset): Fees charged by Bank client (Number of cents) Example: 500.
        purpose (None | str | Unset): The purpose of the transaction Example: Payment for services.
        reference (None | str | Unset): Additional reference Example: 123456789.
        test (bool | None | Unset): Indicates if the transaction is a test transaction Example: True.
        simulate (bool | None | Unset): Indicates if it's only a simulation or if the transaction must be stored
            permanently. If True, returned IDs are set to `-1`. Example: True.
    """

    type_: CreateTransactionBodyType | Unset = UNSET
    origin_subclient_id: int | None | Unset = UNSET
    origin_subclient_account_id: int | None | Unset = UNSET
    destination_subclient_id: int | None | Unset = UNSET
    destination_subclient_account_id: int | None | Unset = UNSET
    external_key: None | str | Unset = UNSET
    amount: float | Unset = UNSET
    true_sender_subclient_id: int | None | Unset = UNSET
    ultimate_beneficiary_subclient_id: int | None | Unset = UNSET
    fees: float | None | Unset = UNSET
    purpose: None | str | Unset = UNSET
    reference: None | str | Unset = UNSET
    test: bool | None | Unset = UNSET
    simulate: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        origin_subclient_id: int | None | Unset
        if isinstance(self.origin_subclient_id, Unset):
            origin_subclient_id = UNSET
        else:
            origin_subclient_id = self.origin_subclient_id

        origin_subclient_account_id: int | None | Unset
        if isinstance(self.origin_subclient_account_id, Unset):
            origin_subclient_account_id = UNSET
        else:
            origin_subclient_account_id = self.origin_subclient_account_id

        destination_subclient_id: int | None | Unset
        if isinstance(self.destination_subclient_id, Unset):
            destination_subclient_id = UNSET
        else:
            destination_subclient_id = self.destination_subclient_id

        destination_subclient_account_id: int | None | Unset
        if isinstance(self.destination_subclient_account_id, Unset):
            destination_subclient_account_id = UNSET
        else:
            destination_subclient_account_id = self.destination_subclient_account_id

        external_key: None | str | Unset
        if isinstance(self.external_key, Unset):
            external_key = UNSET
        else:
            external_key = self.external_key

        amount = self.amount

        true_sender_subclient_id: int | None | Unset
        if isinstance(self.true_sender_subclient_id, Unset):
            true_sender_subclient_id = UNSET
        else:
            true_sender_subclient_id = self.true_sender_subclient_id

        ultimate_beneficiary_subclient_id: int | None | Unset
        if isinstance(self.ultimate_beneficiary_subclient_id, Unset):
            ultimate_beneficiary_subclient_id = UNSET
        else:
            ultimate_beneficiary_subclient_id = self.ultimate_beneficiary_subclient_id

        fees: float | None | Unset
        if isinstance(self.fees, Unset):
            fees = UNSET
        else:
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

        test: bool | None | Unset
        if isinstance(self.test, Unset):
            test = UNSET
        else:
            test = self.test

        simulate: bool | None | Unset
        if isinstance(self.simulate, Unset):
            simulate = UNSET
        else:
            simulate = self.simulate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if origin_subclient_id is not UNSET:
            field_dict["origin_subclient_id"] = origin_subclient_id
        if origin_subclient_account_id is not UNSET:
            field_dict["origin_subclient_account_id"] = origin_subclient_account_id
        if destination_subclient_id is not UNSET:
            field_dict["destination_subclient_id"] = destination_subclient_id
        if destination_subclient_account_id is not UNSET:
            field_dict["destination_subclient_account_id"] = (
                destination_subclient_account_id
            )
        if external_key is not UNSET:
            field_dict["external_key"] = external_key
        if amount is not UNSET:
            field_dict["amount"] = amount
        if true_sender_subclient_id is not UNSET:
            field_dict["true_sender_subclient_id"] = true_sender_subclient_id
        if ultimate_beneficiary_subclient_id is not UNSET:
            field_dict["ultimate_beneficiary_subclient_id"] = (
                ultimate_beneficiary_subclient_id
            )
        if fees is not UNSET:
            field_dict["fees"] = fees
        if purpose is not UNSET:
            field_dict["purpose"] = purpose
        if reference is not UNSET:
            field_dict["reference"] = reference
        if test is not UNSET:
            field_dict["test"] = test
        if simulate is not UNSET:
            field_dict["simulate"] = simulate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: CreateTransactionBodyType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = CreateTransactionBodyType(_type_)

        def _parse_origin_subclient_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        origin_subclient_id = _parse_origin_subclient_id(
            d.pop("origin_subclient_id", UNSET)
        )

        def _parse_origin_subclient_account_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        origin_subclient_account_id = _parse_origin_subclient_account_id(
            d.pop("origin_subclient_account_id", UNSET)
        )

        def _parse_destination_subclient_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        destination_subclient_id = _parse_destination_subclient_id(
            d.pop("destination_subclient_id", UNSET)
        )

        def _parse_destination_subclient_account_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        destination_subclient_account_id = _parse_destination_subclient_account_id(
            d.pop("destination_subclient_account_id", UNSET)
        )

        def _parse_external_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_key = _parse_external_key(d.pop("external_key", UNSET))

        amount = d.pop("amount", UNSET)

        def _parse_true_sender_subclient_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        true_sender_subclient_id = _parse_true_sender_subclient_id(
            d.pop("true_sender_subclient_id", UNSET)
        )

        def _parse_ultimate_beneficiary_subclient_id(
            data: object,
        ) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ultimate_beneficiary_subclient_id = _parse_ultimate_beneficiary_subclient_id(
            d.pop("ultimate_beneficiary_subclient_id", UNSET)
        )

        def _parse_fees(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        fees = _parse_fees(d.pop("fees", UNSET))

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

        def _parse_test(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        test = _parse_test(d.pop("test", UNSET))

        def _parse_simulate(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        simulate = _parse_simulate(d.pop("simulate", UNSET))

        create_transaction_body = cls(
            type_=type_,
            origin_subclient_id=origin_subclient_id,
            origin_subclient_account_id=origin_subclient_account_id,
            destination_subclient_id=destination_subclient_id,
            destination_subclient_account_id=destination_subclient_account_id,
            external_key=external_key,
            amount=amount,
            true_sender_subclient_id=true_sender_subclient_id,
            ultimate_beneficiary_subclient_id=ultimate_beneficiary_subclient_id,
            fees=fees,
            purpose=purpose,
            reference=reference,
            test=test,
            simulate=simulate,
        )

        create_transaction_body.additional_properties = d
        return create_transaction_body

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
