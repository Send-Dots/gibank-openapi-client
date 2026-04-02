from __future__ import annotations

from collections.abc import Mapping
from typing import Any
from typing import TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.business_name_verification_category import (
    BusinessNameVerificationCategory,
)
from ..models.business_name_verification_type import BusinessNameVerificationType

T = TypeVar("T", bound="BusinessNameVerification")


@_attrs_define
class BusinessNameVerification:
    """Subclient - Business - Name Verification

    Attributes:
        category (BusinessNameVerificationCategory): Business - Name Verification
        type_ (BusinessNameVerificationType): The specific type of document or verification method used for business
            name verification. Possible values include:

            - `articles_of_incorporation` - Official document filed with a government body to legally document the creation
            of a corporation (**Document upload only**)
            - `certificate_of_formation` - Legal document used to form a limited liability company (LLC) in some states
            (**Document upload only**)
            - `articles_of_organization` - Document filed to form an LLC, similar to articles of incorporation for
            corporations (**Document upload only**)
            - `state_certificate_of_good_standing` - Official document proving a business entity is compliant with state
            regulations (**Document upload only**)
            - `irs_ein_verification_letter` - Official IRS letter confirming a business's Employer Identification Number
            (**Document upload only**)
            - `business_license` - Government-issued document allowing a business to operate within a particular
            jurisdiction (**Document upload only**)
            - `business_tax_return` - Official tax document filed by a business to report income, losses, and other
            financial information (**Document upload only**)
            - `other` - Any other document type that verifies the business name (**Document upload only**)
    """

    category: BusinessNameVerificationCategory
    type_: BusinessNameVerificationType
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
        category = BusinessNameVerificationCategory(d.pop("category"))

        type_ = BusinessNameVerificationType(d.pop("type"))

        business_name_verification = cls(
            category=category,
            type_=type_,
        )

        business_name_verification.additional_properties = d
        return business_name_verification

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
