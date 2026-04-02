from __future__ import annotations

from collections.abc import Mapping
from typing import Any
from typing import TypeVar
from typing import cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="SubtransactionUpdate")


@_attrs_define
class SubtransactionUpdate:
    """
    Example:
        {'deleted': True}

    Attributes:
        transaction_id (int | None | Unset): The ID of the associated transaction. If you need more, please use the
            dedicated `link` endpoints. The value is not returned. Example: 1.
        deleted (bool | Unset): Indicates if the subtransaction is deleted
    """

    transaction_id: int | None | Unset = UNSET
    deleted: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        transaction_id: int | None | Unset
        if isinstance(self.transaction_id, Unset):
            transaction_id = UNSET
        else:
            transaction_id = self.transaction_id

        deleted = self.deleted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if transaction_id is not UNSET:
            field_dict["transaction_id"] = transaction_id
        if deleted is not UNSET:
            field_dict["deleted"] = deleted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_transaction_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        transaction_id = _parse_transaction_id(d.pop("transaction_id", UNSET))

        deleted = d.pop("deleted", UNSET)

        subtransaction_update = cls(
            transaction_id=transaction_id,
            deleted=deleted,
        )

        subtransaction_update.additional_properties = d
        return subtransaction_update

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
