from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any
from typing import TypeVar
from typing import cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.business_fields_risk_rating import BusinessFieldsRiskRating
from ..models.subclient_data_business_type import SubclientDataBusinessType
from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="SubclientDataBusiness")


@_attrs_define
class SubclientDataBusiness:
    """
    Attributes:
        legal_name (str): Legal name of the business Example: Acme Corporation.
        type_ (SubclientDataBusinessType):  Example: business.
        id (float | Unset): The subclient data business ID Example: 1.
        subclient_id (float | Unset): The subclient ID Example: 1.
        onboarding_date (datetime.date | None | Unset): Date when the business was onboarded Example: 2024-02-04.
        registration_number (None | str | Unset): Business registration number Example: REG12345.
        website (None | str | Unset): Website of the business Example: https://www.acmecorp.com.
        risk_rating (BusinessFieldsRiskRating | Unset): Risk rating of the business Example: low.
        risk_rating_date_time (datetime.datetime | None | Unset): Date and time when the risk rating was last updated
            (Stored as UTC, formatted as zero UTC offset (Zulu) format) Example: 2024-02-04T23:00:00.000Z.
        high_risk (bool | None | Unset): If there is a high risk
        create_date_time (datetime.datetime | Unset): The date and time when the subclient data business was created
            (Stored as UTC, formatted as zero UTC offset (Zulu) format) Example: 2024-02-04T23:00:00.000Z.
        update_date_time (datetime.datetime | Unset): The date and time when the subclient data business was last
            updated (Stored as UTC, formatted as zero UTC offset (Zulu) format) Example: 2024-02-04T23:00:00.000Z.
        create_user_id (float | Unset): The ID of the user who created the subclient data business Example: 1.
        update_user_id (float | Unset): The ID of the user who last updated the subclient data business Example: 1.
    """

    legal_name: str
    type_: SubclientDataBusinessType
    id: float | Unset = UNSET
    subclient_id: float | Unset = UNSET
    onboarding_date: datetime.date | None | Unset = UNSET
    registration_number: None | str | Unset = UNSET
    website: None | str | Unset = UNSET
    risk_rating: BusinessFieldsRiskRating | Unset = UNSET
    risk_rating_date_time: datetime.datetime | None | Unset = UNSET
    high_risk: bool | None | Unset = UNSET
    create_date_time: datetime.datetime | Unset = UNSET
    update_date_time: datetime.datetime | Unset = UNSET
    create_user_id: float | Unset = UNSET
    update_user_id: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        legal_name = self.legal_name

        type_ = self.type_.value

        id = self.id

        subclient_id = self.subclient_id

        onboarding_date: None | str | Unset
        if isinstance(self.onboarding_date, Unset):
            onboarding_date = UNSET
        elif isinstance(self.onboarding_date, datetime.date):
            onboarding_date = self.onboarding_date.isoformat()
        else:
            onboarding_date = self.onboarding_date

        registration_number: None | str | Unset
        if isinstance(self.registration_number, Unset):
            registration_number = UNSET
        else:
            registration_number = self.registration_number

        website: None | str | Unset
        if isinstance(self.website, Unset):
            website = UNSET
        else:
            website = self.website

        risk_rating: str | Unset = UNSET
        if not isinstance(self.risk_rating, Unset):
            risk_rating = self.risk_rating.value

        risk_rating_date_time: None | str | Unset
        if isinstance(self.risk_rating_date_time, Unset):
            risk_rating_date_time = UNSET
        elif isinstance(self.risk_rating_date_time, datetime.datetime):
            risk_rating_date_time = self.risk_rating_date_time.isoformat()
        else:
            risk_rating_date_time = self.risk_rating_date_time

        high_risk: bool | None | Unset
        if isinstance(self.high_risk, Unset):
            high_risk = UNSET
        else:
            high_risk = self.high_risk

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
        field_dict.update(
            {
                "legal_name": legal_name,
                "type": type_,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if subclient_id is not UNSET:
            field_dict["subclient_id"] = subclient_id
        if onboarding_date is not UNSET:
            field_dict["onboarding_date"] = onboarding_date
        if registration_number is not UNSET:
            field_dict["registration_number"] = registration_number
        if website is not UNSET:
            field_dict["website"] = website
        if risk_rating is not UNSET:
            field_dict["risk_rating"] = risk_rating
        if risk_rating_date_time is not UNSET:
            field_dict["risk_rating_date_time"] = risk_rating_date_time
        if high_risk is not UNSET:
            field_dict["high_risk"] = high_risk
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
        d = dict(src_dict)
        legal_name = d.pop("legal_name")

        type_ = SubclientDataBusinessType(d.pop("type"))

        id = d.pop("id", UNSET)

        subclient_id = d.pop("subclient_id", UNSET)

        def _parse_onboarding_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                onboarding_date_type_0 = isoparse(data).date()

                return onboarding_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        onboarding_date = _parse_onboarding_date(d.pop("onboarding_date", UNSET))

        def _parse_registration_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        registration_number = _parse_registration_number(
            d.pop("registration_number", UNSET)
        )

        def _parse_website(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website = _parse_website(d.pop("website", UNSET))

        _risk_rating = d.pop("risk_rating", UNSET)
        risk_rating: BusinessFieldsRiskRating | Unset
        if isinstance(_risk_rating, Unset):
            risk_rating = UNSET
        else:
            risk_rating = BusinessFieldsRiskRating(_risk_rating)

        def _parse_risk_rating_date_time(
            data: object,
        ) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                risk_rating_date_time_type_0 = isoparse(data)

                return risk_rating_date_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        risk_rating_date_time = _parse_risk_rating_date_time(
            d.pop("risk_rating_date_time", UNSET)
        )

        def _parse_high_risk(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        high_risk = _parse_high_risk(d.pop("high_risk", UNSET))

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

        subclient_data_business = cls(
            legal_name=legal_name,
            type_=type_,
            id=id,
            subclient_id=subclient_id,
            onboarding_date=onboarding_date,
            registration_number=registration_number,
            website=website,
            risk_rating=risk_rating,
            risk_rating_date_time=risk_rating_date_time,
            high_risk=high_risk,
            create_date_time=create_date_time,
            update_date_time=update_date_time,
            create_user_id=create_user_id,
            update_user_id=update_user_id,
        )

        subclient_data_business.additional_properties = d
        return subclient_data_business

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
