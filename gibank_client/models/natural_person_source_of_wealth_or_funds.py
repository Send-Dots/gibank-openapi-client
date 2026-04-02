from __future__ import annotations

from collections.abc import Mapping
from typing import Any
from typing import TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.natural_person_source_of_wealth_or_funds_category import (
    NaturalPersonSourceOfWealthOrFundsCategory,
)
from ..models.natural_person_source_of_wealth_or_funds_type import (
    NaturalPersonSourceOfWealthOrFundsType,
)

T = TypeVar("T", bound="NaturalPersonSourceOfWealthOrFunds")


@_attrs_define
class NaturalPersonSourceOfWealthOrFunds:
    """Subclient - Natural Person - Source of Wealth or Funds

    Attributes:
        category (NaturalPersonSourceOfWealthOrFundsCategory): Natural Person - Source of Wealth or Funds
        type_ (NaturalPersonSourceOfWealthOrFundsType): The specific type of document used to verify a natural person's
            source of wealt or funds. Possible values include:

            - `payslip` - Document showing a person's salary and deductions from an employer (**Document upload only**)
            - `employment_contract` - Legal agreement between an employer and employee (**Document upload only**)
            - `bank_statement` - Official record of financial transactions in a person's bank account (**Document upload
            only**)
            - `investment_account_statements` - Documents showing the performance and holdings in investment accounts
            (**Document upload only**)
            - `tax_return` - Official document filed with a tax authority to report income, expenses, and other tax-related
            information (**Document upload only**)
    """

    category: NaturalPersonSourceOfWealthOrFundsCategory
    type_: NaturalPersonSourceOfWealthOrFundsType
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
        category = NaturalPersonSourceOfWealthOrFundsCategory(d.pop("category"))

        type_ = NaturalPersonSourceOfWealthOrFundsType(d.pop("type"))

        natural_person_source_of_wealth_or_funds = cls(
            category=category,
            type_=type_,
        )

        natural_person_source_of_wealth_or_funds.additional_properties = d
        return natural_person_source_of_wealth_or_funds

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
