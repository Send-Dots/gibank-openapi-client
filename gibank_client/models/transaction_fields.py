from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any
from typing import TypeVar
from typing import cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.transaction_fields_create_user_type import TransactionFieldsCreateUserType
from ..models.transaction_fields_data_direction import TransactionFieldsDataDirection
from ..models.transaction_fields_state import TransactionFieldsState
from ..models.transaction_fields_transfer_direction import (
    TransactionFieldsTransferDirection,
)
from ..models.transaction_fields_transfer_flow import TransactionFieldsTransferFlow
from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="TransactionFields")


@_attrs_define
class TransactionFields:
    """
    Attributes:
        id (float | Unset): The transaction ID Example: 1.
        company_id (float | None | Unset): The company ID of the user who owns the transaction Example: 1.
        company_name (None | str | Unset): The company name of the user who created the transaction Example: ABC Bank.
        user_id (float | Unset): The user ID of the user who owns the transaction Example: 1.
        user_full_name (str | Unset): The full name of the user who created the transaction Example: Max Mustermann.
        create_user_id (float | Unset): The user ID of the user who created the transaction Example: 1.
        create_user_full_name (str | Unset): The full name of the user who created the transaction Example: Max
            Mustermann.
        create_user_type (TransactionFieldsCreateUserType | Unset): The type of the user who created the transaction
            Example: client.
        update_user_id (float | Unset): The user ID of the user who updated the transaction Example: 1.
        update_user_full_name (None | str | Unset): The full name of the user who updated the transaction Example: Max
            Mustermann.
        validated (bool | Unset): Indicates if the transaction has been validated Example: True.
        validate_error (None | str | Unset): Contains a possible validate error text Example: CashLetter ID is not
            unique.
        transfer_direction (TransactionFieldsTransferDirection | Unset): The direction of the transfer. `outbound` means
            money left your account, `inbound` means money was added to your account. Always outbound if both accounts are
            known in the system, so business shouldn't rely on it. Please use `transfer_flow` to have a clear info about
            push/pull from origin. Example: outbound.
        transfer_flow (TransactionFieldsTransferFlow | Unset): The flow of the transfer. `push` means the money went
            from origin to destination, `pull` means the money went from destination to origin Example: push.
        state (TransactionFieldsState | Unset): The state of the transaction Example: created.
        original_transaction_id (float | None | Unset): The original transaction ID (For Returns) Example: 1.
        return_transaction_id (float | None | Unset): The return transaction ID (If Returned) Example: 1.
        is_return_of_return (bool | Unset): Whether this return is a return-of-return (dishonoring another return)
        is_dishonored (bool | Unset): Whether this return has been dishonored (has a return-of-return)
        create_date_time (datetime.datetime | Unset): The date and time when the transaction was created (Stored as UTC,
            formatted as zero UTC offset (Zulu) format) Example: 2024-02-04T23:00:00.000Z.
        update_date_time (datetime.datetime | Unset): The date and time when the transaction was last updated (Stored as
            UTC, formatted as zero UTC offset (Zulu) format) Example: 2024-02-04T23:00:00.000Z.
        processed_date_time (datetime.datetime | Unset): The date and time when the transaction was processed (Stored as
            UTC, formatted as zero UTC offset (Zulu) format) Example: 2024-02-04T23:00:00.000Z.
        posted_date (datetime.date | Unset): The date when the transaction was posted Example: 2024-02-04.
        test (bool | Unset): Indicates if the transaction is a test transaction Example: True.
        deleted (bool | Unset): Indicates if the transaction is deleted
        batch_id (float | Unset): The batch ID Example: 4.
        batch_external_key (None | str | Unset): External key of the batch Example: ABC123456789.
        data_direction (TransactionFieldsDataDirection | Unset): Whether the batch file is outgoing or came in by
            another bank. Fintech API batches are always outgoing. API generated Returns are outgoing. Example: outgoing.
        comment_count (float | Unset): The number of comments that exist on the transaction
        running_balance (float | None | Unset): The balance of the core account after the transaction posted (Number of
            cents) Example: 100.
    """

    id: float | Unset = UNSET
    company_id: float | None | Unset = UNSET
    company_name: None | str | Unset = UNSET
    user_id: float | Unset = UNSET
    user_full_name: str | Unset = UNSET
    create_user_id: float | Unset = UNSET
    create_user_full_name: str | Unset = UNSET
    create_user_type: TransactionFieldsCreateUserType | Unset = UNSET
    update_user_id: float | Unset = UNSET
    update_user_full_name: None | str | Unset = UNSET
    validated: bool | Unset = UNSET
    validate_error: None | str | Unset = UNSET
    transfer_direction: TransactionFieldsTransferDirection | Unset = UNSET
    transfer_flow: TransactionFieldsTransferFlow | Unset = UNSET
    state: TransactionFieldsState | Unset = UNSET
    original_transaction_id: float | None | Unset = UNSET
    return_transaction_id: float | None | Unset = UNSET
    is_return_of_return: bool | Unset = UNSET
    is_dishonored: bool | Unset = UNSET
    create_date_time: datetime.datetime | Unset = UNSET
    update_date_time: datetime.datetime | Unset = UNSET
    processed_date_time: datetime.datetime | Unset = UNSET
    posted_date: datetime.date | Unset = UNSET
    test: bool | Unset = UNSET
    deleted: bool | Unset = UNSET
    batch_id: float | Unset = UNSET
    batch_external_key: None | str | Unset = UNSET
    data_direction: TransactionFieldsDataDirection | Unset = UNSET
    comment_count: float | Unset = UNSET
    running_balance: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        company_id: float | None | Unset
        if isinstance(self.company_id, Unset):
            company_id = UNSET
        else:
            company_id = self.company_id

        company_name: None | str | Unset
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        else:
            company_name = self.company_name

        user_id = self.user_id

        user_full_name = self.user_full_name

        create_user_id = self.create_user_id

        create_user_full_name = self.create_user_full_name

        create_user_type: str | Unset = UNSET
        if not isinstance(self.create_user_type, Unset):
            create_user_type = self.create_user_type.value

        update_user_id = self.update_user_id

        update_user_full_name: None | str | Unset
        if isinstance(self.update_user_full_name, Unset):
            update_user_full_name = UNSET
        else:
            update_user_full_name = self.update_user_full_name

        validated = self.validated

        validate_error: None | str | Unset
        if isinstance(self.validate_error, Unset):
            validate_error = UNSET
        else:
            validate_error = self.validate_error

        transfer_direction: str | Unset = UNSET
        if not isinstance(self.transfer_direction, Unset):
            transfer_direction = self.transfer_direction.value

        transfer_flow: str | Unset = UNSET
        if not isinstance(self.transfer_flow, Unset):
            transfer_flow = self.transfer_flow.value

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        original_transaction_id: float | None | Unset
        if isinstance(self.original_transaction_id, Unset):
            original_transaction_id = UNSET
        else:
            original_transaction_id = self.original_transaction_id

        return_transaction_id: float | None | Unset
        if isinstance(self.return_transaction_id, Unset):
            return_transaction_id = UNSET
        else:
            return_transaction_id = self.return_transaction_id

        is_return_of_return = self.is_return_of_return

        is_dishonored = self.is_dishonored

        create_date_time: str | Unset = UNSET
        if not isinstance(self.create_date_time, Unset):
            create_date_time = self.create_date_time.isoformat()

        update_date_time: str | Unset = UNSET
        if not isinstance(self.update_date_time, Unset):
            update_date_time = self.update_date_time.isoformat()

        processed_date_time: str | Unset = UNSET
        if not isinstance(self.processed_date_time, Unset):
            processed_date_time = self.processed_date_time.isoformat()

        posted_date: str | Unset = UNSET
        if not isinstance(self.posted_date, Unset):
            posted_date = self.posted_date.isoformat()

        test = self.test

        deleted = self.deleted

        batch_id = self.batch_id

        batch_external_key: None | str | Unset
        if isinstance(self.batch_external_key, Unset):
            batch_external_key = UNSET
        else:
            batch_external_key = self.batch_external_key

        data_direction: str | Unset = UNSET
        if not isinstance(self.data_direction, Unset):
            data_direction = self.data_direction.value

        comment_count = self.comment_count

        running_balance: float | None | Unset
        if isinstance(self.running_balance, Unset):
            running_balance = UNSET
        else:
            running_balance = self.running_balance

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if company_id is not UNSET:
            field_dict["company_id"] = company_id
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if user_full_name is not UNSET:
            field_dict["user_full_name"] = user_full_name
        if create_user_id is not UNSET:
            field_dict["create_user_id"] = create_user_id
        if create_user_full_name is not UNSET:
            field_dict["create_user_full_name"] = create_user_full_name
        if create_user_type is not UNSET:
            field_dict["create_user_type"] = create_user_type
        if update_user_id is not UNSET:
            field_dict["update_user_id"] = update_user_id
        if update_user_full_name is not UNSET:
            field_dict["update_user_full_name"] = update_user_full_name
        if validated is not UNSET:
            field_dict["validated"] = validated
        if validate_error is not UNSET:
            field_dict["validate_error"] = validate_error
        if transfer_direction is not UNSET:
            field_dict["transfer_direction"] = transfer_direction
        if transfer_flow is not UNSET:
            field_dict["transfer_flow"] = transfer_flow
        if state is not UNSET:
            field_dict["state"] = state
        if original_transaction_id is not UNSET:
            field_dict["original_transaction_id"] = original_transaction_id
        if return_transaction_id is not UNSET:
            field_dict["return_transaction_id"] = return_transaction_id
        if is_return_of_return is not UNSET:
            field_dict["is_return_of_return"] = is_return_of_return
        if is_dishonored is not UNSET:
            field_dict["is_dishonored"] = is_dishonored
        if create_date_time is not UNSET:
            field_dict["create_date_time"] = create_date_time
        if update_date_time is not UNSET:
            field_dict["update_date_time"] = update_date_time
        if processed_date_time is not UNSET:
            field_dict["processed_date_time"] = processed_date_time
        if posted_date is not UNSET:
            field_dict["posted_date"] = posted_date
        if test is not UNSET:
            field_dict["test"] = test
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if batch_id is not UNSET:
            field_dict["batch_id"] = batch_id
        if batch_external_key is not UNSET:
            field_dict["batch_external_key"] = batch_external_key
        if data_direction is not UNSET:
            field_dict["data_direction"] = data_direction
        if comment_count is not UNSET:
            field_dict["comment_count"] = comment_count
        if running_balance is not UNSET:
            field_dict["running_balance"] = running_balance

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_company_id(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        company_id = _parse_company_id(d.pop("company_id", UNSET))

        def _parse_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_name = _parse_company_name(d.pop("company_name", UNSET))

        user_id = d.pop("user_id", UNSET)

        user_full_name = d.pop("user_full_name", UNSET)

        create_user_id = d.pop("create_user_id", UNSET)

        create_user_full_name = d.pop("create_user_full_name", UNSET)

        _create_user_type = d.pop("create_user_type", UNSET)
        create_user_type: TransactionFieldsCreateUserType | Unset
        if isinstance(_create_user_type, Unset):
            create_user_type = UNSET
        else:
            create_user_type = TransactionFieldsCreateUserType(_create_user_type)

        update_user_id = d.pop("update_user_id", UNSET)

        def _parse_update_user_full_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        update_user_full_name = _parse_update_user_full_name(
            d.pop("update_user_full_name", UNSET)
        )

        validated = d.pop("validated", UNSET)

        def _parse_validate_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        validate_error = _parse_validate_error(d.pop("validate_error", UNSET))

        _transfer_direction = d.pop("transfer_direction", UNSET)
        transfer_direction: TransactionFieldsTransferDirection | Unset
        if isinstance(_transfer_direction, Unset):
            transfer_direction = UNSET
        else:
            transfer_direction = TransactionFieldsTransferDirection(_transfer_direction)

        _transfer_flow = d.pop("transfer_flow", UNSET)
        transfer_flow: TransactionFieldsTransferFlow | Unset
        if isinstance(_transfer_flow, Unset):
            transfer_flow = UNSET
        else:
            transfer_flow = TransactionFieldsTransferFlow(_transfer_flow)

        _state = d.pop("state", UNSET)
        state: TransactionFieldsState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = TransactionFieldsState(_state)

        def _parse_original_transaction_id(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        original_transaction_id = _parse_original_transaction_id(
            d.pop("original_transaction_id", UNSET)
        )

        def _parse_return_transaction_id(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        return_transaction_id = _parse_return_transaction_id(
            d.pop("return_transaction_id", UNSET)
        )

        is_return_of_return = d.pop("is_return_of_return", UNSET)

        is_dishonored = d.pop("is_dishonored", UNSET)

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

        _processed_date_time = d.pop("processed_date_time", UNSET)
        processed_date_time: datetime.datetime | Unset
        if isinstance(_processed_date_time, Unset):
            processed_date_time = UNSET
        else:
            processed_date_time = isoparse(_processed_date_time)

        _posted_date = d.pop("posted_date", UNSET)
        posted_date: datetime.date | Unset
        if isinstance(_posted_date, Unset):
            posted_date = UNSET
        else:
            posted_date = isoparse(_posted_date).date()

        test = d.pop("test", UNSET)

        deleted = d.pop("deleted", UNSET)

        batch_id = d.pop("batch_id", UNSET)

        def _parse_batch_external_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        batch_external_key = _parse_batch_external_key(
            d.pop("batch_external_key", UNSET)
        )

        _data_direction = d.pop("data_direction", UNSET)
        data_direction: TransactionFieldsDataDirection | Unset
        if isinstance(_data_direction, Unset):
            data_direction = UNSET
        else:
            data_direction = TransactionFieldsDataDirection(_data_direction)

        comment_count = d.pop("comment_count", UNSET)

        def _parse_running_balance(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        running_balance = _parse_running_balance(d.pop("running_balance", UNSET))

        transaction_fields = cls(
            id=id,
            company_id=company_id,
            company_name=company_name,
            user_id=user_id,
            user_full_name=user_full_name,
            create_user_id=create_user_id,
            create_user_full_name=create_user_full_name,
            create_user_type=create_user_type,
            update_user_id=update_user_id,
            update_user_full_name=update_user_full_name,
            validated=validated,
            validate_error=validate_error,
            transfer_direction=transfer_direction,
            transfer_flow=transfer_flow,
            state=state,
            original_transaction_id=original_transaction_id,
            return_transaction_id=return_transaction_id,
            is_return_of_return=is_return_of_return,
            is_dishonored=is_dishonored,
            create_date_time=create_date_time,
            update_date_time=update_date_time,
            processed_date_time=processed_date_time,
            posted_date=posted_date,
            test=test,
            deleted=deleted,
            batch_id=batch_id,
            batch_external_key=batch_external_key,
            data_direction=data_direction,
            comment_count=comment_count,
            running_balance=running_balance,
        )

        transaction_fields.additional_properties = d
        return transaction_fields

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
