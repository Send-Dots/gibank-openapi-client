from __future__ import annotations

from collections.abc import Mapping
from typing import Any
from typing import TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.business_dba_registration_category import BusinessDBARegistrationCategory
from ..models.business_dba_registration_type import BusinessDBARegistrationType

T = TypeVar("T", bound="BusinessDBARegistration")


@_attrs_define
class BusinessDBARegistration:
    """Subclient - Business - DBA Registration

    Attributes:
        category (BusinessDBARegistrationCategory): Business - DBA Registration
        type_ (BusinessDBARegistrationType): The specific type of document used for business DBA (Doing Business As)
            registration. Possible values include:

            - `certificate_of_assumed_name` - Official document certifying a business is operating under a name different
            from its legal name (**Document upload only**)
            - `certificate_of_trade_name` - Document registering a business's trade name with the appropriate government
            agency (**Document upload only**)
            - `dba_certificate` - Certificate issued by a government agency allowing a business to operate under a 'doing
            business as' name (**Document upload only**)
            - `business_license` - Government-issued document allowing a business to operate within a particular
            jurisdiction (**Document upload only**)
            - `business_permit` - Official permission granted by a government entity to a business for specific activities
            (**Document upload only**)
            - `dba_registration_confirmation_letter` - Official letter confirming the registration of a 'doing business as'
            name (**Document upload only**)
    """

    category: BusinessDBARegistrationCategory
    type_: BusinessDBARegistrationType
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
        category = BusinessDBARegistrationCategory(d.pop("category"))

        type_ = BusinessDBARegistrationType(d.pop("type"))

        business_dba_registration = cls(
            category=category,
            type_=type_,
        )

        business_dba_registration.additional_properties = d
        return business_dba_registration

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
