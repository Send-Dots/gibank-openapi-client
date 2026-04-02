from __future__ import annotations

from collections.abc import Mapping
from typing import Any
from typing import TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.natural_person_address_verification_category import (
    NaturalPersonAddressVerificationCategory,
)
from ..models.natural_person_address_verification_type import (
    NaturalPersonAddressVerificationType,
)

T = TypeVar("T", bound="NaturalPersonAddressVerification")


@_attrs_define
class NaturalPersonAddressVerification:
    """Subclient - Natural Person - Address Verification

    Attributes:
        category (NaturalPersonAddressVerificationCategory): Natural Person - Address Verification
        type_ (NaturalPersonAddressVerificationType): The specific type of document or verification method used for
            natural person address verification. Possible values include:

            - `vendor_output` - Third-party verification result of the person's address (**Text input only**)
            - `water_bill` - Utility bill showing the person's address (**Document upload only**)
            - `lease_agreement` - Official document showing the person's leased premises (**Document upload only**)
            - `state_id_card` - Government-issued identification card showing the person's address (**Document upload
            only**)
            - `other` - Any other document type that verifies the person's address (**Document upload only**)
    """

    category: NaturalPersonAddressVerificationCategory
    type_: NaturalPersonAddressVerificationType
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
        category = NaturalPersonAddressVerificationCategory(d.pop("category"))

        type_ = NaturalPersonAddressVerificationType(d.pop("type"))

        natural_person_address_verification = cls(
            category=category,
            type_=type_,
        )

        natural_person_address_verification.additional_properties = d
        return natural_person_address_verification

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
