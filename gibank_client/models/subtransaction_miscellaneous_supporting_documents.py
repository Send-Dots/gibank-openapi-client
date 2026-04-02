from __future__ import annotations

from collections.abc import Mapping
from typing import Any
from typing import TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.subtransaction_miscellaneous_supporting_documents_category import (
    SubtransactionMiscellaneousSupportingDocumentsCategory,
)
from ..models.subtransaction_miscellaneous_supporting_documents_type import (
    SubtransactionMiscellaneousSupportingDocumentsType,
)

T = TypeVar("T", bound="SubtransactionMiscellaneousSupportingDocuments")


@_attrs_define
class SubtransactionMiscellaneousSupportingDocuments:
    """Subtransaction - Miscellaneous Supporting Documents

    Attributes:
        category (SubtransactionMiscellaneousSupportingDocumentsCategory): Subtransaction - Miscellaneous Supporting
            Documents
        type_ (SubtransactionMiscellaneousSupportingDocumentsType): The specific type of miscellaneous supporting
            document used for a Subtransaction. Possible values include:

            - `correspondence` - Email/letter/chat correspondence referencing the transaction
            - `internal_memo` - Explanation by compliance or operations
    """

    category: SubtransactionMiscellaneousSupportingDocumentsCategory
    type_: SubtransactionMiscellaneousSupportingDocumentsType
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
        category = SubtransactionMiscellaneousSupportingDocumentsCategory(
            d.pop("category")
        )

        type_ = SubtransactionMiscellaneousSupportingDocumentsType(d.pop("type"))

        subtransaction_miscellaneous_supporting_documents = cls(
            category=category,
            type_=type_,
        )

        subtransaction_miscellaneous_supporting_documents.additional_properties = d
        return subtransaction_miscellaneous_supporting_documents

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
