from __future__ import annotations

from collections.abc import Mapping
from typing import Any
from typing import TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.subtransaction_quote_estimate_category import (
    SubtransactionQuoteEstimateCategory,
)
from ..models.subtransaction_quote_estimate_type import SubtransactionQuoteEstimateType

T = TypeVar("T", bound="SubtransactionQuoteEstimate")


@_attrs_define
class SubtransactionQuoteEstimate:
    """Subtransaction - Quote/Estimate

    Attributes:
        category (SubtransactionQuoteEstimateCategory): Subtransaction - Quote/Estimate
        type_ (SubtransactionQuoteEstimateType): The specific type of quote or estimate used for a Subtransaction.
            Possible values include:

            - `vendor_quote` - Formal price quote justifying expected payment
            - `work_order` - Instruction authorizing specific work
    """

    category: SubtransactionQuoteEstimateCategory
    type_: SubtransactionQuoteEstimateType
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
        category = SubtransactionQuoteEstimateCategory(d.pop("category"))

        type_ = SubtransactionQuoteEstimateType(d.pop("type"))

        subtransaction_quote_estimate = cls(
            category=category,
            type_=type_,
        )

        subtransaction_quote_estimate.additional_properties = d
        return subtransaction_quote_estimate

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
