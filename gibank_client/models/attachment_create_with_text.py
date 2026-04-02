from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING
from typing import Any
from typing import TypeVar
from typing import cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET
from ..types import Unset

if TYPE_CHECKING:
    from ..models.business_address_verification import BusinessAddressVerification
    from ..models.business_dba_registration import BusinessDBARegistration
    from ..models.business_ein import BusinessEIN
    from ..models.business_ein_verification import BusinessEINVerification
    from ..models.business_name_verification import BusinessNameVerification
    from ..models.business_ownership_structure_verification import (
        BusinessOwnershipStructureVerification,
    )
    from ..models.business_screening import BusinessScreening
    from ..models.natural_person_address_verification import (
        NaturalPersonAddressVerification,
    )
    from ..models.natural_person_date_of_birth import NaturalPersonDateOfBirth
    from ..models.natural_person_identification import NaturalPersonIdentification
    from ..models.natural_person_identification_number import (
        NaturalPersonIdentificationNumber,
    )
    from ..models.natural_person_screening import NaturalPersonScreening
    from ..models.natural_person_source_of_wealth_or_funds import (
        NaturalPersonSourceOfWealthOrFunds,
    )
    from ..models.other import Other
    from ..models.subtransaction_contract import SubtransactionContract
    from ..models.subtransaction_invoice import SubtransactionInvoice
    from ..models.subtransaction_miscellaneous_supporting_documents import (
        SubtransactionMiscellaneousSupportingDocuments,
    )
    from ..models.subtransaction_quote_estimate import SubtransactionQuoteEstimate
    from ..models.ubo_control_prong_confirmation import UBOControlProngConfirmation
    from ..models.ubo_date_of_birth import UBODateOfBirth
    from ..models.ubo_identification import UBOIdentification
    from ..models.ubo_identification_number import UBOIdentificationNumber
    from ..models.ubo_ownership_prong_confirmation import UBOOwnershipProngConfirmation
    from ..models.ubo_screening import UBOScreening
    from ..models.uncategorized import Uncategorized


T = TypeVar("T", bound="AttachmentCreateWithText")


@_attrs_define
class AttachmentCreateWithText:
    """Payload for creating a text-based attachment.

    Example:
        {'category_and_type': {'category': 'natural_person_identification_number', 'type': 'ssn'}, 'description': "John
            Doe's SSN (Masked Text)", 'active': True, 'text_value': 'XXX-XX-1234'}

    Attributes:
        category_and_type (BusinessAddressVerification | BusinessDBARegistration | BusinessEIN | BusinessEINVerification
            | BusinessNameVerification | BusinessOwnershipStructureVerification | BusinessScreening |
            NaturalPersonAddressVerification | NaturalPersonDateOfBirth | NaturalPersonIdentification |
            NaturalPersonIdentificationNumber | NaturalPersonScreening | NaturalPersonSourceOfWealthOrFunds | Other |
            SubtransactionContract | SubtransactionInvoice | SubtransactionMiscellaneousSupportingDocuments |
            SubtransactionQuoteEstimate | UBOControlProngConfirmation | UBODateOfBirth | UBOIdentification |
            UBOIdentificationNumber | UBOOwnershipProngConfirmation | UBOScreening | Uncategorized):
        text_value (None | str): The text value of the attachment Example: 123456789.
        category_variation (None | str | Unset): The variation of the category (if the category is `other`) Example:
            passport.
        type_variation (None | str | Unset): The variation of the type (if the type is `other`) Example: pdf.
        description (None | str | Unset): A description of the attachment Example: User's passport scan.
        active (bool | Unset): Indicates if the attachment is active Example: True.
        language_alpha_3_code (None | str | Unset): The ISO 639-2 code for the lanuage the document is in Example: eng.
    """

    category_and_type: (
        BusinessAddressVerification
        | BusinessDBARegistration
        | BusinessEIN
        | BusinessEINVerification
        | BusinessNameVerification
        | BusinessOwnershipStructureVerification
        | BusinessScreening
        | NaturalPersonAddressVerification
        | NaturalPersonDateOfBirth
        | NaturalPersonIdentification
        | NaturalPersonIdentificationNumber
        | NaturalPersonScreening
        | NaturalPersonSourceOfWealthOrFunds
        | Other
        | SubtransactionContract
        | SubtransactionInvoice
        | SubtransactionMiscellaneousSupportingDocuments
        | SubtransactionQuoteEstimate
        | UBOControlProngConfirmation
        | UBODateOfBirth
        | UBOIdentification
        | UBOIdentificationNumber
        | UBOOwnershipProngConfirmation
        | UBOScreening
        | Uncategorized
    )
    text_value: None | str
    category_variation: None | str | Unset = UNSET
    type_variation: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    active: bool | Unset = UNSET
    language_alpha_3_code: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.business_address_verification import BusinessAddressVerification
        from ..models.business_dba_registration import BusinessDBARegistration
        from ..models.business_ein import BusinessEIN
        from ..models.business_ein_verification import BusinessEINVerification
        from ..models.business_name_verification import BusinessNameVerification
        from ..models.business_ownership_structure_verification import (
            BusinessOwnershipStructureVerification,
        )
        from ..models.business_screening import BusinessScreening
        from ..models.natural_person_address_verification import (
            NaturalPersonAddressVerification,
        )
        from ..models.natural_person_date_of_birth import NaturalPersonDateOfBirth
        from ..models.natural_person_identification import NaturalPersonIdentification
        from ..models.natural_person_identification_number import (
            NaturalPersonIdentificationNumber,
        )
        from ..models.natural_person_screening import NaturalPersonScreening
        from ..models.natural_person_source_of_wealth_or_funds import (
            NaturalPersonSourceOfWealthOrFunds,
        )
        from ..models.other import Other
        from ..models.subtransaction_contract import SubtransactionContract
        from ..models.subtransaction_invoice import SubtransactionInvoice
        from ..models.subtransaction_miscellaneous_supporting_documents import (
            SubtransactionMiscellaneousSupportingDocuments,
        )
        from ..models.subtransaction_quote_estimate import SubtransactionQuoteEstimate
        from ..models.ubo_control_prong_confirmation import UBOControlProngConfirmation
        from ..models.ubo_date_of_birth import UBODateOfBirth
        from ..models.ubo_identification import UBOIdentification
        from ..models.ubo_identification_number import UBOIdentificationNumber
        from ..models.ubo_ownership_prong_confirmation import (
            UBOOwnershipProngConfirmation,
        )
        from ..models.ubo_screening import UBOScreening

        category_and_type: dict[str, Any]
        if isinstance(self.category_and_type, BusinessNameVerification):
            category_and_type = self.category_and_type.to_dict()
        elif isinstance(self.category_and_type, BusinessEINVerification):
            category_and_type = self.category_and_type.to_dict()
        elif isinstance(self.category_and_type, BusinessAddressVerification):
            category_and_type = self.category_and_type.to_dict()
        elif isinstance(self.category_and_type, BusinessOwnershipStructureVerification):
            category_and_type = self.category_and_type.to_dict()
        elif isinstance(self.category_and_type, NaturalPersonIdentification):
            category_and_type = self.category_and_type.to_dict()
        elif isinstance(self.category_and_type, NaturalPersonAddressVerification):
            category_and_type = self.category_and_type.to_dict()
        elif isinstance(self.category_and_type, NaturalPersonDateOfBirth):
            category_and_type = self.category_and_type.to_dict()
        elif isinstance(self.category_and_type, NaturalPersonScreening):
            category_and_type = self.category_and_type.to_dict()
        elif isinstance(self.category_and_type, NaturalPersonIdentificationNumber):
            category_and_type = self.category_and_type.to_dict()
        elif isinstance(self.category_and_type, NaturalPersonSourceOfWealthOrFunds):
            category_and_type = self.category_and_type.to_dict()
        elif isinstance(self.category_and_type, BusinessDBARegistration):
            category_and_type = self.category_and_type.to_dict()
        elif isinstance(self.category_and_type, BusinessEIN):
            category_and_type = self.category_and_type.to_dict()
        elif isinstance(self.category_and_type, BusinessScreening):
            category_and_type = self.category_and_type.to_dict()
        elif isinstance(self.category_and_type, UBOControlProngConfirmation):
            category_and_type = self.category_and_type.to_dict()
        elif isinstance(self.category_and_type, UBOOwnershipProngConfirmation):
            category_and_type = self.category_and_type.to_dict()
        elif isinstance(self.category_and_type, UBOIdentification):
            category_and_type = self.category_and_type.to_dict()
        elif isinstance(self.category_and_type, UBODateOfBirth):
            category_and_type = self.category_and_type.to_dict()
        elif isinstance(self.category_and_type, UBOScreening):
            category_and_type = self.category_and_type.to_dict()
        elif isinstance(self.category_and_type, UBOIdentificationNumber):
            category_and_type = self.category_and_type.to_dict()
        elif isinstance(self.category_and_type, SubtransactionInvoice):
            category_and_type = self.category_and_type.to_dict()
        elif isinstance(self.category_and_type, SubtransactionContract):
            category_and_type = self.category_and_type.to_dict()
        elif isinstance(self.category_and_type, SubtransactionQuoteEstimate):
            category_and_type = self.category_and_type.to_dict()
        elif isinstance(
            self.category_and_type, SubtransactionMiscellaneousSupportingDocuments
        ):
            category_and_type = self.category_and_type.to_dict()
        elif isinstance(self.category_and_type, Other):
            category_and_type = self.category_and_type.to_dict()
        else:
            category_and_type = self.category_and_type.to_dict()

        text_value: None | str
        text_value = self.text_value

        category_variation: None | str | Unset
        if isinstance(self.category_variation, Unset):
            category_variation = UNSET
        else:
            category_variation = self.category_variation

        type_variation: None | str | Unset
        if isinstance(self.type_variation, Unset):
            type_variation = UNSET
        else:
            type_variation = self.type_variation

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        active = self.active

        language_alpha_3_code: None | str | Unset
        if isinstance(self.language_alpha_3_code, Unset):
            language_alpha_3_code = UNSET
        else:
            language_alpha_3_code = self.language_alpha_3_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category_and_type": category_and_type,
                "text_value": text_value,
            }
        )
        if category_variation is not UNSET:
            field_dict["category_variation"] = category_variation
        if type_variation is not UNSET:
            field_dict["type_variation"] = type_variation
        if description is not UNSET:
            field_dict["description"] = description
        if active is not UNSET:
            field_dict["active"] = active
        if language_alpha_3_code is not UNSET:
            field_dict["language_alpha_3_code"] = language_alpha_3_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.business_address_verification import BusinessAddressVerification
        from ..models.business_dba_registration import BusinessDBARegistration
        from ..models.business_ein import BusinessEIN
        from ..models.business_ein_verification import BusinessEINVerification
        from ..models.business_name_verification import BusinessNameVerification
        from ..models.business_ownership_structure_verification import (
            BusinessOwnershipStructureVerification,
        )
        from ..models.business_screening import BusinessScreening
        from ..models.natural_person_address_verification import (
            NaturalPersonAddressVerification,
        )
        from ..models.natural_person_date_of_birth import NaturalPersonDateOfBirth
        from ..models.natural_person_identification import NaturalPersonIdentification
        from ..models.natural_person_identification_number import (
            NaturalPersonIdentificationNumber,
        )
        from ..models.natural_person_screening import NaturalPersonScreening
        from ..models.natural_person_source_of_wealth_or_funds import (
            NaturalPersonSourceOfWealthOrFunds,
        )
        from ..models.other import Other
        from ..models.subtransaction_contract import SubtransactionContract
        from ..models.subtransaction_invoice import SubtransactionInvoice
        from ..models.subtransaction_miscellaneous_supporting_documents import (
            SubtransactionMiscellaneousSupportingDocuments,
        )
        from ..models.subtransaction_quote_estimate import SubtransactionQuoteEstimate
        from ..models.ubo_control_prong_confirmation import UBOControlProngConfirmation
        from ..models.ubo_date_of_birth import UBODateOfBirth
        from ..models.ubo_identification import UBOIdentification
        from ..models.ubo_identification_number import UBOIdentificationNumber
        from ..models.ubo_ownership_prong_confirmation import (
            UBOOwnershipProngConfirmation,
        )
        from ..models.ubo_screening import UBOScreening
        from ..models.uncategorized import Uncategorized

        d = dict(src_dict)

        def _parse_category_and_type(
            data: object,
        ) -> (
            BusinessAddressVerification
            | BusinessDBARegistration
            | BusinessEIN
            | BusinessEINVerification
            | BusinessNameVerification
            | BusinessOwnershipStructureVerification
            | BusinessScreening
            | NaturalPersonAddressVerification
            | NaturalPersonDateOfBirth
            | NaturalPersonIdentification
            | NaturalPersonIdentificationNumber
            | NaturalPersonScreening
            | NaturalPersonSourceOfWealthOrFunds
            | Other
            | SubtransactionContract
            | SubtransactionInvoice
            | SubtransactionMiscellaneousSupportingDocuments
            | SubtransactionQuoteEstimate
            | UBOControlProngConfirmation
            | UBODateOfBirth
            | UBOIdentification
            | UBOIdentificationNumber
            | UBOOwnershipProngConfirmation
            | UBOScreening
            | Uncategorized
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_category_and_type_type_0 = (
                    BusinessNameVerification.from_dict(data)
                )

                return componentsschemas_category_and_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_category_and_type_type_1 = (
                    BusinessEINVerification.from_dict(data)
                )

                return componentsschemas_category_and_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_category_and_type_type_2 = (
                    BusinessAddressVerification.from_dict(data)
                )

                return componentsschemas_category_and_type_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_category_and_type_type_3 = (
                    BusinessOwnershipStructureVerification.from_dict(data)
                )

                return componentsschemas_category_and_type_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_category_and_type_type_4 = (
                    NaturalPersonIdentification.from_dict(data)
                )

                return componentsschemas_category_and_type_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_category_and_type_type_5 = (
                    NaturalPersonAddressVerification.from_dict(data)
                )

                return componentsschemas_category_and_type_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_category_and_type_type_6 = (
                    NaturalPersonDateOfBirth.from_dict(data)
                )

                return componentsschemas_category_and_type_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_category_and_type_type_7 = (
                    NaturalPersonScreening.from_dict(data)
                )

                return componentsschemas_category_and_type_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_category_and_type_type_8 = (
                    NaturalPersonIdentificationNumber.from_dict(data)
                )

                return componentsschemas_category_and_type_type_8
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_category_and_type_type_9 = (
                    NaturalPersonSourceOfWealthOrFunds.from_dict(data)
                )

                return componentsschemas_category_and_type_type_9
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_category_and_type_type_10 = (
                    BusinessDBARegistration.from_dict(data)
                )

                return componentsschemas_category_and_type_type_10
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_category_and_type_type_11 = BusinessEIN.from_dict(
                    data
                )

                return componentsschemas_category_and_type_type_11
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_category_and_type_type_12 = (
                    BusinessScreening.from_dict(data)
                )

                return componentsschemas_category_and_type_type_12
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_category_and_type_type_13 = (
                    UBOControlProngConfirmation.from_dict(data)
                )

                return componentsschemas_category_and_type_type_13
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_category_and_type_type_14 = (
                    UBOOwnershipProngConfirmation.from_dict(data)
                )

                return componentsschemas_category_and_type_type_14
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_category_and_type_type_15 = (
                    UBOIdentification.from_dict(data)
                )

                return componentsschemas_category_and_type_type_15
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_category_and_type_type_16 = UBODateOfBirth.from_dict(
                    data
                )

                return componentsschemas_category_and_type_type_16
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_category_and_type_type_17 = UBOScreening.from_dict(
                    data
                )

                return componentsschemas_category_and_type_type_17
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_category_and_type_type_18 = (
                    UBOIdentificationNumber.from_dict(data)
                )

                return componentsschemas_category_and_type_type_18
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_category_and_type_type_19 = (
                    SubtransactionInvoice.from_dict(data)
                )

                return componentsschemas_category_and_type_type_19
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_category_and_type_type_20 = (
                    SubtransactionContract.from_dict(data)
                )

                return componentsschemas_category_and_type_type_20
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_category_and_type_type_21 = (
                    SubtransactionQuoteEstimate.from_dict(data)
                )

                return componentsschemas_category_and_type_type_21
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_category_and_type_type_22 = (
                    SubtransactionMiscellaneousSupportingDocuments.from_dict(data)
                )

                return componentsschemas_category_and_type_type_22
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_category_and_type_type_23 = Other.from_dict(data)

                return componentsschemas_category_and_type_type_23
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_category_and_type_type_24 = Uncategorized.from_dict(data)

            return componentsschemas_category_and_type_type_24

        category_and_type = _parse_category_and_type(d.pop("category_and_type"))

        def _parse_text_value(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        text_value = _parse_text_value(d.pop("text_value"))

        def _parse_category_variation(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category_variation = _parse_category_variation(
            d.pop("category_variation", UNSET)
        )

        def _parse_type_variation(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_variation = _parse_type_variation(d.pop("type_variation", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        active = d.pop("active", UNSET)

        def _parse_language_alpha_3_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        language_alpha_3_code = _parse_language_alpha_3_code(
            d.pop("language_alpha_3_code", UNSET)
        )

        attachment_create_with_text = cls(
            category_and_type=category_and_type,
            text_value=text_value,
            category_variation=category_variation,
            type_variation=type_variation,
            description=description,
            active=active,
            language_alpha_3_code=language_alpha_3_code,
        )

        attachment_create_with_text.additional_properties = d
        return attachment_create_with_text

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
