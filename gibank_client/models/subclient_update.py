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
from ..types import UNSET
from ..types import Unset

if TYPE_CHECKING:
    from ..models.address_update import AddressUpdate
    from ..models.subclient_data_business_response import SubclientDataBusinessResponse
    from ..models.subclient_data_natural_person_response import (
        SubclientDataNaturalPersonResponse,
    )


T = TypeVar("T", bound="SubclientUpdate")


@_attrs_define
class SubclientUpdate:
    """
    Example:
        {'name': 'Innovatech Global Solutions', 'active': False, 'data': {'type': 'business', 'website':
            'https://www.innovatech.global'}, 'address': {'street_address_1': '456 Global Avenue'}}

    Attributes:
        external_key (None | str | Unset): External key of the subclient Example: BUS123.
        name (str | Unset): The name of the subclient Example: Acme Inc..
        active (bool | Unset): Indicates if the subclient is active Example: True.
        state (PropertiesState | Unset): The state of the subclient. States `approved` and `rejected` are reserved to
            bank members. Use `pending` to request approval. Example: created.
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
        state_reason (str | Unset): The reason of the state. Required if `pending`/`approved`/`rejected` Example: Needs
            approval from Bank because of ....
        data (SubclientDataBusinessResponse | SubclientDataNaturalPersonResponse | Unset):
        address (AddressUpdate | Unset):  Example: {'street_address_1': 'Hauptstraße 5 (Updated)', 'postal_code':
            '10115'}.
    """

    external_key: None | str | Unset = UNSET
    name: str | Unset = UNSET
    active: bool | Unset = UNSET
    state: PropertiesState | Unset = UNSET
    relationship_type: RelationshipType | Unset = UNSET
    state_reason: str | Unset = UNSET
    data: SubclientDataBusinessResponse | SubclientDataNaturalPersonResponse | Unset = (
        UNSET
    )
    address: AddressUpdate | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.subclient_data_business_response import (
            SubclientDataBusinessResponse,
        )

        external_key: None | str | Unset
        if isinstance(self.external_key, Unset):
            external_key = UNSET
        else:
            external_key = self.external_key

        name = self.name

        active = self.active

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        relationship_type: str | Unset = UNSET
        if not isinstance(self.relationship_type, Unset):
            relationship_type = self.relationship_type.value

        state_reason = self.state_reason

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
        if external_key is not UNSET:
            field_dict["external_key"] = external_key
        if name is not UNSET:
            field_dict["name"] = name
        if active is not UNSET:
            field_dict["active"] = active
        if state is not UNSET:
            field_dict["state"] = state
        if relationship_type is not UNSET:
            field_dict["relationship_type"] = relationship_type
        if state_reason is not UNSET:
            field_dict["state_reason"] = state_reason
        if data is not UNSET:
            field_dict["data"] = data
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address_update import AddressUpdate
        from ..models.subclient_data_business_response import (
            SubclientDataBusinessResponse,
        )
        from ..models.subclient_data_natural_person_response import (
            SubclientDataNaturalPersonResponse,
        )

        d = dict(src_dict)

        def _parse_external_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_key = _parse_external_key(d.pop("external_key", UNSET))

        name = d.pop("name", UNSET)

        active = d.pop("active", UNSET)

        _state = d.pop("state", UNSET)
        state: PropertiesState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = PropertiesState(_state)

        _relationship_type = d.pop("relationship_type", UNSET)
        relationship_type: RelationshipType | Unset
        if isinstance(_relationship_type, Unset):
            relationship_type = UNSET
        else:
            relationship_type = RelationshipType(_relationship_type)

        state_reason = d.pop("state_reason", UNSET)

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
        address: AddressUpdate | Unset
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = AddressUpdate.from_dict(_address)

        subclient_update = cls(
            external_key=external_key,
            name=name,
            active=active,
            state=state,
            relationship_type=relationship_type,
            state_reason=state_reason,
            data=data,
            address=address,
        )

        subclient_update.additional_properties = d
        return subclient_update

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
