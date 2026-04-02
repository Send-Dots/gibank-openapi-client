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
    from ..models.batch_files_response_batch_parsed_type_0 import (
        BatchFilesResponseBatchParsedType0,
    )
    from ..models.batch_files_response_batch_parsed_virtual_type_0 import (
        BatchFilesResponseBatchParsedVirtualType0,
    )
    from ..models.batch_files_response_batch_raw_type_0 import (
        BatchFilesResponseBatchRawType0,
    )
    from ..models.batch_files_response_batch_raw_virtual_type_0 import (
        BatchFilesResponseBatchRawVirtualType0,
    )
    from ..models.batch_files_response_processed_parsed_type_0 import (
        BatchFilesResponseProcessedParsedType0,
    )
    from ..models.batch_files_response_processed_raw_type_0 import (
        BatchFilesResponseProcessedRawType0,
    )


T = TypeVar("T", bound="BatchFilesResponse")


@_attrs_define
class BatchFilesResponse:
    """
    Attributes:
        batch_raw (BatchFilesResponseBatchRawType0 | None | Unset):
        batch_parsed (BatchFilesResponseBatchParsedType0 | None | Unset):
        batch_raw_virtual (BatchFilesResponseBatchRawVirtualType0 | None | Unset):
        batch_parsed_virtual (BatchFilesResponseBatchParsedVirtualType0 | None | Unset):
        processed_raw (BatchFilesResponseProcessedRawType0 | None | Unset):
        processed_parsed (BatchFilesResponseProcessedParsedType0 | None | Unset):
    """

    batch_raw: BatchFilesResponseBatchRawType0 | None | Unset = UNSET
    batch_parsed: BatchFilesResponseBatchParsedType0 | None | Unset = UNSET
    batch_raw_virtual: BatchFilesResponseBatchRawVirtualType0 | None | Unset = UNSET
    batch_parsed_virtual: BatchFilesResponseBatchParsedVirtualType0 | None | Unset = (
        UNSET
    )
    processed_raw: BatchFilesResponseProcessedRawType0 | None | Unset = UNSET
    processed_parsed: BatchFilesResponseProcessedParsedType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.batch_files_response_batch_parsed_type_0 import (
            BatchFilesResponseBatchParsedType0,
        )
        from ..models.batch_files_response_batch_parsed_virtual_type_0 import (
            BatchFilesResponseBatchParsedVirtualType0,
        )
        from ..models.batch_files_response_batch_raw_type_0 import (
            BatchFilesResponseBatchRawType0,
        )
        from ..models.batch_files_response_batch_raw_virtual_type_0 import (
            BatchFilesResponseBatchRawVirtualType0,
        )
        from ..models.batch_files_response_processed_parsed_type_0 import (
            BatchFilesResponseProcessedParsedType0,
        )
        from ..models.batch_files_response_processed_raw_type_0 import (
            BatchFilesResponseProcessedRawType0,
        )

        batch_raw: dict[str, Any] | None | Unset
        if isinstance(self.batch_raw, Unset):
            batch_raw = UNSET
        elif isinstance(self.batch_raw, BatchFilesResponseBatchRawType0):
            batch_raw = self.batch_raw.to_dict()
        else:
            batch_raw = self.batch_raw

        batch_parsed: dict[str, Any] | None | Unset
        if isinstance(self.batch_parsed, Unset):
            batch_parsed = UNSET
        elif isinstance(self.batch_parsed, BatchFilesResponseBatchParsedType0):
            batch_parsed = self.batch_parsed.to_dict()
        else:
            batch_parsed = self.batch_parsed

        batch_raw_virtual: dict[str, Any] | None | Unset
        if isinstance(self.batch_raw_virtual, Unset):
            batch_raw_virtual = UNSET
        elif isinstance(self.batch_raw_virtual, BatchFilesResponseBatchRawVirtualType0):
            batch_raw_virtual = self.batch_raw_virtual.to_dict()
        else:
            batch_raw_virtual = self.batch_raw_virtual

        batch_parsed_virtual: dict[str, Any] | None | Unset
        if isinstance(self.batch_parsed_virtual, Unset):
            batch_parsed_virtual = UNSET
        elif isinstance(
            self.batch_parsed_virtual, BatchFilesResponseBatchParsedVirtualType0
        ):
            batch_parsed_virtual = self.batch_parsed_virtual.to_dict()
        else:
            batch_parsed_virtual = self.batch_parsed_virtual

        processed_raw: dict[str, Any] | None | Unset
        if isinstance(self.processed_raw, Unset):
            processed_raw = UNSET
        elif isinstance(self.processed_raw, BatchFilesResponseProcessedRawType0):
            processed_raw = self.processed_raw.to_dict()
        else:
            processed_raw = self.processed_raw

        processed_parsed: dict[str, Any] | None | Unset
        if isinstance(self.processed_parsed, Unset):
            processed_parsed = UNSET
        elif isinstance(self.processed_parsed, BatchFilesResponseProcessedParsedType0):
            processed_parsed = self.processed_parsed.to_dict()
        else:
            processed_parsed = self.processed_parsed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if batch_raw is not UNSET:
            field_dict["batch_raw"] = batch_raw
        if batch_parsed is not UNSET:
            field_dict["batch_parsed"] = batch_parsed
        if batch_raw_virtual is not UNSET:
            field_dict["batch_raw_virtual"] = batch_raw_virtual
        if batch_parsed_virtual is not UNSET:
            field_dict["batch_parsed_virtual"] = batch_parsed_virtual
        if processed_raw is not UNSET:
            field_dict["processed_raw"] = processed_raw
        if processed_parsed is not UNSET:
            field_dict["processed_parsed"] = processed_parsed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.batch_files_response_batch_parsed_type_0 import (
            BatchFilesResponseBatchParsedType0,
        )
        from ..models.batch_files_response_batch_parsed_virtual_type_0 import (
            BatchFilesResponseBatchParsedVirtualType0,
        )
        from ..models.batch_files_response_batch_raw_type_0 import (
            BatchFilesResponseBatchRawType0,
        )
        from ..models.batch_files_response_batch_raw_virtual_type_0 import (
            BatchFilesResponseBatchRawVirtualType0,
        )
        from ..models.batch_files_response_processed_parsed_type_0 import (
            BatchFilesResponseProcessedParsedType0,
        )
        from ..models.batch_files_response_processed_raw_type_0 import (
            BatchFilesResponseProcessedRawType0,
        )

        d = dict(src_dict)

        def _parse_batch_raw(
            data: object,
        ) -> BatchFilesResponseBatchRawType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                batch_raw_type_0 = BatchFilesResponseBatchRawType0.from_dict(data)

                return batch_raw_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BatchFilesResponseBatchRawType0 | None | Unset, data)

        batch_raw = _parse_batch_raw(d.pop("batch_raw", UNSET))

        def _parse_batch_parsed(
            data: object,
        ) -> BatchFilesResponseBatchParsedType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                batch_parsed_type_0 = BatchFilesResponseBatchParsedType0.from_dict(data)

                return batch_parsed_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BatchFilesResponseBatchParsedType0 | None | Unset, data)

        batch_parsed = _parse_batch_parsed(d.pop("batch_parsed", UNSET))

        def _parse_batch_raw_virtual(
            data: object,
        ) -> BatchFilesResponseBatchRawVirtualType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                batch_raw_virtual_type_0 = (
                    BatchFilesResponseBatchRawVirtualType0.from_dict(data)
                )

                return batch_raw_virtual_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BatchFilesResponseBatchRawVirtualType0 | None | Unset, data)

        batch_raw_virtual = _parse_batch_raw_virtual(d.pop("batch_raw_virtual", UNSET))

        def _parse_batch_parsed_virtual(
            data: object,
        ) -> BatchFilesResponseBatchParsedVirtualType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                batch_parsed_virtual_type_0 = (
                    BatchFilesResponseBatchParsedVirtualType0.from_dict(data)
                )

                return batch_parsed_virtual_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BatchFilesResponseBatchParsedVirtualType0 | None | Unset, data)

        batch_parsed_virtual = _parse_batch_parsed_virtual(
            d.pop("batch_parsed_virtual", UNSET)
        )

        def _parse_processed_raw(
            data: object,
        ) -> BatchFilesResponseProcessedRawType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                processed_raw_type_0 = BatchFilesResponseProcessedRawType0.from_dict(
                    data
                )

                return processed_raw_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BatchFilesResponseProcessedRawType0 | None | Unset, data)

        processed_raw = _parse_processed_raw(d.pop("processed_raw", UNSET))

        def _parse_processed_parsed(
            data: object,
        ) -> BatchFilesResponseProcessedParsedType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                processed_parsed_type_0 = (
                    BatchFilesResponseProcessedParsedType0.from_dict(data)
                )

                return processed_parsed_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BatchFilesResponseProcessedParsedType0 | None | Unset, data)

        processed_parsed = _parse_processed_parsed(d.pop("processed_parsed", UNSET))

        batch_files_response = cls(
            batch_raw=batch_raw,
            batch_parsed=batch_parsed,
            batch_raw_virtual=batch_raw_virtual,
            batch_parsed_virtual=batch_parsed_virtual,
            processed_raw=processed_raw,
            processed_parsed=processed_parsed,
        )

        batch_files_response.additional_properties = d
        return batch_files_response

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
