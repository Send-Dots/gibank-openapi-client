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
    from ..models.transaction_files_response_parse_virtual_type_0 import (
        TransactionFilesResponseParseVirtualType0,
    )
    from ..models.transaction_files_response_parsed_type_0 import (
        TransactionFilesResponseParsedType0,
    )
    from ..models.transaction_files_response_processed_parsed_type_0 import (
        TransactionFilesResponseProcessedParsedType0,
    )
    from ..models.transaction_files_response_processed_raw_type_0 import (
        TransactionFilesResponseProcessedRawType0,
    )
    from ..models.transaction_files_response_raw_type_0 import (
        TransactionFilesResponseRawType0,
    )
    from ..models.transaction_files_response_raw_virtual_type_0 import (
        TransactionFilesResponseRawVirtualType0,
    )


T = TypeVar("T", bound="TransactionFilesResponse")


@_attrs_define
class TransactionFilesResponse:
    """
    Attributes:
        raw (None | TransactionFilesResponseRawType0 | Unset):
        parsed (None | TransactionFilesResponseParsedType0 | Unset):
        raw_virtual (None | TransactionFilesResponseRawVirtualType0 | Unset):
        parse_virtual (None | TransactionFilesResponseParseVirtualType0 | Unset):
        processed_raw (None | TransactionFilesResponseProcessedRawType0 | Unset):
        processed_parsed (None | TransactionFilesResponseProcessedParsedType0 | Unset):
    """

    raw: None | TransactionFilesResponseRawType0 | Unset = UNSET
    parsed: None | TransactionFilesResponseParsedType0 | Unset = UNSET
    raw_virtual: None | TransactionFilesResponseRawVirtualType0 | Unset = UNSET
    parse_virtual: None | TransactionFilesResponseParseVirtualType0 | Unset = UNSET
    processed_raw: None | TransactionFilesResponseProcessedRawType0 | Unset = UNSET
    processed_parsed: None | TransactionFilesResponseProcessedParsedType0 | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.transaction_files_response_parse_virtual_type_0 import (
            TransactionFilesResponseParseVirtualType0,
        )
        from ..models.transaction_files_response_parsed_type_0 import (
            TransactionFilesResponseParsedType0,
        )
        from ..models.transaction_files_response_processed_parsed_type_0 import (
            TransactionFilesResponseProcessedParsedType0,
        )
        from ..models.transaction_files_response_processed_raw_type_0 import (
            TransactionFilesResponseProcessedRawType0,
        )
        from ..models.transaction_files_response_raw_type_0 import (
            TransactionFilesResponseRawType0,
        )
        from ..models.transaction_files_response_raw_virtual_type_0 import (
            TransactionFilesResponseRawVirtualType0,
        )

        raw: dict[str, Any] | None | Unset
        if isinstance(self.raw, Unset):
            raw = UNSET
        elif isinstance(self.raw, TransactionFilesResponseRawType0):
            raw = self.raw.to_dict()
        else:
            raw = self.raw

        parsed: dict[str, Any] | None | Unset
        if isinstance(self.parsed, Unset):
            parsed = UNSET
        elif isinstance(self.parsed, TransactionFilesResponseParsedType0):
            parsed = self.parsed.to_dict()
        else:
            parsed = self.parsed

        raw_virtual: dict[str, Any] | None | Unset
        if isinstance(self.raw_virtual, Unset):
            raw_virtual = UNSET
        elif isinstance(self.raw_virtual, TransactionFilesResponseRawVirtualType0):
            raw_virtual = self.raw_virtual.to_dict()
        else:
            raw_virtual = self.raw_virtual

        parse_virtual: dict[str, Any] | None | Unset
        if isinstance(self.parse_virtual, Unset):
            parse_virtual = UNSET
        elif isinstance(self.parse_virtual, TransactionFilesResponseParseVirtualType0):
            parse_virtual = self.parse_virtual.to_dict()
        else:
            parse_virtual = self.parse_virtual

        processed_raw: dict[str, Any] | None | Unset
        if isinstance(self.processed_raw, Unset):
            processed_raw = UNSET
        elif isinstance(self.processed_raw, TransactionFilesResponseProcessedRawType0):
            processed_raw = self.processed_raw.to_dict()
        else:
            processed_raw = self.processed_raw

        processed_parsed: dict[str, Any] | None | Unset
        if isinstance(self.processed_parsed, Unset):
            processed_parsed = UNSET
        elif isinstance(
            self.processed_parsed, TransactionFilesResponseProcessedParsedType0
        ):
            processed_parsed = self.processed_parsed.to_dict()
        else:
            processed_parsed = self.processed_parsed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if raw is not UNSET:
            field_dict["raw"] = raw
        if parsed is not UNSET:
            field_dict["parsed"] = parsed
        if raw_virtual is not UNSET:
            field_dict["raw_virtual"] = raw_virtual
        if parse_virtual is not UNSET:
            field_dict["parse_virtual"] = parse_virtual
        if processed_raw is not UNSET:
            field_dict["processed_raw"] = processed_raw
        if processed_parsed is not UNSET:
            field_dict["processed_parsed"] = processed_parsed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transaction_files_response_parse_virtual_type_0 import (
            TransactionFilesResponseParseVirtualType0,
        )
        from ..models.transaction_files_response_parsed_type_0 import (
            TransactionFilesResponseParsedType0,
        )
        from ..models.transaction_files_response_processed_parsed_type_0 import (
            TransactionFilesResponseProcessedParsedType0,
        )
        from ..models.transaction_files_response_processed_raw_type_0 import (
            TransactionFilesResponseProcessedRawType0,
        )
        from ..models.transaction_files_response_raw_type_0 import (
            TransactionFilesResponseRawType0,
        )
        from ..models.transaction_files_response_raw_virtual_type_0 import (
            TransactionFilesResponseRawVirtualType0,
        )

        d = dict(src_dict)

        def _parse_raw(data: object) -> None | TransactionFilesResponseRawType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                raw_type_0 = TransactionFilesResponseRawType0.from_dict(data)

                return raw_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TransactionFilesResponseRawType0 | Unset, data)

        raw = _parse_raw(d.pop("raw", UNSET))

        def _parse_parsed(
            data: object,
        ) -> None | TransactionFilesResponseParsedType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                parsed_type_0 = TransactionFilesResponseParsedType0.from_dict(data)

                return parsed_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TransactionFilesResponseParsedType0 | Unset, data)

        parsed = _parse_parsed(d.pop("parsed", UNSET))

        def _parse_raw_virtual(
            data: object,
        ) -> None | TransactionFilesResponseRawVirtualType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                raw_virtual_type_0 = TransactionFilesResponseRawVirtualType0.from_dict(
                    data
                )

                return raw_virtual_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TransactionFilesResponseRawVirtualType0 | Unset, data)

        raw_virtual = _parse_raw_virtual(d.pop("raw_virtual", UNSET))

        def _parse_parse_virtual(
            data: object,
        ) -> None | TransactionFilesResponseParseVirtualType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                parse_virtual_type_0 = (
                    TransactionFilesResponseParseVirtualType0.from_dict(data)
                )

                return parse_virtual_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TransactionFilesResponseParseVirtualType0 | Unset, data)

        parse_virtual = _parse_parse_virtual(d.pop("parse_virtual", UNSET))

        def _parse_processed_raw(
            data: object,
        ) -> None | TransactionFilesResponseProcessedRawType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                processed_raw_type_0 = (
                    TransactionFilesResponseProcessedRawType0.from_dict(data)
                )

                return processed_raw_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TransactionFilesResponseProcessedRawType0 | Unset, data)

        processed_raw = _parse_processed_raw(d.pop("processed_raw", UNSET))

        def _parse_processed_parsed(
            data: object,
        ) -> None | TransactionFilesResponseProcessedParsedType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                processed_parsed_type_0 = (
                    TransactionFilesResponseProcessedParsedType0.from_dict(data)
                )

                return processed_parsed_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | TransactionFilesResponseProcessedParsedType0 | Unset, data
            )

        processed_parsed = _parse_processed_parsed(d.pop("processed_parsed", UNSET))

        transaction_files_response = cls(
            raw=raw,
            parsed=parsed,
            raw_virtual=raw_virtual,
            parse_virtual=parse_virtual,
            processed_raw=processed_raw,
            processed_parsed=processed_parsed,
        )

        transaction_files_response.additional_properties = d
        return transaction_files_response

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
