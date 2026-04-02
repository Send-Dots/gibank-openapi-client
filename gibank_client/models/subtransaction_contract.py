from __future__ import annotations

from collections.abc import Mapping
from typing import Any
from typing import TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.subtransaction_contract_category import SubtransactionContractCategory
from ..models.subtransaction_contract_type import SubtransactionContractType

T = TypeVar("T", bound="SubtransactionContract")


@_attrs_define
class SubtransactionContract:
    """Subtransaction - Contract

    Attributes:
        category (SubtransactionContractCategory): Subtransaction - Contract
        type_ (SubtransactionContractType): The specific type of contract used for a Subtransaction. Possible values
            include:

            - `sales_contract` - Legal agreement for sale of goods/services
            - `purchase_order` - Issued by a buyer to confirm purchase intent
            - `service_agreement` - Recurring service relationship (e.g., SaaS contract, consulting)
    """

    category: SubtransactionContractCategory
    type_: SubtransactionContractType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category.value

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category = SubtransactionContractCategory(d.pop("category"))

        type_ = SubtransactionContractType(d.pop("type"))

        subtransaction_contract = cls(
            category=category,
            type_=type_,
        )

        subtransaction_contract.additional_properties = d
        return subtransaction_contract

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
