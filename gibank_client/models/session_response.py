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
    from ..models.session_response_company_type_0 import SessionResponseCompanyType0
    from ..models.session_response_role import SessionResponseRole
    from ..models.session_response_user import SessionResponseUser


T = TypeVar("T", bound="SessionResponse")


@_attrs_define
class SessionResponse:
    """
    Attributes:
        user (SessionResponseUser | Unset):
        role (SessionResponseRole | Unset):
        permission_keys (list[str] | Unset):
        company (None | SessionResponseCompanyType0 | Unset):
    """

    user: SessionResponseUser | Unset = UNSET
    role: SessionResponseRole | Unset = UNSET
    permission_keys: list[str] | Unset = UNSET
    company: None | SessionResponseCompanyType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.session_response_company_type_0 import SessionResponseCompanyType0

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        role: dict[str, Any] | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.to_dict()

        permission_keys: list[str] | Unset = UNSET
        if not isinstance(self.permission_keys, Unset):
            permission_keys = self.permission_keys

        company: dict[str, Any] | None | Unset
        if isinstance(self.company, Unset):
            company = UNSET
        elif isinstance(self.company, SessionResponseCompanyType0):
            company = self.company.to_dict()
        else:
            company = self.company

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user
        if role is not UNSET:
            field_dict["role"] = role
        if permission_keys is not UNSET:
            field_dict["permission_keys"] = permission_keys
        if company is not UNSET:
            field_dict["company"] = company

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.session_response_company_type_0 import SessionResponseCompanyType0
        from ..models.session_response_role import SessionResponseRole
        from ..models.session_response_user import SessionResponseUser

        d = dict(src_dict)
        _user = d.pop("user", UNSET)
        user: SessionResponseUser | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = SessionResponseUser.from_dict(_user)

        _role = d.pop("role", UNSET)
        role: SessionResponseRole | Unset
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = SessionResponseRole.from_dict(_role)

        permission_keys = cast(list[str], d.pop("permission_keys", UNSET))

        def _parse_company(data: object) -> None | SessionResponseCompanyType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_type_0 = SessionResponseCompanyType0.from_dict(data)

                return company_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SessionResponseCompanyType0 | Unset, data)

        company = _parse_company(d.pop("company", UNSET))

        session_response = cls(
            user=user,
            role=role,
            permission_keys=permission_keys,
            company=company,
        )

        session_response.additional_properties = d
        return session_response

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
