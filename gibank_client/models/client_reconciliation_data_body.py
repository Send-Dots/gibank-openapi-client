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
    from ..models.client_reconciliation_account import ClientReconciliationAccount
    from ..models.client_reconciliation_transaction import (
        ClientReconciliationTransaction,
    )


T = TypeVar("T", bound="ClientReconciliationDataBody")


@_attrs_define
class ClientReconciliationDataBody:
    """
    Attributes:
        data (list[ClientReconciliationAccount | ClientReconciliationTransaction] | Unset):
        url (str | Unset): The url of the file you uploaded previously using a generated URL (uploaded raw/JSON file),
            see `/file/upload_url`
        direct_invoke (bool | None | Unset): In normal cases, client data is sent to a queue system to ensure there is
            enough time to reconcile.
            However, direct invoke means that we don't use the queue system but instead reconcile immediately.
            For testing purposes only and not recommended for general use.
    """

    data: (
        list[ClientReconciliationAccount | ClientReconciliationTransaction] | Unset
    ) = UNSET
    url: str | Unset = UNSET
    direct_invoke: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.client_reconciliation_account import ClientReconciliationAccount

        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item: dict[str, Any]
                if isinstance(data_item_data, ClientReconciliationAccount):
                    data_item = data_item_data.to_dict()
                else:
                    data_item = data_item_data.to_dict()

                data.append(data_item)

        url = self.url

        direct_invoke: bool | None | Unset
        if isinstance(self.direct_invoke, Unset):
            direct_invoke = UNSET
        else:
            direct_invoke = self.direct_invoke

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if url is not UNSET:
            field_dict["url"] = url
        if direct_invoke is not UNSET:
            field_dict["direct_invoke"] = direct_invoke

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.client_reconciliation_account import ClientReconciliationAccount
        from ..models.client_reconciliation_transaction import (
            ClientReconciliationTransaction,
        )

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: (
            list[ClientReconciliationAccount | ClientReconciliationTransaction] | Unset
        ) = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:

                def _parse_data_item(
                    data: object,
                ) -> ClientReconciliationAccount | ClientReconciliationTransaction:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_client_reconciliation_data_type_0 = (
                            ClientReconciliationAccount.from_dict(data)
                        )

                        return componentsschemas_client_reconciliation_data_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_client_reconciliation_data_type_1 = (
                        ClientReconciliationTransaction.from_dict(data)
                    )

                    return componentsschemas_client_reconciliation_data_type_1

                data_item = _parse_data_item(data_item_data)

                data.append(data_item)

        url = d.pop("url", UNSET)

        def _parse_direct_invoke(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        direct_invoke = _parse_direct_invoke(d.pop("direct_invoke", UNSET))

        client_reconciliation_data_body = cls(
            data=data,
            url=url,
            direct_invoke=direct_invoke,
        )

        client_reconciliation_data_body.additional_properties = d
        return client_reconciliation_data_body

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
