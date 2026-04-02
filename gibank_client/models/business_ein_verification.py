from __future__ import annotations

from collections.abc import Mapping
from typing import Any
from typing import TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.business_ein_verification_category import BusinessEINVerificationCategory
from ..models.business_ein_verification_type import BusinessEINVerificationType

T = TypeVar("T", bound="BusinessEINVerification")


@_attrs_define
class BusinessEINVerification:
    """Subclient - Business - EIN Verification

    Attributes:
        category (BusinessEINVerificationCategory): Business - EIN Verification
        type_ (BusinessEINVerificationType): The specific type of document or verification method used for business EIN
            verification. Possible values include:

            - `vendor_output` - Third-party verification result of the business EIN (**Text input only**)
            - `irs_ein_verification_letter` - Official IRS letter confirming a business's Employer Identification Number
            (**Document upload only**)
            - `irs_tax_return` - Official tax document filed by a business, which includes the EIN (**Document upload
            only**)
            - `irs_form_w9` - Request for Taxpayer Identification Number and Certification form (**Document upload only**)
            - `irs_form_ss4` - Application for Employer Identification Number form (**Document upload only**)
            - `other` - Any other document type that verifies the business EIN (**Document upload only**)
    """

    category: BusinessEINVerificationCategory
    type_: BusinessEINVerificationType
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
        category = BusinessEINVerificationCategory(d.pop("category"))

        type_ = BusinessEINVerificationType(d.pop("type"))

        business_ein_verification = cls(
            category=category,
            type_=type_,
        )

        business_ein_verification.additional_properties = d
        return business_ein_verification

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
