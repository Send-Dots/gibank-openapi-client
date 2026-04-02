from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any
from typing import TypeVar
from typing import cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="TransactionDataShared")


@_attrs_define
class TransactionDataShared:
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

        transaction_data_shared = cls(
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
        )

        transaction_data_shared.additional_properties = d
        return transaction_data_shared

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
