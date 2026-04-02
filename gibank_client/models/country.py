from __future__ import annotations

from collections.abc import Mapping
from typing import Any
from typing import TypeVar
from typing import cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.country_account_number_type import CountryAccountNumberType
from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="Country")


@_attrs_define
class Country:
    r"""
    Attributes:
        id (float | Unset): The Country ID Example: 1.
        name (str | Unset): The country Name Example: United States of America.
        alpha_2_code (str | Unset): The ISO 3166-1 alpha-2 code Example: US.
        alpha_3_code (str | Unset): The ISO 3166-1 alpha-3 code Example: USA.
        postal_code_regex (None | str | Unset): The country postal code Regex pattern Example: ^\d{5}([\-]?\d{4})?$.
        account_number_type (CountryAccountNumberType | Unset): The account number type

            **iban_mandatory:**
            For counterparties in certain countries, International Bank Account Numbers (IBANs) are strictly required. The
            API will validate and enforce the specified format.

            **highly_recommended:**
            While not mandatory, following the specified account number formats for counterparties in these countries is
            highly recommended to prevent payment delays or rejections. The API does not enforce these formats, but they
            represent local best practices.
             Example: iban_mandatory.
        account_number_regex (None | str | Unset): The account number Regex pattern Example: ^\d{5}([\-]?\d{4})?$.
        account_number_example (None | str | Unset): The account number example Example: BE1234567890.
    """

    id: float | Unset = UNSET
    name: str | Unset = UNSET
    alpha_2_code: str | Unset = UNSET
    alpha_3_code: str | Unset = UNSET
    postal_code_regex: None | str | Unset = UNSET
    account_number_type: CountryAccountNumberType | Unset = UNSET
    account_number_regex: None | str | Unset = UNSET
    account_number_example: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        alpha_2_code = self.alpha_2_code

        alpha_3_code = self.alpha_3_code

        postal_code_regex: None | str | Unset
        if isinstance(self.postal_code_regex, Unset):
            postal_code_regex = UNSET
        else:
            postal_code_regex = self.postal_code_regex

        account_number_type: str | Unset = UNSET
        if not isinstance(self.account_number_type, Unset):
            account_number_type = self.account_number_type.value

        account_number_regex: None | str | Unset
        if isinstance(self.account_number_regex, Unset):
            account_number_regex = UNSET
        else:
            account_number_regex = self.account_number_regex

        account_number_example: None | str | Unset
        if isinstance(self.account_number_example, Unset):
            account_number_example = UNSET
        else:
            account_number_example = self.account_number_example

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if alpha_2_code is not UNSET:
            field_dict["alpha_2_code"] = alpha_2_code
        if alpha_3_code is not UNSET:
            field_dict["alpha_3_code"] = alpha_3_code
        if postal_code_regex is not UNSET:
            field_dict["postal_code_regex"] = postal_code_regex
        if account_number_type is not UNSET:
            field_dict["account_number_type"] = account_number_type
        if account_number_regex is not UNSET:
            field_dict["account_number_regex"] = account_number_regex
        if account_number_example is not UNSET:
            field_dict["account_number_example"] = account_number_example

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        alpha_2_code = d.pop("alpha_2_code", UNSET)

        alpha_3_code = d.pop("alpha_3_code", UNSET)

        def _parse_postal_code_regex(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        postal_code_regex = _parse_postal_code_regex(d.pop("postal_code_regex", UNSET))

        _account_number_type = d.pop("account_number_type", UNSET)
        account_number_type: CountryAccountNumberType | Unset
        if isinstance(_account_number_type, Unset):
            account_number_type = UNSET
        else:
            account_number_type = CountryAccountNumberType(_account_number_type)

        def _parse_account_number_regex(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account_number_regex = _parse_account_number_regex(
            d.pop("account_number_regex", UNSET)
        )

        def _parse_account_number_example(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account_number_example = _parse_account_number_example(
            d.pop("account_number_example", UNSET)
        )

        country = cls(
            id=id,
            name=name,
            alpha_2_code=alpha_2_code,
            alpha_3_code=alpha_3_code,
            postal_code_regex=postal_code_regex,
            account_number_type=account_number_type,
            account_number_regex=account_number_regex,
            account_number_example=account_number_example,
        )

        country.additional_properties = d
        return country

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
