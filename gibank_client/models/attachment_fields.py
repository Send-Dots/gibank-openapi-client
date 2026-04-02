from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING
from typing import Any
from typing import TypeVar
from typing import cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.attachment_fields_create_user_type import AttachmentFieldsCreateUserType
from ..models.attachment_fields_update_user_type import AttachmentFieldsUpdateUserType
from ..models.attachment_fields_url_malware_protection_status import (
    AttachmentFieldsUrlMalwareProtectionStatus,
)
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


T = TypeVar("T", bound="AttachmentFields")


@_attrs_define
class AttachmentFields:
    """
    Attributes:
        id (float | Unset): The attachment ID Example: 1.
        category_and_type (BusinessAddressVerification | BusinessDBARegistration | BusinessEIN | BusinessEINVerification
            | BusinessNameVerification | BusinessOwnershipStructureVerification | BusinessScreening |
            NaturalPersonAddressVerification | NaturalPersonDateOfBirth | NaturalPersonIdentification |
            NaturalPersonIdentificationNumber | NaturalPersonScreening | NaturalPersonSourceOfWealthOrFunds | Other |
            SubtransactionContract | SubtransactionInvoice | SubtransactionMiscellaneousSupportingDocuments |
            SubtransactionQuoteEstimate | UBOControlProngConfirmation | UBODateOfBirth | UBOIdentification |
            UBOIdentificationNumber | UBOOwnershipProngConfirmation | UBOScreening | Uncategorized | Unset):
        category_variation (None | str | Unset): The variation of the category (if the category is `other`) Example:
            passport.
        type_variation (None | str | Unset): The variation of the type (if the type is `other`) Example: pdf.
        description (None | str | Unset): A description of the attachment Example: User's passport scan.
        file_create_date_time (datetime.datetime | None | Unset): The date and time when the file was created (if
            applicable) (Stored as UTC, formatted as zero UTC offset (Zulu) format) Example: 2024-02-04T23:00:00.000Z.
        file_name_original (None | str | Unset): The original file name Example: passport_scan.pdf.
        file_extension (None | str | Unset): The file extension Example: pdf.
        text_value (None | str | Unset): The text value of the attachment Example: 123456789.
        active (bool | Unset): Indicates if the attachment is active Default: True. Example: True.
        language_id (float | None | Unset): The internal language ID (Not needed during creations/updates; feel free to
            use the ISO code) Example: 1.
        language_alpha_3_code (None | str | Unset): The ISO 639-2 code for the lanuage the document is in Example: eng.
        url (None | str | Unset): The URL to download the attachment (if applicable)
        url_malware_protection_status (AttachmentFieldsUrlMalwareProtectionStatus | Unset): The malware protection
            status of the file (if applicable)
        create_user_full_name (str | Unset): The full name of the create user Example: Max Mustermann.
        create_user_type (AttachmentFieldsCreateUserType | Unset): The type of the create user Example: client.
        update_user_full_name (str | Unset): The full name of the update user Example: Max Mustermann.
        update_user_type (AttachmentFieldsUpdateUserType | Unset): The type of the update user Example: client.
        create_date_time (datetime.datetime | Unset): The date and time when the attachment was created (Stored as UTC,
            formatted as zero UTC offset (Zulu) format) Example: 2024-02-04T23:00:00.000Z.
        update_date_time (datetime.datetime | Unset): The date and time when the attachment was last updated (Stored as
            UTC, formatted as zero UTC offset (Zulu) format) Example: 2024-02-04T23:00:00.000Z.
        create_user_id (float | Unset): The ID of the user who created the attachment Example: 1.
        update_user_id (float | Unset): The ID of the user who last updated the attachment Example: 1.
    """

    id: float | Unset = UNSET
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
        | Unset
    ) = UNSET
    category_variation: None | str | Unset = UNSET
    type_variation: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    file_create_date_time: datetime.datetime | None | Unset = UNSET
    file_name_original: None | str | Unset = UNSET
    file_extension: None | str | Unset = UNSET
    text_value: None | str | Unset = UNSET
    active: bool | Unset = True
    language_id: float | None | Unset = UNSET
    language_alpha_3_code: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    url_malware_protection_status: (
        AttachmentFieldsUrlMalwareProtectionStatus | Unset
    ) = UNSET
    create_user_full_name: str | Unset = UNSET
    create_user_type: AttachmentFieldsCreateUserType | Unset = UNSET
    update_user_full_name: str | Unset = UNSET
    update_user_type: AttachmentFieldsUpdateUserType | Unset = UNSET
    create_date_time: datetime.datetime | Unset = UNSET
    update_date_time: datetime.datetime | Unset = UNSET
    create_user_id: float | Unset = UNSET
    update_user_id: float | Unset = UNSET
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

        id = self.id

        category_and_type: dict[str, Any] | Unset
        if isinstance(self.category_and_type, Unset):
            category_and_type = UNSET
        elif isinstance(self.category_and_type, BusinessNameVerification):
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

        file_create_date_time: None | str | Unset
        if isinstance(self.file_create_date_time, Unset):
            file_create_date_time = UNSET
        elif isinstance(self.file_create_date_time, datetime.datetime):
            file_create_date_time = self.file_create_date_time.isoformat()
        else:
            file_create_date_time = self.file_create_date_time

        file_name_original: None | str | Unset
        if isinstance(self.file_name_original, Unset):
            file_name_original = UNSET
        else:
            file_name_original = self.file_name_original

        file_extension: None | str | Unset
        if isinstance(self.file_extension, Unset):
            file_extension = UNSET
        else:
            file_extension = self.file_extension

        text_value: None | str | Unset
        if isinstance(self.text_value, Unset):
            text_value = UNSET
        else:
            text_value = self.text_value

        active = self.active

        language_id: float | None | Unset
        if isinstance(self.language_id, Unset):
            language_id = UNSET
        else:
            language_id = self.language_id

        language_alpha_3_code: None | str | Unset
        if isinstance(self.language_alpha_3_code, Unset):
            language_alpha_3_code = UNSET
        else:
            language_alpha_3_code = self.language_alpha_3_code

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        url_malware_protection_status: str | Unset = UNSET
        if not isinstance(self.url_malware_protection_status, Unset):
            url_malware_protection_status = self.url_malware_protection_status.value

        create_user_full_name = self.create_user_full_name

        create_user_type: str | Unset = UNSET
        if not isinstance(self.create_user_type, Unset):
            create_user_type = self.create_user_type.value

        update_user_full_name = self.update_user_full_name

        update_user_type: str | Unset = UNSET
        if not isinstance(self.update_user_type, Unset):
            update_user_type = self.update_user_type.value

        create_date_time: str | Unset = UNSET
        if not isinstance(self.create_date_time, Unset):
            create_date_time = self.create_date_time.isoformat()

        update_date_time: str | Unset = UNSET
        if not isinstance(self.update_date_time, Unset):
            update_date_time = self.update_date_time.isoformat()

        create_user_id = self.create_user_id

        update_user_id = self.update_user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if category_and_type is not UNSET:
            field_dict["category_and_type"] = category_and_type
        if category_variation is not UNSET:
            field_dict["category_variation"] = category_variation
        if type_variation is not UNSET:
            field_dict["type_variation"] = type_variation
        if description is not UNSET:
            field_dict["description"] = description
        if file_create_date_time is not UNSET:
            field_dict["file_create_date_time"] = file_create_date_time
        if file_name_original is not UNSET:
            field_dict["file_name_original"] = file_name_original
        if file_extension is not UNSET:
            field_dict["file_extension"] = file_extension
        if text_value is not UNSET:
            field_dict["text_value"] = text_value
        if active is not UNSET:
            field_dict["active"] = active
        if language_id is not UNSET:
            field_dict["language_id"] = language_id
        if language_alpha_3_code is not UNSET:
            field_dict["language_alpha_3_code"] = language_alpha_3_code
        if url is not UNSET:
            field_dict["url"] = url
        if url_malware_protection_status is not UNSET:
            field_dict["url_malware_protection_status"] = url_malware_protection_status
        if create_user_full_name is not UNSET:
            field_dict["create_user_full_name"] = create_user_full_name
        if create_user_type is not UNSET:
            field_dict["create_user_type"] = create_user_type
        if update_user_full_name is not UNSET:
            field_dict["update_user_full_name"] = update_user_full_name
        if update_user_type is not UNSET:
            field_dict["update_user_type"] = update_user_type
        if create_date_time is not UNSET:
            field_dict["create_date_time"] = create_date_time
        if update_date_time is not UNSET:
            field_dict["update_date_time"] = update_date_time
        if create_user_id is not UNSET:
            field_dict["create_user_id"] = create_user_id
        if update_user_id is not UNSET:
            field_dict["update_user_id"] = update_user_id

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
        id = d.pop("id", UNSET)

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
            | Unset
        ):
            if isinstance(data, Unset):
                return data
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

        category_and_type = _parse_category_and_type(d.pop("category_and_type", UNSET))

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

        def _parse_file_create_date_time(
            data: object,
        ) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                file_create_date_time_type_0 = isoparse(data)

                return file_create_date_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        file_create_date_time = _parse_file_create_date_time(
            d.pop("file_create_date_time", UNSET)
        )

        def _parse_file_name_original(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_name_original = _parse_file_name_original(
            d.pop("file_name_original", UNSET)
        )

        def _parse_file_extension(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_extension = _parse_file_extension(d.pop("file_extension", UNSET))

        def _parse_text_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        text_value = _parse_text_value(d.pop("text_value", UNSET))

        active = d.pop("active", UNSET)

        def _parse_language_id(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        language_id = _parse_language_id(d.pop("language_id", UNSET))

        def _parse_language_alpha_3_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        language_alpha_3_code = _parse_language_alpha_3_code(
            d.pop("language_alpha_3_code", UNSET)
        )

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        _url_malware_protection_status = d.pop("url_malware_protection_status", UNSET)
        url_malware_protection_status: (
            AttachmentFieldsUrlMalwareProtectionStatus | Unset
        )
        if isinstance(_url_malware_protection_status, Unset):
            url_malware_protection_status = UNSET
        else:
            url_malware_protection_status = AttachmentFieldsUrlMalwareProtectionStatus(
                _url_malware_protection_status
            )

        create_user_full_name = d.pop("create_user_full_name", UNSET)

        _create_user_type = d.pop("create_user_type", UNSET)
        create_user_type: AttachmentFieldsCreateUserType | Unset
        if isinstance(_create_user_type, Unset):
            create_user_type = UNSET
        else:
            create_user_type = AttachmentFieldsCreateUserType(_create_user_type)

        update_user_full_name = d.pop("update_user_full_name", UNSET)

        _update_user_type = d.pop("update_user_type", UNSET)
        update_user_type: AttachmentFieldsUpdateUserType | Unset
        if isinstance(_update_user_type, Unset):
            update_user_type = UNSET
        else:
            update_user_type = AttachmentFieldsUpdateUserType(_update_user_type)

        _create_date_time = d.pop("create_date_time", UNSET)
        create_date_time: datetime.datetime | Unset
        if isinstance(_create_date_time, Unset):
            create_date_time = UNSET
        else:
            create_date_time = isoparse(_create_date_time)

        _update_date_time = d.pop("update_date_time", UNSET)
        update_date_time: datetime.datetime | Unset
        if isinstance(_update_date_time, Unset):
            update_date_time = UNSET
        else:
            update_date_time = isoparse(_update_date_time)

        create_user_id = d.pop("create_user_id", UNSET)

        update_user_id = d.pop("update_user_id", UNSET)

        attachment_fields = cls(
            id=id,
            category_and_type=category_and_type,
            category_variation=category_variation,
            type_variation=type_variation,
            description=description,
            file_create_date_time=file_create_date_time,
            file_name_original=file_name_original,
            file_extension=file_extension,
            text_value=text_value,
            active=active,
            language_id=language_id,
            language_alpha_3_code=language_alpha_3_code,
            url=url,
            url_malware_protection_status=url_malware_protection_status,
            create_user_full_name=create_user_full_name,
            create_user_type=create_user_type,
            update_user_full_name=update_user_full_name,
            update_user_type=update_user_type,
            create_date_time=create_date_time,
            update_date_time=update_date_time,
            create_user_id=create_user_id,
            update_user_id=update_user_id,
        )

        attachment_fields.additional_properties = d
        return attachment_fields

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
