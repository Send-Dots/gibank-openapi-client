from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any
from typing import TypeVar
from typing import cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.natural_person_fields_risk_rating import NaturalPersonFieldsRiskRating
from ..models.subclient_data_natural_person_type import SubclientDataNaturalPersonType
from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="SubclientDataNaturalPerson")


@_attrs_define
class SubclientDataNaturalPerson:
    """
    Attributes:
        first_name (str): First name of the natural person Example: John.
        last_name (str): Last name of the natural person Example: Doe.
        type_ (SubclientDataNaturalPersonType):  Example: natural_person.
        id (float | Unset): The subclient data natural person ID Example: 1.
        subclient_id (float | Unset): The subclient ID Example: 1.
        middle_name (None | str | Unset): Middle name of the natural person Example: Michael.
        birth_date (datetime.date | None | Unset): Birth date of the natural person Example: 1990-01-01.
        risk_rating (NaturalPersonFieldsRiskRating | Unset): Risk rating of the natural person Example: low.
        risk_rating_date_time (datetime.datetime | None | Unset): Date and time when the risk rating was last updated
            (Stored as UTC, formatted as zero UTC offset (Zulu) format) Example: 2024-02-04T23:00:00.000Z.
        high_risk (bool | None | Unset): If there is a high risk
        create_date_time (datetime.datetime | Unset): The date and time when the subclient data natural person was
            created (Stored as UTC, formatted as zero UTC offset (Zulu) format) Example: 2024-02-04T23:00:00.000Z.
        update_date_time (datetime.datetime | Unset): The date and time when the subclient data natural person was last
            updated (Stored as UTC, formatted as zero UTC offset (Zulu) format) Example: 2024-02-04T23:00:00.000Z.
        create_user_id (float | Unset): The ID of the user who created the subclient data natural person Example: 1.
        update_user_id (float | Unset): The ID of the user who last updated the subclient data natural person Example:
            1.
    """

    first_name: str
    last_name: str
    type_: SubclientDataNaturalPersonType
    id: float | Unset = UNSET
    subclient_id: float | Unset = UNSET
    middle_name: None | str | Unset = UNSET
    birth_date: datetime.date | None | Unset = UNSET
    risk_rating: NaturalPersonFieldsRiskRating | Unset = UNSET
    risk_rating_date_time: datetime.datetime | None | Unset = UNSET
    high_risk: bool | None | Unset = UNSET
    create_date_time: datetime.datetime | Unset = UNSET
    update_date_time: datetime.datetime | Unset = UNSET
    create_user_id: float | Unset = UNSET
    update_user_id: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        first_name = self.first_name

        last_name = self.last_name

        type_ = self.type_.value

        id = self.id

        subclient_id = self.subclient_id

        middle_name: None | str | Unset
        if isinstance(self.middle_name, Unset):
            middle_name = UNSET
        else:
            middle_name = self.middle_name

        birth_date: None | str | Unset
        if isinstance(self.birth_date, Unset):
            birth_date = UNSET
        elif isinstance(self.birth_date, datetime.date):
            birth_date = self.birth_date.isoformat()
        else:
            birth_date = self.birth_date

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
                "first_name": first_name,
                "last_name": last_name,
                "type": type_,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if subclient_id is not UNSET:
            field_dict["subclient_id"] = subclient_id
        if middle_name is not UNSET:
            field_dict["middle_name"] = middle_name
        if birth_date is not UNSET:
            field_dict["birth_date"] = birth_date
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
        first_name = d.pop("first_name")

        last_name = d.pop("last_name")

        type_ = SubclientDataNaturalPersonType(d.pop("type"))

        id = d.pop("id", UNSET)

        subclient_id = d.pop("subclient_id", UNSET)

        def _parse_middle_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        middle_name = _parse_middle_name(d.pop("middle_name", UNSET))

        def _parse_birth_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                birth_date_type_0 = isoparse(data).date()

                return birth_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        birth_date = _parse_birth_date(d.pop("birth_date", UNSET))

        _risk_rating = d.pop("risk_rating", UNSET)
        risk_rating: NaturalPersonFieldsRiskRating | Unset
        if isinstance(_risk_rating, Unset):
            risk_rating = UNSET
        else:
            risk_rating = NaturalPersonFieldsRiskRating(_risk_rating)

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

        subclient_data_natural_person = cls(
            first_name=first_name,
            last_name=last_name,
            type_=type_,
            id=id,
            subclient_id=subclient_id,
            middle_name=middle_name,
            birth_date=birth_date,
            risk_rating=risk_rating,
            risk_rating_date_time=risk_rating_date_time,
            high_risk=high_risk,
            create_date_time=create_date_time,
            update_date_time=update_date_time,
            create_user_id=create_user_id,
            update_user_id=update_user_id,
        )

        subclient_data_natural_person.additional_properties = d
        return subclient_data_natural_person

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
