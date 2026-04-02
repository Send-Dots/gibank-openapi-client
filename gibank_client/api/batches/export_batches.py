import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient
from ...client import Client
from ...models.error_body import ErrorBody
from ...models.export_batches_create_user_type import ExportBatchesCreateUserType
from ...models.export_batches_export_type import ExportBatchesExportType
from ...models.export_batches_response import ExportBatchesResponse
from ...models.export_batches_state import ExportBatchesState
from ...models.export_batches_type import ExportBatchesType
from ...types import UNSET
from ...types import Response
from ...types import Unset


def _get_kwargs(
    *,
    export_type: ExportBatchesExportType,
    limit: int | Unset = 1000,
    offset: int | Unset = 0,
    id: str | Unset = UNSET,
    type_: ExportBatchesType | Unset = UNSET,
    state: ExportBatchesState | Unset = UNSET,
    external_key: str | Unset = UNSET,
    create_user_type: ExportBatchesCreateUserType | Unset = UNSET,
    uploaded_filename: str | Unset = UNSET,
    contains_virtual_transactions: bool | Unset = UNSET,
    contains_transactions_with_routing_number: str | Unset = UNSET,
    doesnt_contain_transactions_with_routing_number: str | Unset = UNSET,
    create_date_from: datetime.date | Unset = UNSET,
    create_date_to: datetime.date | Unset = UNSET,
    create_date_time_from: str | Unset = UNSET,
    create_date_time_to: str | Unset = UNSET,
    test: bool | Unset = UNSET,
    contains_return_transactions: bool | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_export_type = export_type.value
    params["export_type"] = json_export_type

    params["limit"] = limit

    params["offset"] = offset

    params["id"] = id

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    json_state: str | Unset = UNSET
    if not isinstance(state, Unset):
        json_state = state.value

    params["state"] = json_state

    params["external_key"] = external_key

    json_create_user_type: str | Unset = UNSET
    if not isinstance(create_user_type, Unset):
        json_create_user_type = create_user_type.value

    params["create_user_type"] = json_create_user_type

    params["uploaded_filename"] = uploaded_filename

    params["contains_virtual_transactions"] = contains_virtual_transactions

    params["contains_transactions_with_routing_number"] = (
        contains_transactions_with_routing_number
    )

    params["doesnt_contain_transactions_with_routing_number"] = (
        doesnt_contain_transactions_with_routing_number
    )

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

    params["test"] = test

    params["contains_return_transactions"] = contains_return_transactions

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/batch/export",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorBody | ExportBatchesResponse | None:
    if response.status_code == 200:
        response_200 = ExportBatchesResponse.from_dict(response.json())

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
) -> Response[ErrorBody | ExportBatchesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    export_type: ExportBatchesExportType,
    limit: int | Unset = 1000,
    offset: int | Unset = 0,
    id: str | Unset = UNSET,
    type_: ExportBatchesType | Unset = UNSET,
    state: ExportBatchesState | Unset = UNSET,
    external_key: str | Unset = UNSET,
    create_user_type: ExportBatchesCreateUserType | Unset = UNSET,
    uploaded_filename: str | Unset = UNSET,
    contains_virtual_transactions: bool | Unset = UNSET,
    contains_transactions_with_routing_number: str | Unset = UNSET,
    doesnt_contain_transactions_with_routing_number: str | Unset = UNSET,
    create_date_from: datetime.date | Unset = UNSET,
    create_date_to: datetime.date | Unset = UNSET,
    create_date_time_from: str | Unset = UNSET,
    create_date_time_to: str | Unset = UNSET,
    test: bool | Unset = UNSET,
    contains_return_transactions: bool | Unset = UNSET,
) -> Response[ErrorBody | ExportBatchesResponse]:
    """Batches: Export

     Export batches in differnt formats based on their IDs. Useful for any kind of reporting.
    Might be a ZIP file if the export results in multiple files.

    For Fintech clients, access is restricted to batches where all transactions belong to their company.


    ***Dates and Date Times are in UTC!***


    ***Requires authorization.***

    Args:
        export_type (ExportBatchesExportType):  Example: csv.
        limit (int | Unset):  Default: 1000. Example: 1000.
        offset (int | Unset):  Default: 0.
        id (str | Unset): The batch ID (can be multiple (array or comma separated)) Example: 1.
        type_ (ExportBatchesType | Unset): The batch type Example: icl.
        state (ExportBatchesState | Unset): The state of the batch Example: created.
        external_key (str | Unset): The external_key of the batch Example: ABC123456789.
        create_user_type (ExportBatchesCreateUserType | Unset): The user type Example: client.
        uploaded_filename (str | Unset): The uploaded_filename of the batch (contains, case
            insensitive, please combine with `create_date_from`) Example: merged_batch_id_123.ach.
        contains_virtual_transactions (bool | Unset): Signifies that virtual accounts are expected
            in all transactions
        contains_transactions_with_routing_number (str | Unset): Checks if the provided routing
            number is in the batch (can be multiple) Example: 123456789.
        doesnt_contain_transactions_with_routing_number (str | Unset): Checks if the provided
            routing number is not in the batch (can be multiple) Example: 123456789.
        create_date_from (datetime.date | Unset): The batch create date (>=) (Please use UTC)
            Example: 2024-02-04.
        create_date_to (datetime.date | Unset): The batch create date (<) (Please use UTC)
            Example: 2024-02-04.
        create_date_time_from (str | Unset): The batch create date time (>=) (Please use the zero
            UTC offset (Zulu) format) Example: 2024-02-04T00:00:00.000Z.
        create_date_time_to (str | Unset): The batch create date time (<) (Please use the zero UTC
            offset (Zulu) format) Example: 2024-02-04T23:59:59.000Z.
        test (bool | Unset): The batch test state Example: True.
        contains_return_transactions (bool | Unset): Filter batches that contain return
            transactions (transfer_type 'return' or 'iat_return') Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | ExportBatchesResponse]
    """

    kwargs = _get_kwargs(
        export_type=export_type,
        limit=limit,
        offset=offset,
        id=id,
        type_=type_,
        state=state,
        external_key=external_key,
        create_user_type=create_user_type,
        uploaded_filename=uploaded_filename,
        contains_virtual_transactions=contains_virtual_transactions,
        contains_transactions_with_routing_number=contains_transactions_with_routing_number,
        doesnt_contain_transactions_with_routing_number=doesnt_contain_transactions_with_routing_number,
        create_date_from=create_date_from,
        create_date_to=create_date_to,
        create_date_time_from=create_date_time_from,
        create_date_time_to=create_date_time_to,
        test=test,
        contains_return_transactions=contains_return_transactions,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    export_type: ExportBatchesExportType,
    limit: int | Unset = 1000,
    offset: int | Unset = 0,
    id: str | Unset = UNSET,
    type_: ExportBatchesType | Unset = UNSET,
    state: ExportBatchesState | Unset = UNSET,
    external_key: str | Unset = UNSET,
    create_user_type: ExportBatchesCreateUserType | Unset = UNSET,
    uploaded_filename: str | Unset = UNSET,
    contains_virtual_transactions: bool | Unset = UNSET,
    contains_transactions_with_routing_number: str | Unset = UNSET,
    doesnt_contain_transactions_with_routing_number: str | Unset = UNSET,
    create_date_from: datetime.date | Unset = UNSET,
    create_date_to: datetime.date | Unset = UNSET,
    create_date_time_from: str | Unset = UNSET,
    create_date_time_to: str | Unset = UNSET,
    test: bool | Unset = UNSET,
    contains_return_transactions: bool | Unset = UNSET,
) -> ErrorBody | ExportBatchesResponse | None:
    """Batches: Export

     Export batches in differnt formats based on their IDs. Useful for any kind of reporting.
    Might be a ZIP file if the export results in multiple files.

    For Fintech clients, access is restricted to batches where all transactions belong to their company.


    ***Dates and Date Times are in UTC!***


    ***Requires authorization.***

    Args:
        export_type (ExportBatchesExportType):  Example: csv.
        limit (int | Unset):  Default: 1000. Example: 1000.
        offset (int | Unset):  Default: 0.
        id (str | Unset): The batch ID (can be multiple (array or comma separated)) Example: 1.
        type_ (ExportBatchesType | Unset): The batch type Example: icl.
        state (ExportBatchesState | Unset): The state of the batch Example: created.
        external_key (str | Unset): The external_key of the batch Example: ABC123456789.
        create_user_type (ExportBatchesCreateUserType | Unset): The user type Example: client.
        uploaded_filename (str | Unset): The uploaded_filename of the batch (contains, case
            insensitive, please combine with `create_date_from`) Example: merged_batch_id_123.ach.
        contains_virtual_transactions (bool | Unset): Signifies that virtual accounts are expected
            in all transactions
        contains_transactions_with_routing_number (str | Unset): Checks if the provided routing
            number is in the batch (can be multiple) Example: 123456789.
        doesnt_contain_transactions_with_routing_number (str | Unset): Checks if the provided
            routing number is not in the batch (can be multiple) Example: 123456789.
        create_date_from (datetime.date | Unset): The batch create date (>=) (Please use UTC)
            Example: 2024-02-04.
        create_date_to (datetime.date | Unset): The batch create date (<) (Please use UTC)
            Example: 2024-02-04.
        create_date_time_from (str | Unset): The batch create date time (>=) (Please use the zero
            UTC offset (Zulu) format) Example: 2024-02-04T00:00:00.000Z.
        create_date_time_to (str | Unset): The batch create date time (<) (Please use the zero UTC
            offset (Zulu) format) Example: 2024-02-04T23:59:59.000Z.
        test (bool | Unset): The batch test state Example: True.
        contains_return_transactions (bool | Unset): Filter batches that contain return
            transactions (transfer_type 'return' or 'iat_return') Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | ExportBatchesResponse
    """

    return sync_detailed(
        client=client,
        export_type=export_type,
        limit=limit,
        offset=offset,
        id=id,
        type_=type_,
        state=state,
        external_key=external_key,
        create_user_type=create_user_type,
        uploaded_filename=uploaded_filename,
        contains_virtual_transactions=contains_virtual_transactions,
        contains_transactions_with_routing_number=contains_transactions_with_routing_number,
        doesnt_contain_transactions_with_routing_number=doesnt_contain_transactions_with_routing_number,
        create_date_from=create_date_from,
        create_date_to=create_date_to,
        create_date_time_from=create_date_time_from,
        create_date_time_to=create_date_time_to,
        test=test,
        contains_return_transactions=contains_return_transactions,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    export_type: ExportBatchesExportType,
    limit: int | Unset = 1000,
    offset: int | Unset = 0,
    id: str | Unset = UNSET,
    type_: ExportBatchesType | Unset = UNSET,
    state: ExportBatchesState | Unset = UNSET,
    external_key: str | Unset = UNSET,
    create_user_type: ExportBatchesCreateUserType | Unset = UNSET,
    uploaded_filename: str | Unset = UNSET,
    contains_virtual_transactions: bool | Unset = UNSET,
    contains_transactions_with_routing_number: str | Unset = UNSET,
    doesnt_contain_transactions_with_routing_number: str | Unset = UNSET,
    create_date_from: datetime.date | Unset = UNSET,
    create_date_to: datetime.date | Unset = UNSET,
    create_date_time_from: str | Unset = UNSET,
    create_date_time_to: str | Unset = UNSET,
    test: bool | Unset = UNSET,
    contains_return_transactions: bool | Unset = UNSET,
) -> Response[ErrorBody | ExportBatchesResponse]:
    """Batches: Export

     Export batches in differnt formats based on their IDs. Useful for any kind of reporting.
    Might be a ZIP file if the export results in multiple files.

    For Fintech clients, access is restricted to batches where all transactions belong to their company.


    ***Dates and Date Times are in UTC!***


    ***Requires authorization.***

    Args:
        export_type (ExportBatchesExportType):  Example: csv.
        limit (int | Unset):  Default: 1000. Example: 1000.
        offset (int | Unset):  Default: 0.
        id (str | Unset): The batch ID (can be multiple (array or comma separated)) Example: 1.
        type_ (ExportBatchesType | Unset): The batch type Example: icl.
        state (ExportBatchesState | Unset): The state of the batch Example: created.
        external_key (str | Unset): The external_key of the batch Example: ABC123456789.
        create_user_type (ExportBatchesCreateUserType | Unset): The user type Example: client.
        uploaded_filename (str | Unset): The uploaded_filename of the batch (contains, case
            insensitive, please combine with `create_date_from`) Example: merged_batch_id_123.ach.
        contains_virtual_transactions (bool | Unset): Signifies that virtual accounts are expected
            in all transactions
        contains_transactions_with_routing_number (str | Unset): Checks if the provided routing
            number is in the batch (can be multiple) Example: 123456789.
        doesnt_contain_transactions_with_routing_number (str | Unset): Checks if the provided
            routing number is not in the batch (can be multiple) Example: 123456789.
        create_date_from (datetime.date | Unset): The batch create date (>=) (Please use UTC)
            Example: 2024-02-04.
        create_date_to (datetime.date | Unset): The batch create date (<) (Please use UTC)
            Example: 2024-02-04.
        create_date_time_from (str | Unset): The batch create date time (>=) (Please use the zero
            UTC offset (Zulu) format) Example: 2024-02-04T00:00:00.000Z.
        create_date_time_to (str | Unset): The batch create date time (<) (Please use the zero UTC
            offset (Zulu) format) Example: 2024-02-04T23:59:59.000Z.
        test (bool | Unset): The batch test state Example: True.
        contains_return_transactions (bool | Unset): Filter batches that contain return
            transactions (transfer_type 'return' or 'iat_return') Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | ExportBatchesResponse]
    """

    kwargs = _get_kwargs(
        export_type=export_type,
        limit=limit,
        offset=offset,
        id=id,
        type_=type_,
        state=state,
        external_key=external_key,
        create_user_type=create_user_type,
        uploaded_filename=uploaded_filename,
        contains_virtual_transactions=contains_virtual_transactions,
        contains_transactions_with_routing_number=contains_transactions_with_routing_number,
        doesnt_contain_transactions_with_routing_number=doesnt_contain_transactions_with_routing_number,
        create_date_from=create_date_from,
        create_date_to=create_date_to,
        create_date_time_from=create_date_time_from,
        create_date_time_to=create_date_time_to,
        test=test,
        contains_return_transactions=contains_return_transactions,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    export_type: ExportBatchesExportType,
    limit: int | Unset = 1000,
    offset: int | Unset = 0,
    id: str | Unset = UNSET,
    type_: ExportBatchesType | Unset = UNSET,
    state: ExportBatchesState | Unset = UNSET,
    external_key: str | Unset = UNSET,
    create_user_type: ExportBatchesCreateUserType | Unset = UNSET,
    uploaded_filename: str | Unset = UNSET,
    contains_virtual_transactions: bool | Unset = UNSET,
    contains_transactions_with_routing_number: str | Unset = UNSET,
    doesnt_contain_transactions_with_routing_number: str | Unset = UNSET,
    create_date_from: datetime.date | Unset = UNSET,
    create_date_to: datetime.date | Unset = UNSET,
    create_date_time_from: str | Unset = UNSET,
    create_date_time_to: str | Unset = UNSET,
    test: bool | Unset = UNSET,
    contains_return_transactions: bool | Unset = UNSET,
) -> ErrorBody | ExportBatchesResponse | None:
    """Batches: Export

     Export batches in differnt formats based on their IDs. Useful for any kind of reporting.
    Might be a ZIP file if the export results in multiple files.

    For Fintech clients, access is restricted to batches where all transactions belong to their company.


    ***Dates and Date Times are in UTC!***


    ***Requires authorization.***

    Args:
        export_type (ExportBatchesExportType):  Example: csv.
        limit (int | Unset):  Default: 1000. Example: 1000.
        offset (int | Unset):  Default: 0.
        id (str | Unset): The batch ID (can be multiple (array or comma separated)) Example: 1.
        type_ (ExportBatchesType | Unset): The batch type Example: icl.
        state (ExportBatchesState | Unset): The state of the batch Example: created.
        external_key (str | Unset): The external_key of the batch Example: ABC123456789.
        create_user_type (ExportBatchesCreateUserType | Unset): The user type Example: client.
        uploaded_filename (str | Unset): The uploaded_filename of the batch (contains, case
            insensitive, please combine with `create_date_from`) Example: merged_batch_id_123.ach.
        contains_virtual_transactions (bool | Unset): Signifies that virtual accounts are expected
            in all transactions
        contains_transactions_with_routing_number (str | Unset): Checks if the provided routing
            number is in the batch (can be multiple) Example: 123456789.
        doesnt_contain_transactions_with_routing_number (str | Unset): Checks if the provided
            routing number is not in the batch (can be multiple) Example: 123456789.
        create_date_from (datetime.date | Unset): The batch create date (>=) (Please use UTC)
            Example: 2024-02-04.
        create_date_to (datetime.date | Unset): The batch create date (<) (Please use UTC)
            Example: 2024-02-04.
        create_date_time_from (str | Unset): The batch create date time (>=) (Please use the zero
            UTC offset (Zulu) format) Example: 2024-02-04T00:00:00.000Z.
        create_date_time_to (str | Unset): The batch create date time (<) (Please use the zero UTC
            offset (Zulu) format) Example: 2024-02-04T23:59:59.000Z.
        test (bool | Unset): The batch test state Example: True.
        contains_return_transactions (bool | Unset): Filter batches that contain return
            transactions (transfer_type 'return' or 'iat_return') Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | ExportBatchesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            export_type=export_type,
            limit=limit,
            offset=offset,
            id=id,
            type_=type_,
            state=state,
            external_key=external_key,
            create_user_type=create_user_type,
            uploaded_filename=uploaded_filename,
            contains_virtual_transactions=contains_virtual_transactions,
            contains_transactions_with_routing_number=contains_transactions_with_routing_number,
            doesnt_contain_transactions_with_routing_number=doesnt_contain_transactions_with_routing_number,
            create_date_from=create_date_from,
            create_date_to=create_date_to,
            create_date_time_from=create_date_time_from,
            create_date_time_to=create_date_time_to,
            test=test,
            contains_return_transactions=contains_return_transactions,
        )
    ).parsed
