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

from ..models.subclient_fields_relationship_type import SubclientFieldsRelationshipType
from ..models.subclient_fields_state import SubclientFieldsState
from ..models.subclient_fields_type import SubclientFieldsType
from ..types import UNSET
from ..types import Unset

if TYPE_CHECKING:
    from ..models.address_fields import AddressFields
    from ..models.subclient_data_business_response import SubclientDataBusinessResponse
    from ..models.subclient_data_natural_person_response import (
        SubclientDataNaturalPersonResponse,
    )


T = TypeVar("T", bound="Subclient")


@_attrs_define
class Subclient:
    """
    Attributes:
        id (float | Unset): The subclient ID Example: 1.
        external_key (None | str | Unset): External key of the subclient Example: BUS123.
        name (str | Unset): The name of the subclient Example: Acme Inc..
        active (bool | Unset): Indicates if the subclient is active Default: True. Example: True.
        type_ (SubclientFieldsType | Unset): The type of the subclient Example: business.
        relationship_type (SubclientFieldsRelationshipType | Unset): The relationship of the subclient to the client.

            - `customer` - A Customer represents a person or organization possessing separate and distinct legal rights. You
            will create entities for each customer or user. A Subclient is required to create a Subclient account.
            - `counterparty` - A Counterparty is any person or organization that ultimately sends or receives funds as part
            of your funds flow. While remittance flows may utilize payment service providers and/or affiliates to prepare
            funds for payout, those receiving the payment are counterparties. Likwise, any known party that sends funds to
            this Bank and that does not meet any other definition is also a Counterparty. NOTE - fields such as address
            related information, while not required for creation of the subclient, are highly recommended when sending
            domestic or international wires.
            - `payment_service_provider` - A Payment Service Provider is a third-party company that helps enable your
            payment flows. Some Examples: card processors, FX providers, and payout networks.
            - `affiliate` - An Affiliate is any entity that controls, is controlled by, or is under common control with your
            company. This includes parent companies, subsidiaries, and sister companies with shared ownership — including
            foreign entities owned by the same parent organization but operating in another jurisdiction.
            - `root` - The Root Subclient is your company.
             Example: customer.
        state (SubclientFieldsState | Unset): The state of the subclient. States `approved` and `rejected` are reserved
            to bank members. Use `pending` to request approval. Default: SubclientFieldsState.CREATED. Example: created.
        company_id (float | Unset): The company ID Example: 1.
        company_name (str | Unset): The company name of the user Example: ABC Fintech.
        comment_count (float | Unset): The number of comments that exist on the subclient
        create_date_time (datetime.datetime | Unset): The date and time when the subclient was created (Stored as UTC,
            formatted as zero UTC offset (Zulu) format) Example: 2024-02-04T23:00:00.000Z.
        update_date_time (datetime.datetime | Unset): The date and time when the subclient was last updated (Stored as
            UTC, formatted as zero UTC offset (Zulu) format) Example: 2024-02-04T23:00:00.000Z.
        create_user_id (float | Unset): The ID of the user who created the subclient Example: 1.
        update_user_id (float | Unset): The ID of the user who last updated the subclient Example: 1.
        data (SubclientDataBusinessResponse | SubclientDataNaturalPersonResponse | Unset):
        address (AddressFields | Unset):
    """

    id: float | Unset = UNSET
    external_key: None | str | Unset = UNSET
    name: str | Unset = UNSET
    active: bool | Unset = True
    type_: SubclientFieldsType | Unset = UNSET
    relationship_type: SubclientFieldsRelationshipType | Unset = UNSET
    state: SubclientFieldsState | Unset = SubclientFieldsState.CREATED
    company_id: float | Unset = UNSET
    company_name: str | Unset = UNSET
    comment_count: float | Unset = UNSET
    create_date_time: datetime.datetime | Unset = UNSET
    update_date_time: datetime.datetime | Unset = UNSET
    create_user_id: float | Unset = UNSET
    update_user_id: float | Unset = UNSET
    data: SubclientDataBusinessResponse | SubclientDataNaturalPersonResponse | Unset = (
        UNSET
    )
    address: AddressFields | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.subclient_data_business_response import (
            SubclientDataBusinessResponse,
        )

        id = self.id

        external_key: None | str | Unset
        if isinstance(self.external_key, Unset):
            external_key = UNSET
        else:
            external_key = self.external_key

        name = self.name

        active = self.active

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        relationship_type: str | Unset = UNSET
        if not isinstance(self.relationship_type, Unset):
            relationship_type = self.relationship_type.value

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        company_id = self.company_id

        company_name = self.company_name

        comment_count = self.comment_count

        create_date_time: str | Unset = UNSET
        if not isinstance(self.create_date_time, Unset):
            create_date_time = self.create_date_time.isoformat()

        update_date_time: str | Unset = UNSET
        if not isinstance(self.update_date_time, Unset):
            update_date_time = self.update_date_time.isoformat()

        create_user_id = self.create_user_id

        update_user_id = self.update_user_id

        data: dict[str, Any] | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, SubclientDataBusinessResponse):
            data = self.data.to_dict()
        else:
            data = self.data.to_dict()

        address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if external_key is not UNSET:
            field_dict["external_key"] = external_key
        if name is not UNSET:
            field_dict["name"] = name
        if active is not UNSET:
            field_dict["active"] = active
        if type_ is not UNSET:
            field_dict["type"] = type_
        if relationship_type is not UNSET:
            field_dict["relationship_type"] = relationship_type
        if state is not UNSET:
            field_dict["state"] = state
        if company_id is not UNSET:
            field_dict["company_id"] = company_id
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if comment_count is not UNSET:
            field_dict["comment_count"] = comment_count
        if create_date_time is not UNSET:
            field_dict["create_date_time"] = create_date_time
        if update_date_time is not UNSET:
            field_dict["update_date_time"] = update_date_time
        if create_user_id is not UNSET:
            field_dict["create_user_id"] = create_user_id
        if update_user_id is not UNSET:
            field_dict["update_user_id"] = update_user_id
        if data is not UNSET:
            field_dict["data"] = data
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address_fields import AddressFields
        from ..models.subclient_data_business_response import (
            SubclientDataBusinessResponse,
        )
        from ..models.subclient_data_natural_person_response import (
            SubclientDataNaturalPersonResponse,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_external_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_key = _parse_external_key(d.pop("external_key", UNSET))

        name = d.pop("name", UNSET)

        active = d.pop("active", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: SubclientFieldsType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = SubclientFieldsType(_type_)

        _relationship_type = d.pop("relationship_type", UNSET)
        relationship_type: SubclientFieldsRelationshipType | Unset
        if isinstance(_relationship_type, Unset):
            relationship_type = UNSET
        else:
            relationship_type = SubclientFieldsRelationshipType(_relationship_type)

        _state = d.pop("state", UNSET)
        state: SubclientFieldsState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = SubclientFieldsState(_state)

        company_id = d.pop("company_id", UNSET)

        company_name = d.pop("company_name", UNSET)

        comment_count = d.pop("comment_count", UNSET)

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

        def _parse_data(
            data: object,
        ) -> SubclientDataBusinessResponse | SubclientDataNaturalPersonResponse | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_subclient_data_response_type_0 = (
                    SubclientDataBusinessResponse.from_dict(data)
                )

                return componentsschemas_subclient_data_response_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_subclient_data_response_type_1 = (
                SubclientDataNaturalPersonResponse.from_dict(data)
            )

            return componentsschemas_subclient_data_response_type_1

        data = _parse_data(d.pop("data", UNSET))

        _address = d.pop("address", UNSET)
        address: AddressFields | Unset
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = AddressFields.from_dict(_address)

        subclient = cls(
            id=id,
            external_key=external_key,
            name=name,
            active=active,
            type_=type_,
            relationship_type=relationship_type,
            state=state,
            company_id=company_id,
            company_name=company_name,
            comment_count=comment_count,
            create_date_time=create_date_time,
            update_date_time=update_date_time,
            create_user_id=create_user_id,
            update_user_id=update_user_id,
            data=data,
            address=address,
        )

        subclient.additional_properties = d
        return subclient

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
