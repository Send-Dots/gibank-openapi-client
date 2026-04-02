import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient
from ...client import Client
from ...models.error_body import ErrorBody
from ...models.search_transactions_create_user_type import (
    SearchTransactionsCreateUserType,
)
from ...models.search_transactions_mode import SearchTransactionsMode
from ...models.search_transactions_not_state import SearchTransactionsNotState
from ...models.search_transactions_state import SearchTransactionsState
from ...models.search_transactions_transfer_direction import (
    SearchTransactionsTransferDirection,
)
from ...models.search_transactions_transfer_type import SearchTransactionsTransferType
from ...models.search_transactions_type import SearchTransactionsType
from ...models.transaction_fields import TransactionFields
from ...types import UNSET
from ...types import Response
from ...types import Unset


def _get_kwargs(
    *,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    id: str | Unset = UNSET,
    batch_id: float | Unset = UNSET,
    batch_external_key: str | Unset = UNSET,
    type_: SearchTransactionsType | Unset = UNSET,
    transfer_direction: SearchTransactionsTransferDirection | Unset = UNSET,
    transfer_type: SearchTransactionsTransferType | Unset = UNSET,
    state: SearchTransactionsState | Unset = UNSET,
    not_state: SearchTransactionsNotState | Unset = UNSET,
    user_id: float | Unset = UNSET,
    user_full_name: str | Unset = UNSET,
    create_user_type: SearchTransactionsCreateUserType | Unset = UNSET,
    company_id: float | Unset = UNSET,
    company_name: str | Unset = UNSET,
    subtransaction_id: float | Unset = UNSET,
    create_date_from: datetime.date | Unset = UNSET,
    create_date_to: datetime.date | Unset = UNSET,
    create_date_time_from: str | Unset = UNSET,
    create_date_time_to: str | Unset = UNSET,
    posted_date_from: datetime.date | Unset = UNSET,
    posted_date_to: datetime.date | Unset = UNSET,
    amount_from: float | Unset = UNSET,
    amount_to: float | Unset = UNSET,
    test: bool | Unset = UNSET,
    deleted: bool | Unset = UNSET,
    reference: str | Unset = UNSET,
    payment_info: str | Unset = UNSET,
    origin_name: str | Unset = UNSET,
    origin_number: str | Unset = UNSET,
    destination_name: str | Unset = UNSET,
    destination_number: str | Unset = UNSET,
    trace_reference: str | Unset = UNSET,
    trace_reference_original: str | Unset = UNSET,
    trace_reference_final: str | Unset = UNSET,
    return_: bool | Unset = UNSET,
    returned: bool | Unset = UNSET,
    core_account_number: str | Unset = UNSET,
    core_account_id: str | Unset = UNSET,
    contains_virtual: bool | Unset = UNSET,
    doesnt_contain_virtual: bool | Unset = UNSET,
    mode: SearchTransactionsMode | Unset = UNSET,
    has_return: bool | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params["id"] = id

    params["batch_id"] = batch_id

    params["batch_external_key"] = batch_external_key

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    json_transfer_direction: str | Unset = UNSET
    if not isinstance(transfer_direction, Unset):
        json_transfer_direction = transfer_direction.value

    params["transfer_direction"] = json_transfer_direction

    json_transfer_type: str | Unset = UNSET
    if not isinstance(transfer_type, Unset):
        json_transfer_type = transfer_type.value

    params["transfer_type"] = json_transfer_type

    json_state: str | Unset = UNSET
    if not isinstance(state, Unset):
        json_state = state.value

    params["state"] = json_state

    json_not_state: str | Unset = UNSET
    if not isinstance(not_state, Unset):
        json_not_state = not_state.value

    params["not_state"] = json_not_state

    params["user_id"] = user_id

    params["user_full_name"] = user_full_name

    json_create_user_type: str | Unset = UNSET
    if not isinstance(create_user_type, Unset):
        json_create_user_type = create_user_type.value

    params["create_user_type"] = json_create_user_type

    params["company_id"] = company_id

    params["company_name"] = company_name

    params["subtransaction_id"] = subtransaction_id

    json_create_date_from: str | Unset = UNSET
    if not isinstance(create_date_from, Unset):
        json_create_date_from = create_date_from.isoformat()
    params["create_date_from"] = json_create_date_from

    json_create_date_to: str | Unset = UNSET
    if not isinstance(create_date_to, Unset):
        json_create_date_to = create_date_to.isoformat()
    params["create_date_to"] = json_create_date_to

    params["create_date_time_from"] = create_date_time_from

    params["create_date_time_to"] = create_date_time_to

    json_posted_date_from: str | Unset = UNSET
    if not isinstance(posted_date_from, Unset):
        json_posted_date_from = posted_date_from.isoformat()
    params["posted_date_from"] = json_posted_date_from

    json_posted_date_to: str | Unset = UNSET
    if not isinstance(posted_date_to, Unset):
        json_posted_date_to = posted_date_to.isoformat()
    params["posted_date_to"] = json_posted_date_to

    params["amount_from"] = amount_from

    params["amount_to"] = amount_to

    params["test"] = test

    params["deleted"] = deleted

    params["reference"] = reference

    params["payment_info"] = payment_info

    params["origin_name"] = origin_name

    params["origin_number"] = origin_number

    params["destination_name"] = destination_name

    params["destination_number"] = destination_number

    params["trace_reference"] = trace_reference

    params["trace_reference_original"] = trace_reference_original

    params["trace_reference_final"] = trace_reference_final

    params["return"] = return_

    params["returned"] = returned

    params["core_account_number"] = core_account_number

    params["core_account_id"] = core_account_id

    params["contains_virtual"] = contains_virtual

    params["doesnt_contain_virtual"] = doesnt_contain_virtual

    json_mode: str | Unset = UNSET
    if not isinstance(mode, Unset):
        json_mode = mode.value

    params["mode"] = json_mode

    params["has_return"] = has_return

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/transaction/search",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorBody | list[TransactionFields] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = TransactionFields.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = ErrorBody.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorBody.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorBody.from_dict(response.json())

        return response_403

    if response.status_code == 500:
        response_500 = ErrorBody.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorBody | list[TransactionFields]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    id: str | Unset = UNSET,
    batch_id: float | Unset = UNSET,
    batch_external_key: str | Unset = UNSET,
    type_: SearchTransactionsType | Unset = UNSET,
    transfer_direction: SearchTransactionsTransferDirection | Unset = UNSET,
    transfer_type: SearchTransactionsTransferType | Unset = UNSET,
    state: SearchTransactionsState | Unset = UNSET,
    not_state: SearchTransactionsNotState | Unset = UNSET,
    user_id: float | Unset = UNSET,
    user_full_name: str | Unset = UNSET,
    create_user_type: SearchTransactionsCreateUserType | Unset = UNSET,
    company_id: float | Unset = UNSET,
    company_name: str | Unset = UNSET,
    subtransaction_id: float | Unset = UNSET,
    create_date_from: datetime.date | Unset = UNSET,
    create_date_to: datetime.date | Unset = UNSET,
    create_date_time_from: str | Unset = UNSET,
    create_date_time_to: str | Unset = UNSET,
    posted_date_from: datetime.date | Unset = UNSET,
    posted_date_to: datetime.date | Unset = UNSET,
    amount_from: float | Unset = UNSET,
    amount_to: float | Unset = UNSET,
    test: bool | Unset = UNSET,
    deleted: bool | Unset = UNSET,
    reference: str | Unset = UNSET,
    payment_info: str | Unset = UNSET,
    origin_name: str | Unset = UNSET,
    origin_number: str | Unset = UNSET,
    destination_name: str | Unset = UNSET,
    destination_number: str | Unset = UNSET,
    trace_reference: str | Unset = UNSET,
    trace_reference_original: str | Unset = UNSET,
    trace_reference_final: str | Unset = UNSET,
    return_: bool | Unset = UNSET,
    returned: bool | Unset = UNSET,
    core_account_number: str | Unset = UNSET,
    core_account_id: str | Unset = UNSET,
    contains_virtual: bool | Unset = UNSET,
    doesnt_contain_virtual: bool | Unset = UNSET,
    mode: SearchTransactionsMode | Unset = UNSET,
    has_return: bool | Unset = UNSET,
) -> Response[ErrorBody | list[TransactionFields]]:
    """Transactions: Search

     Search transactions based on filters. Useful to find transactions of the past time period, or to
    check the transaction state.

    ***Requires authorization.***

    Args:
        limit (int | Unset):  Default: 100. Example: 100.
        offset (int | Unset):  Default: 0.
        id (str | Unset): The transaction ID (can be multiple (array or comma separated)) Example:
            1.
        batch_id (float | Unset): The transaction by batch ID Example: 1.
        batch_external_key (str | Unset): The transaction by batch external key Example: 1.
        type_ (SearchTransactionsType | Unset): The transaction type Example: icl.
        transfer_direction (SearchTransactionsTransferDirection | Unset): The direction of the
            transfer. `outbound` means money left your account, `inbound` means money was added to
            your account Example: outbound.
        transfer_type (SearchTransactionsTransferType | Unset): The transfer type, depends on the
            transaction type (ICL: `check/return`, ACH: `batch/return/iat_batch/iat_return/noc`, WIRE:
            `transaction/return`, WIRE20022: `transaction/return`) Example: check.
        state (SearchTransactionsState | Unset): The state of the transfer (can be multiple (array
            or comma separated)) Example: created.
        not_state (SearchTransactionsNotState | Unset): The state the transfer should not be in
            (can be multiple (array or comma separated)) Example: created.
        user_id (float | Unset): The user ID Example: 1.
        user_full_name (str | Unset): The user full name (contains, case insensitive) Example: Max
            Mustermann.
        create_user_type (SearchTransactionsCreateUserType | Unset): The user type Example:
            client.
        company_id (float | Unset): The company ID Example: 1.
        company_name (str | Unset): The company name (contains, case insensitive) Example: ABC
            Bank.
        subtransaction_id (float | Unset): The subtransaction ID. Deleted links are excluded.
            Example: 1.
        create_date_from (datetime.date | Unset): The transaction create date (>=) (Please use
            UTC) Example: 2024-02-04.
        create_date_to (datetime.date | Unset): The transaction create date (<) (Please use UTC)
            Example: 2024-02-04.
        create_date_time_from (str | Unset): The transaction create date time (>=) (Please use the
            zero UTC offset (Zulu) format) Example: 2024-02-04T00:00:00.000Z.
        create_date_time_to (str | Unset): The transaction create date time (<) (Please use the
            zero UTC offset (Zulu) format) Example: 2024-02-04T23:59:59.000Z.
        posted_date_from (datetime.date | Unset): The transaction posted date (>=) (Please use
            UTC) Example: 2024-02-04.
        posted_date_to (datetime.date | Unset): The transaction posted date (<) (Please use UTC)
            Example: 2024-02-04.
        amount_from (float | Unset): The transaction amount (>=) Example: 500.
        amount_to (float | Unset): The transaction amount (<) Example: 2000.
        test (bool | Unset): The transaction test state Example: True.
        deleted (bool | Unset): The transaction deleted flag
        reference (str | Unset): The transaction reference (contains, case insensitive, please
            combine with `create_date_from`) (can be multiple) Example: Test 01.
        payment_info (str | Unset): The transaction payment_info (contains, case insensitive,
            please combine with `create_date_from`) (can be multiple) Example: Test 01.
        origin_name (str | Unset): The transaction origin routing/account name (contains, please
            combine with `create_date_from`, case insensitive) Example: Test 01.
        origin_number (str | Unset): The transaction origin routing/account number (contains,
            please combine with `create_date_from`, case insensitive) Example: 0123456789.
        destination_name (str | Unset): The transaction destination routing/account name
            (contains, please combine with `create_date_from`, case insensitive) Example: Test 01.
        destination_number (str | Unset): The transaction destination routing/account number
            (contains, please combine with `create_date_from`, case insensitive) Example: 0123456789.
        trace_reference (str | Unset): The trace reference Example: 123456789.
        trace_reference_original (str | Unset): The trace reference of the original transaction
            (For Returns; matches with `trace_reference` or `trace_reference_final`) Example:
            123456789.
        trace_reference_final (str | Unset): The final trace reference Example: 123456789.
        return_ (bool | Unset): If the transaction is a return
        returned (bool | Unset): If the transaction is returned
        core_account_number (str | Unset): The transaction origin or destination core account
            number. Example: 0123456789.
        core_account_id (str | Unset): Same as core_account_number but using the user_account ID.
            Example: 123.
        contains_virtual (bool | Unset): Signifies that the transaction has a virtual origin
            account and or virtual destination account Example: True.
        doesnt_contain_virtual (bool | Unset): Signifies that the transaction does not have a
            virtual origin account or virtual destination account Example: True.
        mode (SearchTransactionsMode | Unset): How the transaction data should be returned.
            Use "balance" mode to get the transactions in the order they were posted to the core, with
            running balance.
            Transactions might show up multiple times in this mode if they are linked to more than one
            core transaction.
             Example: balance.
        has_return (bool | Unset): Signifies that the transaction has been returned Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | list[TransactionFields]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        id=id,
        batch_id=batch_id,
        batch_external_key=batch_external_key,
        type_=type_,
        transfer_direction=transfer_direction,
        transfer_type=transfer_type,
        state=state,
        not_state=not_state,
        user_id=user_id,
        user_full_name=user_full_name,
        create_user_type=create_user_type,
        company_id=company_id,
        company_name=company_name,
        subtransaction_id=subtransaction_id,
        create_date_from=create_date_from,
        create_date_to=create_date_to,
        create_date_time_from=create_date_time_from,
        create_date_time_to=create_date_time_to,
        posted_date_from=posted_date_from,
        posted_date_to=posted_date_to,
        amount_from=amount_from,
        amount_to=amount_to,
        test=test,
        deleted=deleted,
        reference=reference,
        payment_info=payment_info,
        origin_name=origin_name,
        origin_number=origin_number,
        destination_name=destination_name,
        destination_number=destination_number,
        trace_reference=trace_reference,
        trace_reference_original=trace_reference_original,
        trace_reference_final=trace_reference_final,
        return_=return_,
        returned=returned,
        core_account_number=core_account_number,
        core_account_id=core_account_id,
        contains_virtual=contains_virtual,
        doesnt_contain_virtual=doesnt_contain_virtual,
        mode=mode,
        has_return=has_return,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    id: str | Unset = UNSET,
    batch_id: float | Unset = UNSET,
    batch_external_key: str | Unset = UNSET,
    type_: SearchTransactionsType | Unset = UNSET,
    transfer_direction: SearchTransactionsTransferDirection | Unset = UNSET,
    transfer_type: SearchTransactionsTransferType | Unset = UNSET,
    state: SearchTransactionsState | Unset = UNSET,
    not_state: SearchTransactionsNotState | Unset = UNSET,
    user_id: float | Unset = UNSET,
    user_full_name: str | Unset = UNSET,
    create_user_type: SearchTransactionsCreateUserType | Unset = UNSET,
    company_id: float | Unset = UNSET,
    company_name: str | Unset = UNSET,
    subtransaction_id: float | Unset = UNSET,
    create_date_from: datetime.date | Unset = UNSET,
    create_date_to: datetime.date | Unset = UNSET,
    create_date_time_from: str | Unset = UNSET,
    create_date_time_to: str | Unset = UNSET,
    posted_date_from: datetime.date | Unset = UNSET,
    posted_date_to: datetime.date | Unset = UNSET,
    amount_from: float | Unset = UNSET,
    amount_to: float | Unset = UNSET,
    test: bool | Unset = UNSET,
    deleted: bool | Unset = UNSET,
    reference: str | Unset = UNSET,
    payment_info: str | Unset = UNSET,
    origin_name: str | Unset = UNSET,
    origin_number: str | Unset = UNSET,
    destination_name: str | Unset = UNSET,
    destination_number: str | Unset = UNSET,
    trace_reference: str | Unset = UNSET,
    trace_reference_original: str | Unset = UNSET,
    trace_reference_final: str | Unset = UNSET,
    return_: bool | Unset = UNSET,
    returned: bool | Unset = UNSET,
    core_account_number: str | Unset = UNSET,
    core_account_id: str | Unset = UNSET,
    contains_virtual: bool | Unset = UNSET,
    doesnt_contain_virtual: bool | Unset = UNSET,
    mode: SearchTransactionsMode | Unset = UNSET,
    has_return: bool | Unset = UNSET,
) -> ErrorBody | list[TransactionFields] | None:
    """Transactions: Search

     Search transactions based on filters. Useful to find transactions of the past time period, or to
    check the transaction state.

    ***Requires authorization.***

    Args:
        limit (int | Unset):  Default: 100. Example: 100.
        offset (int | Unset):  Default: 0.
        id (str | Unset): The transaction ID (can be multiple (array or comma separated)) Example:
            1.
        batch_id (float | Unset): The transaction by batch ID Example: 1.
        batch_external_key (str | Unset): The transaction by batch external key Example: 1.
        type_ (SearchTransactionsType | Unset): The transaction type Example: icl.
        transfer_direction (SearchTransactionsTransferDirection | Unset): The direction of the
            transfer. `outbound` means money left your account, `inbound` means money was added to
            your account Example: outbound.
        transfer_type (SearchTransactionsTransferType | Unset): The transfer type, depends on the
            transaction type (ICL: `check/return`, ACH: `batch/return/iat_batch/iat_return/noc`, WIRE:
            `transaction/return`, WIRE20022: `transaction/return`) Example: check.
        state (SearchTransactionsState | Unset): The state of the transfer (can be multiple (array
            or comma separated)) Example: created.
        not_state (SearchTransactionsNotState | Unset): The state the transfer should not be in
            (can be multiple (array or comma separated)) Example: created.
        user_id (float | Unset): The user ID Example: 1.
        user_full_name (str | Unset): The user full name (contains, case insensitive) Example: Max
            Mustermann.
        create_user_type (SearchTransactionsCreateUserType | Unset): The user type Example:
            client.
        company_id (float | Unset): The company ID Example: 1.
        company_name (str | Unset): The company name (contains, case insensitive) Example: ABC
            Bank.
        subtransaction_id (float | Unset): The subtransaction ID. Deleted links are excluded.
            Example: 1.
        create_date_from (datetime.date | Unset): The transaction create date (>=) (Please use
            UTC) Example: 2024-02-04.
        create_date_to (datetime.date | Unset): The transaction create date (<) (Please use UTC)
            Example: 2024-02-04.
        create_date_time_from (str | Unset): The transaction create date time (>=) (Please use the
            zero UTC offset (Zulu) format) Example: 2024-02-04T00:00:00.000Z.
        create_date_time_to (str | Unset): The transaction create date time (<) (Please use the
            zero UTC offset (Zulu) format) Example: 2024-02-04T23:59:59.000Z.
        posted_date_from (datetime.date | Unset): The transaction posted date (>=) (Please use
            UTC) Example: 2024-02-04.
        posted_date_to (datetime.date | Unset): The transaction posted date (<) (Please use UTC)
            Example: 2024-02-04.
        amount_from (float | Unset): The transaction amount (>=) Example: 500.
        amount_to (float | Unset): The transaction amount (<) Example: 2000.
        test (bool | Unset): The transaction test state Example: True.
        deleted (bool | Unset): The transaction deleted flag
        reference (str | Unset): The transaction reference (contains, case insensitive, please
            combine with `create_date_from`) (can be multiple) Example: Test 01.
        payment_info (str | Unset): The transaction payment_info (contains, case insensitive,
            please combine with `create_date_from`) (can be multiple) Example: Test 01.
        origin_name (str | Unset): The transaction origin routing/account name (contains, please
            combine with `create_date_from`, case insensitive) Example: Test 01.
        origin_number (str | Unset): The transaction origin routing/account number (contains,
            please combine with `create_date_from`, case insensitive) Example: 0123456789.
        destination_name (str | Unset): The transaction destination routing/account name
            (contains, please combine with `create_date_from`, case insensitive) Example: Test 01.
        destination_number (str | Unset): The transaction destination routing/account number
            (contains, please combine with `create_date_from`, case insensitive) Example: 0123456789.
        trace_reference (str | Unset): The trace reference Example: 123456789.
        trace_reference_original (str | Unset): The trace reference of the original transaction
            (For Returns; matches with `trace_reference` or `trace_reference_final`) Example:
            123456789.
        trace_reference_final (str | Unset): The final trace reference Example: 123456789.
        return_ (bool | Unset): If the transaction is a return
        returned (bool | Unset): If the transaction is returned
        core_account_number (str | Unset): The transaction origin or destination core account
            number. Example: 0123456789.
        core_account_id (str | Unset): Same as core_account_number but using the user_account ID.
            Example: 123.
        contains_virtual (bool | Unset): Signifies that the transaction has a virtual origin
            account and or virtual destination account Example: True.
        doesnt_contain_virtual (bool | Unset): Signifies that the transaction does not have a
            virtual origin account or virtual destination account Example: True.
        mode (SearchTransactionsMode | Unset): How the transaction data should be returned.
            Use "balance" mode to get the transactions in the order they were posted to the core, with
            running balance.
            Transactions might show up multiple times in this mode if they are linked to more than one
            core transaction.
             Example: balance.
        has_return (bool | Unset): Signifies that the transaction has been returned Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | list[TransactionFields]
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        id=id,
        batch_id=batch_id,
        batch_external_key=batch_external_key,
        type_=type_,
        transfer_direction=transfer_direction,
        transfer_type=transfer_type,
        state=state,
        not_state=not_state,
        user_id=user_id,
        user_full_name=user_full_name,
        create_user_type=create_user_type,
        company_id=company_id,
        company_name=company_name,
        subtransaction_id=subtransaction_id,
        create_date_from=create_date_from,
        create_date_to=create_date_to,
        create_date_time_from=create_date_time_from,
        create_date_time_to=create_date_time_to,
        posted_date_from=posted_date_from,
        posted_date_to=posted_date_to,
        amount_from=amount_from,
        amount_to=amount_to,
        test=test,
        deleted=deleted,
        reference=reference,
        payment_info=payment_info,
        origin_name=origin_name,
        origin_number=origin_number,
        destination_name=destination_name,
        destination_number=destination_number,
        trace_reference=trace_reference,
        trace_reference_original=trace_reference_original,
        trace_reference_final=trace_reference_final,
        return_=return_,
        returned=returned,
        core_account_number=core_account_number,
        core_account_id=core_account_id,
        contains_virtual=contains_virtual,
        doesnt_contain_virtual=doesnt_contain_virtual,
        mode=mode,
        has_return=has_return,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    id: str | Unset = UNSET,
    batch_id: float | Unset = UNSET,
    batch_external_key: str | Unset = UNSET,
    type_: SearchTransactionsType | Unset = UNSET,
    transfer_direction: SearchTransactionsTransferDirection | Unset = UNSET,
    transfer_type: SearchTransactionsTransferType | Unset = UNSET,
    state: SearchTransactionsState | Unset = UNSET,
    not_state: SearchTransactionsNotState | Unset = UNSET,
    user_id: float | Unset = UNSET,
    user_full_name: str | Unset = UNSET,
    create_user_type: SearchTransactionsCreateUserType | Unset = UNSET,
    company_id: float | Unset = UNSET,
    company_name: str | Unset = UNSET,
    subtransaction_id: float | Unset = UNSET,
    create_date_from: datetime.date | Unset = UNSET,
    create_date_to: datetime.date | Unset = UNSET,
    create_date_time_from: str | Unset = UNSET,
    create_date_time_to: str | Unset = UNSET,
    posted_date_from: datetime.date | Unset = UNSET,
    posted_date_to: datetime.date | Unset = UNSET,
    amount_from: float | Unset = UNSET,
    amount_to: float | Unset = UNSET,
    test: bool | Unset = UNSET,
    deleted: bool | Unset = UNSET,
    reference: str | Unset = UNSET,
    payment_info: str | Unset = UNSET,
    origin_name: str | Unset = UNSET,
    origin_number: str | Unset = UNSET,
    destination_name: str | Unset = UNSET,
    destination_number: str | Unset = UNSET,
    trace_reference: str | Unset = UNSET,
    trace_reference_original: str | Unset = UNSET,
    trace_reference_final: str | Unset = UNSET,
    return_: bool | Unset = UNSET,
    returned: bool | Unset = UNSET,
    core_account_number: str | Unset = UNSET,
    core_account_id: str | Unset = UNSET,
    contains_virtual: bool | Unset = UNSET,
    doesnt_contain_virtual: bool | Unset = UNSET,
    mode: SearchTransactionsMode | Unset = UNSET,
    has_return: bool | Unset = UNSET,
) -> Response[ErrorBody | list[TransactionFields]]:
    """Transactions: Search

     Search transactions based on filters. Useful to find transactions of the past time period, or to
    check the transaction state.

    ***Requires authorization.***

    Args:
        limit (int | Unset):  Default: 100. Example: 100.
        offset (int | Unset):  Default: 0.
        id (str | Unset): The transaction ID (can be multiple (array or comma separated)) Example:
            1.
        batch_id (float | Unset): The transaction by batch ID Example: 1.
        batch_external_key (str | Unset): The transaction by batch external key Example: 1.
        type_ (SearchTransactionsType | Unset): The transaction type Example: icl.
        transfer_direction (SearchTransactionsTransferDirection | Unset): The direction of the
            transfer. `outbound` means money left your account, `inbound` means money was added to
            your account Example: outbound.
        transfer_type (SearchTransactionsTransferType | Unset): The transfer type, depends on the
            transaction type (ICL: `check/return`, ACH: `batch/return/iat_batch/iat_return/noc`, WIRE:
            `transaction/return`, WIRE20022: `transaction/return`) Example: check.
        state (SearchTransactionsState | Unset): The state of the transfer (can be multiple (array
            or comma separated)) Example: created.
        not_state (SearchTransactionsNotState | Unset): The state the transfer should not be in
            (can be multiple (array or comma separated)) Example: created.
        user_id (float | Unset): The user ID Example: 1.
        user_full_name (str | Unset): The user full name (contains, case insensitive) Example: Max
            Mustermann.
        create_user_type (SearchTransactionsCreateUserType | Unset): The user type Example:
            client.
        company_id (float | Unset): The company ID Example: 1.
        company_name (str | Unset): The company name (contains, case insensitive) Example: ABC
            Bank.
        subtransaction_id (float | Unset): The subtransaction ID. Deleted links are excluded.
            Example: 1.
        create_date_from (datetime.date | Unset): The transaction create date (>=) (Please use
            UTC) Example: 2024-02-04.
        create_date_to (datetime.date | Unset): The transaction create date (<) (Please use UTC)
            Example: 2024-02-04.
        create_date_time_from (str | Unset): The transaction create date time (>=) (Please use the
            zero UTC offset (Zulu) format) Example: 2024-02-04T00:00:00.000Z.
        create_date_time_to (str | Unset): The transaction create date time (<) (Please use the
            zero UTC offset (Zulu) format) Example: 2024-02-04T23:59:59.000Z.
        posted_date_from (datetime.date | Unset): The transaction posted date (>=) (Please use
            UTC) Example: 2024-02-04.
        posted_date_to (datetime.date | Unset): The transaction posted date (<) (Please use UTC)
            Example: 2024-02-04.
        amount_from (float | Unset): The transaction amount (>=) Example: 500.
        amount_to (float | Unset): The transaction amount (<) Example: 2000.
        test (bool | Unset): The transaction test state Example: True.
        deleted (bool | Unset): The transaction deleted flag
        reference (str | Unset): The transaction reference (contains, case insensitive, please
            combine with `create_date_from`) (can be multiple) Example: Test 01.
        payment_info (str | Unset): The transaction payment_info (contains, case insensitive,
            please combine with `create_date_from`) (can be multiple) Example: Test 01.
        origin_name (str | Unset): The transaction origin routing/account name (contains, please
            combine with `create_date_from`, case insensitive) Example: Test 01.
        origin_number (str | Unset): The transaction origin routing/account number (contains,
            please combine with `create_date_from`, case insensitive) Example: 0123456789.
        destination_name (str | Unset): The transaction destination routing/account name
            (contains, please combine with `create_date_from`, case insensitive) Example: Test 01.
        destination_number (str | Unset): The transaction destination routing/account number
            (contains, please combine with `create_date_from`, case insensitive) Example: 0123456789.
        trace_reference (str | Unset): The trace reference Example: 123456789.
        trace_reference_original (str | Unset): The trace reference of the original transaction
            (For Returns; matches with `trace_reference` or `trace_reference_final`) Example:
            123456789.
        trace_reference_final (str | Unset): The final trace reference Example: 123456789.
        return_ (bool | Unset): If the transaction is a return
        returned (bool | Unset): If the transaction is returned
        core_account_number (str | Unset): The transaction origin or destination core account
            number. Example: 0123456789.
        core_account_id (str | Unset): Same as core_account_number but using the user_account ID.
            Example: 123.
        contains_virtual (bool | Unset): Signifies that the transaction has a virtual origin
            account and or virtual destination account Example: True.
        doesnt_contain_virtual (bool | Unset): Signifies that the transaction does not have a
            virtual origin account or virtual destination account Example: True.
        mode (SearchTransactionsMode | Unset): How the transaction data should be returned.
            Use "balance" mode to get the transactions in the order they were posted to the core, with
            running balance.
            Transactions might show up multiple times in this mode if they are linked to more than one
            core transaction.
             Example: balance.
        has_return (bool | Unset): Signifies that the transaction has been returned Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | list[TransactionFields]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        id=id,
        batch_id=batch_id,
        batch_external_key=batch_external_key,
        type_=type_,
        transfer_direction=transfer_direction,
        transfer_type=transfer_type,
        state=state,
        not_state=not_state,
        user_id=user_id,
        user_full_name=user_full_name,
        create_user_type=create_user_type,
        company_id=company_id,
        company_name=company_name,
        subtransaction_id=subtransaction_id,
        create_date_from=create_date_from,
        create_date_to=create_date_to,
        create_date_time_from=create_date_time_from,
        create_date_time_to=create_date_time_to,
        posted_date_from=posted_date_from,
        posted_date_to=posted_date_to,
        amount_from=amount_from,
        amount_to=amount_to,
        test=test,
        deleted=deleted,
        reference=reference,
        payment_info=payment_info,
        origin_name=origin_name,
        origin_number=origin_number,
        destination_name=destination_name,
        destination_number=destination_number,
        trace_reference=trace_reference,
        trace_reference_original=trace_reference_original,
        trace_reference_final=trace_reference_final,
        return_=return_,
        returned=returned,
        core_account_number=core_account_number,
        core_account_id=core_account_id,
        contains_virtual=contains_virtual,
        doesnt_contain_virtual=doesnt_contain_virtual,
        mode=mode,
        has_return=has_return,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    id: str | Unset = UNSET,
    batch_id: float | Unset = UNSET,
    batch_external_key: str | Unset = UNSET,
    type_: SearchTransactionsType | Unset = UNSET,
    transfer_direction: SearchTransactionsTransferDirection | Unset = UNSET,
    transfer_type: SearchTransactionsTransferType | Unset = UNSET,
    state: SearchTransactionsState | Unset = UNSET,
    not_state: SearchTransactionsNotState | Unset = UNSET,
    user_id: float | Unset = UNSET,
    user_full_name: str | Unset = UNSET,
    create_user_type: SearchTransactionsCreateUserType | Unset = UNSET,
    company_id: float | Unset = UNSET,
    company_name: str | Unset = UNSET,
    subtransaction_id: float | Unset = UNSET,
    create_date_from: datetime.date | Unset = UNSET,
    create_date_to: datetime.date | Unset = UNSET,
    create_date_time_from: str | Unset = UNSET,
    create_date_time_to: str | Unset = UNSET,
    posted_date_from: datetime.date | Unset = UNSET,
    posted_date_to: datetime.date | Unset = UNSET,
    amount_from: float | Unset = UNSET,
    amount_to: float | Unset = UNSET,
    test: bool | Unset = UNSET,
    deleted: bool | Unset = UNSET,
    reference: str | Unset = UNSET,
    payment_info: str | Unset = UNSET,
    origin_name: str | Unset = UNSET,
    origin_number: str | Unset = UNSET,
    destination_name: str | Unset = UNSET,
    destination_number: str | Unset = UNSET,
    trace_reference: str | Unset = UNSET,
    trace_reference_original: str | Unset = UNSET,
    trace_reference_final: str | Unset = UNSET,
    return_: bool | Unset = UNSET,
    returned: bool | Unset = UNSET,
    core_account_number: str | Unset = UNSET,
    core_account_id: str | Unset = UNSET,
    contains_virtual: bool | Unset = UNSET,
    doesnt_contain_virtual: bool | Unset = UNSET,
    mode: SearchTransactionsMode | Unset = UNSET,
    has_return: bool | Unset = UNSET,
) -> ErrorBody | list[TransactionFields] | None:
    """Transactions: Search

     Search transactions based on filters. Useful to find transactions of the past time period, or to
    check the transaction state.

    ***Requires authorization.***

    Args:
        limit (int | Unset):  Default: 100. Example: 100.
        offset (int | Unset):  Default: 0.
        id (str | Unset): The transaction ID (can be multiple (array or comma separated)) Example:
            1.
        batch_id (float | Unset): The transaction by batch ID Example: 1.
        batch_external_key (str | Unset): The transaction by batch external key Example: 1.
        type_ (SearchTransactionsType | Unset): The transaction type Example: icl.
        transfer_direction (SearchTransactionsTransferDirection | Unset): The direction of the
            transfer. `outbound` means money left your account, `inbound` means money was added to
            your account Example: outbound.
        transfer_type (SearchTransactionsTransferType | Unset): The transfer type, depends on the
            transaction type (ICL: `check/return`, ACH: `batch/return/iat_batch/iat_return/noc`, WIRE:
            `transaction/return`, WIRE20022: `transaction/return`) Example: check.
        state (SearchTransactionsState | Unset): The state of the transfer (can be multiple (array
            or comma separated)) Example: created.
        not_state (SearchTransactionsNotState | Unset): The state the transfer should not be in
            (can be multiple (array or comma separated)) Example: created.
        user_id (float | Unset): The user ID Example: 1.
        user_full_name (str | Unset): The user full name (contains, case insensitive) Example: Max
            Mustermann.
        create_user_type (SearchTransactionsCreateUserType | Unset): The user type Example:
            client.
        company_id (float | Unset): The company ID Example: 1.
        company_name (str | Unset): The company name (contains, case insensitive) Example: ABC
            Bank.
        subtransaction_id (float | Unset): The subtransaction ID. Deleted links are excluded.
            Example: 1.
        create_date_from (datetime.date | Unset): The transaction create date (>=) (Please use
            UTC) Example: 2024-02-04.
        create_date_to (datetime.date | Unset): The transaction create date (<) (Please use UTC)
            Example: 2024-02-04.
        create_date_time_from (str | Unset): The transaction create date time (>=) (Please use the
            zero UTC offset (Zulu) format) Example: 2024-02-04T00:00:00.000Z.
        create_date_time_to (str | Unset): The transaction create date time (<) (Please use the
            zero UTC offset (Zulu) format) Example: 2024-02-04T23:59:59.000Z.
        posted_date_from (datetime.date | Unset): The transaction posted date (>=) (Please use
            UTC) Example: 2024-02-04.
        posted_date_to (datetime.date | Unset): The transaction posted date (<) (Please use UTC)
            Example: 2024-02-04.
        amount_from (float | Unset): The transaction amount (>=) Example: 500.
        amount_to (float | Unset): The transaction amount (<) Example: 2000.
        test (bool | Unset): The transaction test state Example: True.
        deleted (bool | Unset): The transaction deleted flag
        reference (str | Unset): The transaction reference (contains, case insensitive, please
            combine with `create_date_from`) (can be multiple) Example: Test 01.
        payment_info (str | Unset): The transaction payment_info (contains, case insensitive,
            please combine with `create_date_from`) (can be multiple) Example: Test 01.
        origin_name (str | Unset): The transaction origin routing/account name (contains, please
            combine with `create_date_from`, case insensitive) Example: Test 01.
        origin_number (str | Unset): The transaction origin routing/account number (contains,
            please combine with `create_date_from`, case insensitive) Example: 0123456789.
        destination_name (str | Unset): The transaction destination routing/account name
            (contains, please combine with `create_date_from`, case insensitive) Example: Test 01.
        destination_number (str | Unset): The transaction destination routing/account number
            (contains, please combine with `create_date_from`, case insensitive) Example: 0123456789.
        trace_reference (str | Unset): The trace reference Example: 123456789.
        trace_reference_original (str | Unset): The trace reference of the original transaction
            (For Returns; matches with `trace_reference` or `trace_reference_final`) Example:
            123456789.
        trace_reference_final (str | Unset): The final trace reference Example: 123456789.
        return_ (bool | Unset): If the transaction is a return
        returned (bool | Unset): If the transaction is returned
        core_account_number (str | Unset): The transaction origin or destination core account
            number. Example: 0123456789.
        core_account_id (str | Unset): Same as core_account_number but using the user_account ID.
            Example: 123.
        contains_virtual (bool | Unset): Signifies that the transaction has a virtual origin
            account and or virtual destination account Example: True.
        doesnt_contain_virtual (bool | Unset): Signifies that the transaction does not have a
            virtual origin account or virtual destination account Example: True.
        mode (SearchTransactionsMode | Unset): How the transaction data should be returned.
            Use "balance" mode to get the transactions in the order they were posted to the core, with
            running balance.
            Transactions might show up multiple times in this mode if they are linked to more than one
            core transaction.
             Example: balance.
        has_return (bool | Unset): Signifies that the transaction has been returned Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | list[TransactionFields]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            id=id,
            batch_id=batch_id,
            batch_external_key=batch_external_key,
            type_=type_,
            transfer_direction=transfer_direction,
            transfer_type=transfer_type,
            state=state,
            not_state=not_state,
            user_id=user_id,
            user_full_name=user_full_name,
            create_user_type=create_user_type,
            company_id=company_id,
            company_name=company_name,
            subtransaction_id=subtransaction_id,
            create_date_from=create_date_from,
            create_date_to=create_date_to,
            create_date_time_from=create_date_time_from,
            create_date_time_to=create_date_time_to,
            posted_date_from=posted_date_from,
            posted_date_to=posted_date_to,
            amount_from=amount_from,
            amount_to=amount_to,
            test=test,
            deleted=deleted,
            reference=reference,
            payment_info=payment_info,
            origin_name=origin_name,
            origin_number=origin_number,
            destination_name=destination_name,
            destination_number=destination_number,
            trace_reference=trace_reference,
            trace_reference_original=trace_reference_original,
            trace_reference_final=trace_reference_final,
            return_=return_,
            returned=returned,
            core_account_number=core_account_number,
            core_account_id=core_account_id,
            contains_virtual=contains_virtual,
            doesnt_contain_virtual=doesnt_contain_virtual,
            mode=mode,
            has_return=has_return,
        )
    ).parsed
