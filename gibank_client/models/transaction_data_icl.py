from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any
from typing import TypeVar
from typing import cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.transaction_data_icl_return_code import TransactionDataICLReturnCode
from ..models.transaction_data_icl_transfer_type import TransactionDataICLTransferType
from ..models.transaction_data_icl_type import TransactionDataICLType
from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="TransactionDataICL")


@_attrs_define
class TransactionDataICL:
    """
    Attributes:
        file_create_date_time (datetime.datetime | Unset): The date and time when the batch file was created (Stored as
            UTC, formatted as zero UTC offset (Zulu) format) Example: 2024-02-04T23:00:00.000Z.
        amount (float | Unset): The transaction amount (Number of cents) Example: 100.
        origin_routing_number (None | str | Unset): The origin routing number Example: 091001322.
        origin_routing_name (None | str | Unset): The origin routing name Example: United Bankers Bank.
        origin_account_number (None | str | Unset): The origin account number Example: 12345.
        origin_account_name (None | str | Unset): The origin account name Example: ABC Fintech.
        destination_routing_number (None | str | Unset): The destination routing number Example: 091001322.
        destination_routing_name (None | str | Unset): The destination routing name Example: United Bankers Bank.
        destination_account_number (None | str | Unset): The destination account number Example: 12345.
        destination_account_name (None | str | Unset): The destination account name Example: ABC Fintech.
        origin_routing_number_virtual (None | str | Unset): The origin routing number (for virtual) Example: 091001322.
        origin_account_number_virtual (None | str | Unset): The origin account number (virtual) Example: 12345.
        destination_routing_number_virtual (None | str | Unset): The destination routing number (for virtual) Example:
            091001322.
        destination_account_number_virtual (None | str | Unset): The destination account number (virtual) Example:
            12345.
        has_virtual_origin (bool | Unset): Signifies that the origin was virtual
        has_virtual_destination (bool | Unset): Signifies that the destination was virtual
        type_ (TransactionDataICLType | Unset): The transaction type (ICL/Check) Example: icl.
        transfer_key (str | Unset): The transfer key identifying the line within the ICL file.
            Format: `cash_letter_idx_{i}_bundle_idx_{j}_check_idx_{k}` or
            `cash_letter_idx_{i}_bundle_idx_{j}_return_idx_{k}`
             Example: cash_letter_idx_1_bundle_idx_1_check_idx_1.
        transfer_type (TransactionDataICLTransferType | Unset): ICL Transfer Type Example: check.
        transfer_code (None | str | Unset): Not used for ICL
        reference (None | str | Unset): ICL Reference: `eceInstitutionItemSequenceNumber` Example: 123456789.
        trace_reference (None | str | Unset): ICL Trace: `eceInstitutionItemSequenceNumber` Example: 123456789.
        trace_reference_original (None | str | Unset): ICL Original Trace: `bofdItemSequenceNumber`. For Returns;
            matches with `trace_reference` or `trace_reference_final` Example: 123456789.
        trace_reference_final (None | str | Unset): ICL Final Trace: `eceInstitutionItemSequenceNumber` Example:
            123456789.
        payment_info (None | str | Unset): ICL Payment Info: `auxiliaryOnUs` Example: 000123.
        return_code (TransactionDataICLReturnCode | Unset): ICL Return Codes:
            - `A` - NSF - Not Sufficient Funds
            - `B` - UCF - Uncollected Funds Hold
            - `C` - Stop Payment
            - `D` - Closed Account
            - `E` - UTLA - Unable to Locate Account
            - `F` - Frozen/Blocked Account-Account has Restrictions placed on it by either customer or bank
            - `G` - Stale Dated
            - `H` - Post Dated
            - `I` - Endorsement Missing
            - `J` - Endorsement Irregular
            - `K` - Signature(s) Missing
            - `L` - Signature(s) Irregular, Suspected Forgery
            - `M` - Non-Cash Item (Non-Negotiable)
            - `N` - Altered/Fictitious Item/Suspected Counterfeit/Counterfeit
            - `O` - Unable to Process
            - `P` - Item Exceeds Stated Max Value
            - `Q` - Not Authorized
            - `R` - Branch/Account Sold
            - `S` - Refer to Maker
            - `T` - Item cannot be re-presented
            - `U` - Unusable Image
            - `W` - Cannot Determine Amount
            - `X` - Refer to Image
            - `Y` - Duplicate Presentment
            - `Z` - Forgery
            - `3` - Warranty Breach
            - `4` - RCC Warranty Breach
            - `5` - Forged and Counterfeit Warranty Breach
            - `6` - Retired/Ineligible/Failed Institution Routing Number
             Example: A.
    """

    file_create_date_time: datetime.datetime | Unset = UNSET
    amount: float | Unset = UNSET
    origin_routing_number: None | str | Unset = UNSET
    origin_routing_name: None | str | Unset = UNSET
    origin_account_number: None | str | Unset = UNSET
    origin_account_name: None | str | Unset = UNSET
    destination_routing_number: None | str | Unset = UNSET
    destination_routing_name: None | str | Unset = UNSET
    destination_account_number: None | str | Unset = UNSET
    destination_account_name: None | str | Unset = UNSET
    origin_routing_number_virtual: None | str | Unset = UNSET
    origin_account_number_virtual: None | str | Unset = UNSET
    destination_routing_number_virtual: None | str | Unset = UNSET
    destination_account_number_virtual: None | str | Unset = UNSET
    has_virtual_origin: bool | Unset = UNSET
    has_virtual_destination: bool | Unset = UNSET
    type_: TransactionDataICLType | Unset = UNSET
    transfer_key: str | Unset = UNSET
    transfer_type: TransactionDataICLTransferType | Unset = UNSET
    transfer_code: None | str | Unset = UNSET
    reference: None | str | Unset = UNSET
    trace_reference: None | str | Unset = UNSET
    trace_reference_original: None | str | Unset = UNSET
    trace_reference_final: None | str | Unset = UNSET
    payment_info: None | str | Unset = UNSET
    return_code: TransactionDataICLReturnCode | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_create_date_time: str | Unset = UNSET
        if not isinstance(self.file_create_date_time, Unset):
            file_create_date_time = self.file_create_date_time.isoformat()

        amount = self.amount

        origin_routing_number: None | str | Unset
        if isinstance(self.origin_routing_number, Unset):
            origin_routing_number = UNSET
        else:
            origin_routing_number = self.origin_routing_number

        origin_routing_name: None | str | Unset
        if isinstance(self.origin_routing_name, Unset):
            origin_routing_name = UNSET
        else:
            origin_routing_name = self.origin_routing_name

        origin_account_number: None | str | Unset
        if isinstance(self.origin_account_number, Unset):
            origin_account_number = UNSET
        else:
            origin_account_number = self.origin_account_number

        origin_account_name: None | str | Unset
        if isinstance(self.origin_account_name, Unset):
            origin_account_name = UNSET
        else:
            origin_account_name = self.origin_account_name

        destination_routing_number: None | str | Unset
        if isinstance(self.destination_routing_number, Unset):
            destination_routing_number = UNSET
        else:
            destination_routing_number = self.destination_routing_number

        destination_routing_name: None | str | Unset
        if isinstance(self.destination_routing_name, Unset):
            destination_routing_name = UNSET
        else:
            destination_routing_name = self.destination_routing_name

        destination_account_number: None | str | Unset
        if isinstance(self.destination_account_number, Unset):
            destination_account_number = UNSET
        else:
            destination_account_number = self.destination_account_number

        destination_account_name: None | str | Unset
        if isinstance(self.destination_account_name, Unset):
            destination_account_name = UNSET
        else:
            destination_account_name = self.destination_account_name

        origin_routing_number_virtual: None | str | Unset
        if isinstance(self.origin_routing_number_virtual, Unset):
            origin_routing_number_virtual = UNSET
        else:
            origin_routing_number_virtual = self.origin_routing_number_virtual

        origin_account_number_virtual: None | str | Unset
        if isinstance(self.origin_account_number_virtual, Unset):
            origin_account_number_virtual = UNSET
        else:
            origin_account_number_virtual = self.origin_account_number_virtual

        destination_routing_number_virtual: None | str | Unset
        if isinstance(self.destination_routing_number_virtual, Unset):
            destination_routing_number_virtual = UNSET
        else:
            destination_routing_number_virtual = self.destination_routing_number_virtual

        destination_account_number_virtual: None | str | Unset
        if isinstance(self.destination_account_number_virtual, Unset):
            destination_account_number_virtual = UNSET
        else:
            destination_account_number_virtual = self.destination_account_number_virtual

        has_virtual_origin = self.has_virtual_origin

        has_virtual_destination = self.has_virtual_destination

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        transfer_key = self.transfer_key

        transfer_type: str | Unset = UNSET
        if not isinstance(self.transfer_type, Unset):
            transfer_type = self.transfer_type.value

        transfer_code: None | str | Unset
        if isinstance(self.transfer_code, Unset):
            transfer_code = UNSET
        else:
            transfer_code = self.transfer_code

        reference: None | str | Unset
        if isinstance(self.reference, Unset):
            reference = UNSET
        else:
            reference = self.reference

        trace_reference: None | str | Unset
        if isinstance(self.trace_reference, Unset):
            trace_reference = UNSET
        else:
            trace_reference = self.trace_reference

        trace_reference_original: None | str | Unset
        if isinstance(self.trace_reference_original, Unset):
            trace_reference_original = UNSET
        else:
            trace_reference_original = self.trace_reference_original

        trace_reference_final: None | str | Unset
        if isinstance(self.trace_reference_final, Unset):
            trace_reference_final = UNSET
        else:
            trace_reference_final = self.trace_reference_final

        payment_info: None | str | Unset
        if isinstance(self.payment_info, Unset):
            payment_info = UNSET
        else:
            payment_info = self.payment_info

        return_code: str | Unset = UNSET
        if not isinstance(self.return_code, Unset):
            return_code = self.return_code.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file_create_date_time is not UNSET:
            field_dict["file_create_date_time"] = file_create_date_time
        if amount is not UNSET:
            field_dict["amount"] = amount
        if origin_routing_number is not UNSET:
            field_dict["origin_routing_number"] = origin_routing_number
        if origin_routing_name is not UNSET:
            field_dict["origin_routing_name"] = origin_routing_name
        if origin_account_number is not UNSET:
            field_dict["origin_account_number"] = origin_account_number
        if origin_account_name is not UNSET:
            field_dict["origin_account_name"] = origin_account_name
        if destination_routing_number is not UNSET:
            field_dict["destination_routing_number"] = destination_routing_number
        if destination_routing_name is not UNSET:
            field_dict["destination_routing_name"] = destination_routing_name
        if destination_account_number is not UNSET:
            field_dict["destination_account_number"] = destination_account_number
        if destination_account_name is not UNSET:
            field_dict["destination_account_name"] = destination_account_name
        if origin_routing_number_virtual is not UNSET:
            field_dict["origin_routing_number_virtual"] = origin_routing_number_virtual
        if origin_account_number_virtual is not UNSET:
            field_dict["origin_account_number_virtual"] = origin_account_number_virtual
        if destination_routing_number_virtual is not UNSET:
            field_dict["destination_routing_number_virtual"] = (
                destination_routing_number_virtual
            )
        if destination_account_number_virtual is not UNSET:
            field_dict["destination_account_number_virtual"] = (
                destination_account_number_virtual
            )
        if has_virtual_origin is not UNSET:
            field_dict["has_virtual_origin"] = has_virtual_origin
        if has_virtual_destination is not UNSET:
            field_dict["has_virtual_destination"] = has_virtual_destination
        if type_ is not UNSET:
            field_dict["type"] = type_
        if transfer_key is not UNSET:
            field_dict["transfer_key"] = transfer_key
        if transfer_type is not UNSET:
            field_dict["transfer_type"] = transfer_type
        if transfer_code is not UNSET:
            field_dict["transfer_code"] = transfer_code
        if reference is not UNSET:
            field_dict["reference"] = reference
        if trace_reference is not UNSET:
            field_dict["trace_reference"] = trace_reference
        if trace_reference_original is not UNSET:
            field_dict["trace_reference_original"] = trace_reference_original
        if trace_reference_final is not UNSET:
            field_dict["trace_reference_final"] = trace_reference_final
        if payment_info is not UNSET:
            field_dict["payment_info"] = payment_info
        if return_code is not UNSET:
            field_dict["return_code"] = return_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _file_create_date_time = d.pop("file_create_date_time", UNSET)
        file_create_date_time: datetime.datetime | Unset
        if isinstance(_file_create_date_time, Unset):
            file_create_date_time = UNSET
        else:
            file_create_date_time = isoparse(_file_create_date_time)

        amount = d.pop("amount", UNSET)

        def _parse_origin_routing_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        origin_routing_number = _parse_origin_routing_number(
            d.pop("origin_routing_number", UNSET)
        )

        def _parse_origin_routing_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        origin_routing_name = _parse_origin_routing_name(
            d.pop("origin_routing_name", UNSET)
        )

        def _parse_origin_account_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        origin_account_number = _parse_origin_account_number(
            d.pop("origin_account_number", UNSET)
        )

        def _parse_origin_account_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        origin_account_name = _parse_origin_account_name(
            d.pop("origin_account_name", UNSET)
        )

        def _parse_destination_routing_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        destination_routing_number = _parse_destination_routing_number(
            d.pop("destination_routing_number", UNSET)
        )

        def _parse_destination_routing_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        destination_routing_name = _parse_destination_routing_name(
            d.pop("destination_routing_name", UNSET)
        )

        def _parse_destination_account_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        destination_account_number = _parse_destination_account_number(
            d.pop("destination_account_number", UNSET)
        )

        def _parse_destination_account_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        destination_account_name = _parse_destination_account_name(
            d.pop("destination_account_name", UNSET)
        )

        def _parse_origin_routing_number_virtual(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        origin_routing_number_virtual = _parse_origin_routing_number_virtual(
            d.pop("origin_routing_number_virtual", UNSET)
        )

        def _parse_origin_account_number_virtual(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        origin_account_number_virtual = _parse_origin_account_number_virtual(
            d.pop("origin_account_number_virtual", UNSET)
        )

        def _parse_destination_routing_number_virtual(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        destination_routing_number_virtual = _parse_destination_routing_number_virtual(
            d.pop("destination_routing_number_virtual", UNSET)
        )

        def _parse_destination_account_number_virtual(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        destination_account_number_virtual = _parse_destination_account_number_virtual(
            d.pop("destination_account_number_virtual", UNSET)
        )

        has_virtual_origin = d.pop("has_virtual_origin", UNSET)

        has_virtual_destination = d.pop("has_virtual_destination", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: TransactionDataICLType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = TransactionDataICLType(_type_)

        transfer_key = d.pop("transfer_key", UNSET)

        _transfer_type = d.pop("transfer_type", UNSET)
        transfer_type: TransactionDataICLTransferType | Unset
        if isinstance(_transfer_type, Unset):
            transfer_type = UNSET
        else:
            transfer_type = TransactionDataICLTransferType(_transfer_type)

        def _parse_transfer_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        transfer_code = _parse_transfer_code(d.pop("transfer_code", UNSET))

        def _parse_reference(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reference = _parse_reference(d.pop("reference", UNSET))

        def _parse_trace_reference(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trace_reference = _parse_trace_reference(d.pop("trace_reference", UNSET))

        def _parse_trace_reference_original(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trace_reference_original = _parse_trace_reference_original(
            d.pop("trace_reference_original", UNSET)
        )

        def _parse_trace_reference_final(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trace_reference_final = _parse_trace_reference_final(
            d.pop("trace_reference_final", UNSET)
        )

        def _parse_payment_info(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payment_info = _parse_payment_info(d.pop("payment_info", UNSET))

        _return_code = d.pop("return_code", UNSET)
        return_code: TransactionDataICLReturnCode | Unset
        if isinstance(_return_code, Unset):
            return_code = UNSET
        else:
            return_code = TransactionDataICLReturnCode(_return_code)

        transaction_data_icl = cls(
            file_create_date_time=file_create_date_time,
            amount=amount,
            origin_routing_number=origin_routing_number,
            origin_routing_name=origin_routing_name,
            origin_account_number=origin_account_number,
            origin_account_name=origin_account_name,
            destination_routing_number=destination_routing_number,
            destination_routing_name=destination_routing_name,
            destination_account_number=destination_account_number,
            destination_account_name=destination_account_name,
            origin_routing_number_virtual=origin_routing_number_virtual,
            origin_account_number_virtual=origin_account_number_virtual,
            destination_routing_number_virtual=destination_routing_number_virtual,
            destination_account_number_virtual=destination_account_number_virtual,
            has_virtual_origin=has_virtual_origin,
            has_virtual_destination=has_virtual_destination,
            type_=type_,
            transfer_key=transfer_key,
            transfer_type=transfer_type,
            transfer_code=transfer_code,
            reference=reference,
            trace_reference=trace_reference,
            trace_reference_original=trace_reference_original,
            trace_reference_final=trace_reference_final,
            payment_info=payment_info,
            return_code=return_code,
        )

        transaction_data_icl.additional_properties = d
        return transaction_data_icl

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
