from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING
from typing import Any
from typing import TypeVar
from typing import cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.properties_state import PropertiesState
from ..models.relationship_type import RelationshipType
from ..models.subclient_fields_properties_type import SubclientFieldsPropertiesType
from ..types import UNSET
from ..types import Unset

if TYPE_CHECKING:
    from ..models.address_create import AddressCreate
    from ..models.subclient_data_business import SubclientDataBusiness
    from ..models.subclient_data_natural_person import SubclientDataNaturalPerson


T = TypeVar("T", bound="SubclientCreate")


@_attrs_define
class SubclientCreate:
    """
    Example:
        {'name': 'Innovatech Solutions', 'external_key': 'IS-2025-001', 'active': True, 'type': 'business', 'data':
            {'type': 'business', 'legal_name': 'Innovatech Solutions LLC', 'onboarding_date': '2025-01-10'}, 'address':
            {'country_alpha_2_code': 'US', 'street_address_1': '123 Tech Park', 'city': 'Silicon Valley', 'state_province':
            'CA', 'postal_code': '94000'}}

    Attributes:
        name (str): The name of the subclient Example: Acme Inc..
        type_ (SubclientFieldsPropertiesType): The type of the subclient Example: business.
        external_key (None | str | Unset): External key of the subclient Example: BUS123.
        active (bool | Unset): Indicates if the subclient is active Example: True.
        relationship_type (RelationshipType | Unset): The relationship of the subclient to the client.

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
        state (PropertiesState | Unset): The state of the subclient. States `approved` and `rejected` are reserved to
            bank members. Use `pending` to request approval. Example: created.
        state_reason (str | Unset): The reason of the state. Required if `pending`/`approved`/`rejected` Example: Needs
            approval from Bank because of ....
        data (SubclientDataBusiness | SubclientDataNaturalPerson | Unset):
        address (AddressCreate | Unset):  Example: {'country_alpha_2_code': 'DE', 'street_address_1': 'Musterstraße 10',
            'city': 'Berlin', 'postal_code': '10117'}.
    """

    name: str
    type_: SubclientFieldsPropertiesType
    external_key: None | str | Unset = UNSET
    active: bool | Unset = UNSET
    relationship_type: RelationshipType | Unset = UNSET
    state: PropertiesState | Unset = UNSET
    state_reason: str | Unset = UNSET
    data: SubclientDataBusiness | SubclientDataNaturalPerson | Unset = UNSET
    address: AddressCreate | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.subclient_data_business import SubclientDataBusiness

        name = self.name

        type_ = self.type_.value

        external_key: None | str | Unset
        if isinstance(self.external_key, Unset):
            external_key = UNSET
        else:
            external_key = self.external_key

        active = self.active

        relationship_type: str | Unset = UNSET
        if not isinstance(self.relationship_type, Unset):
            relationship_type = self.relationship_type.value

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        state_reason = self.state_reason

        data: dict[str, Any] | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, SubclientDataBusiness):
            data = self.data.to_dict()
        else:
            data = self.data.to_dict()

        address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
            }
        )
        if external_key is not UNSET:
            field_dict["external_key"] = external_key
        if active is not UNSET:
            field_dict["active"] = active
        if relationship_type is not UNSET:
            field_dict["relationship_type"] = relationship_type
        if state is not UNSET:
            field_dict["state"] = state
        if state_reason is not UNSET:
            field_dict["state_reason"] = state_reason
        if data is not UNSET:
            field_dict["data"] = data
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address_create import AddressCreate
        from ..models.subclient_data_business import SubclientDataBusiness
        from ..models.subclient_data_natural_person import SubclientDataNaturalPerson

        d = dict(src_dict)
        name = d.pop("name")

        type_ = SubclientFieldsPropertiesType(d.pop("type"))

        def _parse_external_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_key = _parse_external_key(d.pop("external_key", UNSET))

        active = d.pop("active", UNSET)

        _relationship_type = d.pop("relationship_type", UNSET)
        relationship_type: RelationshipType | Unset
        if isinstance(_relationship_type, Unset):
            relationship_type = UNSET
        else:
            relationship_type = RelationshipType(_relationship_type)

        _state = d.pop("state", UNSET)
        state: PropertiesState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = PropertiesState(_state)

        state_reason = d.pop("state_reason", UNSET)

        def _parse_data(
            data: object,
        ) -> SubclientDataBusiness | SubclientDataNaturalPerson | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_subclient_data_type_0 = (
                    SubclientDataBusiness.from_dict(data)
                )

                return componentsschemas_subclient_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_subclient_data_type_1 = (
                SubclientDataNaturalPerson.from_dict(data)
            )

            return componentsschemas_subclient_data_type_1

        data = _parse_data(d.pop("data", UNSET))

        _address = d.pop("address", UNSET)
        address: AddressCreate | Unset
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = AddressCreate.from_dict(_address)

        subclient_create = cls(
            name=name,
            type_=type_,
            external_key=external_key,
            active=active,
            relationship_type=relationship_type,
            state=state,
            state_reason=state_reason,
            data=data,
            address=address,
        )

        subclient_create.additional_properties = d
        return subclient_create

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
