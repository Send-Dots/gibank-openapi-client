from __future__ import annotations

from collections.abc import Mapping
from typing import Any
from typing import TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.business_address_verification_category import (
    BusinessAddressVerificationCategory,
)
from ..models.business_address_verification_type import BusinessAddressVerificationType

T = TypeVar("T", bound="BusinessAddressVerification")


@_attrs_define
class BusinessAddressVerification:
    """Subclient - Business - Address Verification

    Attributes:
        category (BusinessAddressVerificationCategory): Business - Address Verification
        type_ (BusinessAddressVerificationType): The specific type of document or verification method used for business
            address verification. Possible values include:

            - `vendor_output` - Third-party verification result of the business address (**Text input only**)
            - `water_bill` - Utility bill showing the business address (**Document upload only**)
            - `lease_agreement` - Official document showing the business's leased premises (**Document upload only**)
            - `bank_statement` - Official bank document showing the business address (**Document upload only**)
            - `credit_card_statement` - Official credit card document showing the business address (**Document upload
            only**)
            - `irs_tax_return` - Official tax document filed by a business, which includes the business address (**Document
            upload only**)
            - `irs_ein_verification_letter` - Official IRS letter confirming a business's address (**Document upload only**)
            - `articles_of_incorporation` - Official document filed with a government body, including the business address
            (**Document upload only**)
            - `certificate_of_formation` - Legal document used to form an LLC, including the business address (**Document
            upload only**)
            - `other` - Any other document type that verifies the business address (**Document upload only**)
    """

    category: BusinessAddressVerificationCategory
    type_: BusinessAddressVerificationType
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
        category = BusinessAddressVerificationCategory(d.pop("category"))

        type_ = BusinessAddressVerificationType(d.pop("type"))

        business_address_verification = cls(
            category=category,
            type_=type_,
        )

        business_address_verification.additional_properties = d
        return business_address_verification

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
