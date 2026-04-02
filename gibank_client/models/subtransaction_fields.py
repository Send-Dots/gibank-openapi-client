from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any
from typing import TypeVar
from typing import cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.subtransaction_fields_transfer_direction import (
    SubtransactionFieldsTransferDirection,
)
from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="SubtransactionFields")


@_attrs_define
class SubtransactionFields:
    """
    Attributes:
        id (int | Unset): The subtransaction ID Example: 1.
        external_key (None | str | Unset): The external key used by bank customer to refer to transactions it maintains
            using its own systems Example: EXT12345.
        subclient_origin_id (int | Unset): The ID of the origin subclient Example: 1.
        subclient_destination_id (int | Unset): The ID of the destination subclient Example: 2.
        amount (float | Unset): The amount of the transaction (Number of cents) Example: 100050.
        currency (str | Unset): The ISO-4217 code for the Transaction's currency Example: USD.
        fees (float | Unset): Fees charged by Bank client (Number of cents) Example: 500.
        purpose (None | str | Unset): The purpose of the transaction Example: Payment for services.
        transfer_direction (SubtransactionFieldsTransferDirection | Unset): The direction of the transfer. `outbound`
            means money left your account, `inbound` means money was added to your account. Only for information, in general
            always `outbound` for sending transfers from origin to destination. Example: outbound.
        reference (None | str | Unset): The subtransaction reference Example: 123456789.
        date_time (datetime.datetime | Unset): The date and time of the subtransaction (Stored as UTC, formatted as zero
            UTC offset (Zulu) format) Example: 2024-02-04T23:00:00.000Z.
        subclient_origin_name (str | Unset): The name of the origin subclient Example: Acme Inc..
        subclient_destination_name (str | Unset): The name of the destination subclient Example: XYZ Corp.
        company_id (float | Unset): The company ID Example: 1.
        company_name (str | Unset): The company name of the subtransaction Example: ABC Fintech.
        create_date_time (datetime.datetime | Unset): The date and time when the subtransaction was created (Stored as
            UTC, formatted as zero UTC offset (Zulu) format) Example: 2024-02-04T23:00:00.000Z.
        update_date_time (datetime.datetime | Unset): The date and time when the subtransaction was last updated (Stored
            as UTC, formatted as zero UTC offset (Zulu) format) Example: 2024-02-04T23:00:00.000Z.
        create_user_id (int | Unset): The ID of the user who created the subtransaction Example: 1.
        create_user_full_name (str | Unset): The full name of the user who created the subtransaction Example: John Doe.
        update_user_id (int | Unset): The ID of the user who last updated the subtransaction Example: 2.
        update_user_full_name (str | Unset): The full name of the user who last updated the subtransaction Example: Jane
            Smith.
        deleted (bool | Unset): Indicates if the subtransaction is deleted
    """

    id: int | Unset = UNSET
    external_key: None | str | Unset = UNSET
    subclient_origin_id: int | Unset = UNSET
    subclient_destination_id: int | Unset = UNSET
    amount: float | Unset = UNSET
    currency: str | Unset = UNSET
    fees: float | Unset = UNSET
    purpose: None | str | Unset = UNSET
    transfer_direction: SubtransactionFieldsTransferDirection | Unset = UNSET
    reference: None | str | Unset = UNSET
    date_time: datetime.datetime | Unset = UNSET
    subclient_origin_name: str | Unset = UNSET
    subclient_destination_name: str | Unset = UNSET
    company_id: float | Unset = UNSET
    company_name: str | Unset = UNSET
    create_date_time: datetime.datetime | Unset = UNSET
    update_date_time: datetime.datetime | Unset = UNSET
    create_user_id: int | Unset = UNSET
    create_user_full_name: str | Unset = UNSET
    update_user_id: int | Unset = UNSET
    update_user_full_name: str | Unset = UNSET
    deleted: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        external_key: None | str | Unset
        if isinstance(self.external_key, Unset):
            external_key = UNSET
        else:
            external_key = self.external_key

        subclient_origin_id = self.subclient_origin_id

        subclient_destination_id = self.subclient_destination_id

        amount = self.amount

        currency = self.currency

        fees = self.fees

        purpose: None | str | Unset
        if isinstance(self.purpose, Unset):
            purpose = UNSET
        else:
            purpose = self.purpose

        transfer_direction: str | Unset = UNSET
        if not isinstance(self.transfer_direction, Unset):
            transfer_direction = self.transfer_direction.value

        reference: None | str | Unset
        if isinstance(self.reference, Unset):
            reference = UNSET
        else:
            reference = self.reference

        date_time: str | Unset = UNSET
        if not isinstance(self.date_time, Unset):
            date_time = self.date_time.isoformat()

        subclient_origin_name = self.subclient_origin_name

        subclient_destination_name = self.subclient_destination_name

        company_id = self.company_id

        company_name = self.company_name

        create_date_time: str | Unset = UNSET
        if not isinstance(self.create_date_time, Unset):
            create_date_time = self.create_date_time.isoformat()

        update_date_time: str | Unset = UNSET
        if not isinstance(self.update_date_time, Unset):
            update_date_time = self.update_date_time.isoformat()

        create_user_id = self.create_user_id

        create_user_full_name = self.create_user_full_name

        update_user_id = self.update_user_id

        update_user_full_name = self.update_user_full_name

        deleted = self.deleted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if external_key is not UNSET:
            field_dict["external_key"] = external_key
        if subclient_origin_id is not UNSET:
            field_dict["subclient_origin_id"] = subclient_origin_id
        if subclient_destination_id is not UNSET:
            field_dict["subclient_destination_id"] = subclient_destination_id
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if fees is not UNSET:
            field_dict["fees"] = fees
        if purpose is not UNSET:
            field_dict["purpose"] = purpose
        if transfer_direction is not UNSET:
            field_dict["transfer_direction"] = transfer_direction
        if reference is not UNSET:
            field_dict["reference"] = reference
        if date_time is not UNSET:
            field_dict["date_time"] = date_time
        if subclient_origin_name is not UNSET:
            field_dict["subclient_origin_name"] = subclient_origin_name
        if subclient_destination_name is not UNSET:
            field_dict["subclient_destination_name"] = subclient_destination_name
        if company_id is not UNSET:
            field_dict["company_id"] = company_id
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if create_date_time is not UNSET:
            field_dict["create_date_time"] = create_date_time
        if update_date_time is not UNSET:
            field_dict["update_date_time"] = update_date_time
        if create_user_id is not UNSET:
            field_dict["create_user_id"] = create_user_id
        if create_user_full_name is not UNSET:
            field_dict["create_user_full_name"] = create_user_full_name
        if update_user_id is not UNSET:
            field_dict["update_user_id"] = update_user_id
        if update_user_full_name is not UNSET:
            field_dict["update_user_full_name"] = update_user_full_name
        if deleted is not UNSET:
            field_dict["deleted"] = deleted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_external_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_key = _parse_external_key(d.pop("external_key", UNSET))

        subclient_origin_id = d.pop("subclient_origin_id", UNSET)

        subclient_destination_id = d.pop("subclient_destination_id", UNSET)

        amount = d.pop("amount", UNSET)

        currency = d.pop("currency", UNSET)

        fees = d.pop("fees", UNSET)

        def _parse_purpose(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        purpose = _parse_purpose(d.pop("purpose", UNSET))

        _transfer_direction = d.pop("transfer_direction", UNSET)
        transfer_direction: SubtransactionFieldsTransferDirection | Unset
        if isinstance(_transfer_direction, Unset):
            transfer_direction = UNSET
        else:
            transfer_direction = SubtransactionFieldsTransferDirection(
                _transfer_direction
            )

        def _parse_reference(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reference = _parse_reference(d.pop("reference", UNSET))

        _date_time = d.pop("date_time", UNSET)
        date_time: datetime.datetime | Unset
        if isinstance(_date_time, Unset):
            date_time = UNSET
        else:
            date_time = isoparse(_date_time)

        subclient_origin_name = d.pop("subclient_origin_name", UNSET)

        subclient_destination_name = d.pop("subclient_destination_name", UNSET)

        company_id = d.pop("company_id", UNSET)

        company_name = d.pop("company_name", UNSET)

        _create_date_time = d.pop("create_date_time", UNSET)
        create_date_time: datetime.datetime | Unset
        if isinstance(_create_date_time, Unset):
            create_date_time = UNSET
        else:
            create_date_time = isoparse(_create_date_time)

        _update_date_time = d.pop("update_date_time", UNSET)
        update_date_time: datetime.datetime | Unset
        if isinstance(_update_date_time, Unset):
            update_date_time = UNSET
        else:
            update_date_time = isoparse(_update_date_time)

        create_user_id = d.pop("create_user_id", UNSET)

        create_user_full_name = d.pop("create_user_full_name", UNSET)

        update_user_id = d.pop("update_user_id", UNSET)

        update_user_full_name = d.pop("update_user_full_name", UNSET)

        deleted = d.pop("deleted", UNSET)

        subtransaction_fields = cls(
            id=id,
            external_key=external_key,
            subclient_origin_id=subclient_origin_id,
            subclient_destination_id=subclient_destination_id,
            amount=amount,
            currency=currency,
            fees=fees,
            purpose=purpose,
            transfer_direction=transfer_direction,
            reference=reference,
            date_time=date_time,
            subclient_origin_name=subclient_origin_name,
            subclient_destination_name=subclient_destination_name,
            company_id=company_id,
            company_name=company_name,
            create_date_time=create_date_time,
            update_date_time=update_date_time,
            create_user_id=create_user_id,
            create_user_full_name=create_user_full_name,
            update_user_id=update_user_id,
            update_user_full_name=update_user_full_name,
            deleted=deleted,
        )

        subtransaction_fields.additional_properties = d
        return subtransaction_fields

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
