from __future__ import annotations

from collections.abc import Mapping
from typing import Any
from typing import TypeVar
from typing import cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="CreateTransactionReturnBody")


@_attrs_define
class CreateTransactionReturnBody:
    """
    Attributes:
        return_code (str | Unset): The transaction return code. Read more here: [Returns](docs/services/transactions-
            ach.html#returns)
             Example: R01.
        return_info (None | str | Unset): The (free text) return info Example: Insufficient Funds.
        simulate (bool | None | Unset): Indicates if it's only a simulation or if the transaction must be stored
            permanently. If True, returned IDs are set to `-1`. Example: True.
        external_key (str | Unset): External key of the batch Example: ABC123456789.
    """

    return_code: str | Unset = UNSET
    return_info: None | str | Unset = UNSET
    simulate: bool | None | Unset = UNSET
    external_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return_code = self.return_code

        return_info: None | str | Unset
        if isinstance(self.return_info, Unset):
            return_info = UNSET
        else:
            return_info = self.return_info

        simulate: bool | None | Unset
        if isinstance(self.simulate, Unset):
            simulate = UNSET
        else:
            simulate = self.simulate

        external_key = self.external_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if return_code is not UNSET:
            field_dict["return_code"] = return_code
        if return_info is not UNSET:
            field_dict["return_info"] = return_info
        if simulate is not UNSET:
            field_dict["simulate"] = simulate
        if external_key is not UNSET:
            field_dict["external_key"] = external_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        return_code = d.pop("return_code", UNSET)

        def _parse_return_info(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        return_info = _parse_return_info(d.pop("return_info", UNSET))

        def _parse_simulate(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        simulate = _parse_simulate(d.pop("simulate", UNSET))

        external_key = d.pop("external_key", UNSET)

        create_transaction_return_body = cls(
            return_code=return_code,
            return_info=return_info,
            simulate=simulate,
            external_key=external_key,
        )

        create_transaction_return_body.additional_properties = d
        return create_transaction_return_body

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
