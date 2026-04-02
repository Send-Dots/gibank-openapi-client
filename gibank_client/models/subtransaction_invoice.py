from __future__ import annotations

from collections.abc import Mapping
from typing import Any
from typing import TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.subtransaction_invoice_category import SubtransactionInvoiceCategory
from ..models.subtransaction_invoice_type import SubtransactionInvoiceType

T = TypeVar("T", bound="SubtransactionInvoice")


@_attrs_define
class SubtransactionInvoice:
    """Subtransaction - Invoice

    Attributes:
        category (SubtransactionInvoiceCategory): Subtransaction - Invoice
        type_ (SubtransactionInvoiceType): The specific type of invoice used for a Subtransaction. Possible values
            include:

            - `customer_invoice` - Invoice issued to the end customer
            - `supplier_invoice` - Invoice from a vendor or supplier
            - `proforma_invoice` - Preliminary invoice/quotation used to justify advance payments
    """

    category: SubtransactionInvoiceCategory
    type_: SubtransactionInvoiceType
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
        category = SubtransactionInvoiceCategory(d.pop("category"))

        type_ = SubtransactionInvoiceType(d.pop("type"))

        subtransaction_invoice = cls(
            category=category,
            type_=type_,
        )

        subtransaction_invoice.additional_properties = d
        return subtransaction_invoice

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
