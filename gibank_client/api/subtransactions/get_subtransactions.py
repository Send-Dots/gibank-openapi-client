import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient
from ...client import Client
from ...models.error_body import ErrorBody
from ...models.get_subtransactions_response_200 import GetSubtransactionsResponse200
from ...models.get_subtransactions_transfer_direction import (
    GetSubtransactionsTransferDirection,
)
from ...types import UNSET
from ...types import Response
from ...types import Unset


def _get_kwargs(
    *,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    id: str | Unset = UNSET,
    transaction_id: float | Unset = UNSET,
    create_date_from: datetime.date | Unset = UNSET,
    create_date_to: datetime.date | Unset = UNSET,
    create_date_time_from: str | Unset = UNSET,
    create_date_time_to: str | Unset = UNSET,
    amount_from: float | Unset = UNSET,
    amount_to: float | Unset = UNSET,
    deleted: bool | Unset = UNSET,
    company_name: str | Unset = UNSET,
    external_key: str | Unset = UNSET,
    purpose: str | Unset = UNSET,
    origin_subclient_name: str | Unset = UNSET,
    destination_subclient_name: str | Unset = UNSET,
    transfer_direction: GetSubtransactionsTransferDirection | Unset = UNSET,
    reference: str | Unset = UNSET,
    date_from: datetime.date | Unset = UNSET,
    date_to: datetime.date | Unset = UNSET,
    date_time_from: str | Unset = UNSET,
    date_time_to: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params["id"] = id

    params["transaction_id"] = transaction_id

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

    params["amount_from"] = amount_from

    params["amount_to"] = amount_to

    params["deleted"] = deleted

    params["company_name"] = company_name

    params["external_key"] = external_key

    params["purpose"] = purpose

    params["origin_subclient_name"] = origin_subclient_name

    params["destination_subclient_name"] = destination_subclient_name

    json_transfer_direction: str | Unset = UNSET
    if not isinstance(transfer_direction, Unset):
        json_transfer_direction = transfer_direction.value

    params["transfer_direction"] = json_transfer_direction

    params["reference"] = reference

    json_date_from: str | Unset = UNSET
    if not isinstance(date_from, Unset):
        json_date_from = date_from.isoformat()
    params["date_from"] = json_date_from

    json_date_to: str | Unset = UNSET
    if not isinstance(date_to, Unset):
        json_date_to = date_to.isoformat()
    params["date_to"] = json_date_to

    params["date_time_from"] = date_time_from

    params["date_time_to"] = date_time_to

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/subtransaction",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorBody | GetSubtransactionsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetSubtransactionsResponse200.from_dict(response.json())

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
) -> Response[ErrorBody | GetSubtransactionsResponse200]:
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
    transaction_id: float | Unset = UNSET,
    create_date_from: datetime.date | Unset = UNSET,
    create_date_to: datetime.date | Unset = UNSET,
    create_date_time_from: str | Unset = UNSET,
    create_date_time_to: str | Unset = UNSET,
    amount_from: float | Unset = UNSET,
    amount_to: float | Unset = UNSET,
    deleted: bool | Unset = UNSET,
    company_name: str | Unset = UNSET,
    external_key: str | Unset = UNSET,
    purpose: str | Unset = UNSET,
    origin_subclient_name: str | Unset = UNSET,
    destination_subclient_name: str | Unset = UNSET,
    transfer_direction: GetSubtransactionsTransferDirection | Unset = UNSET,
    reference: str | Unset = UNSET,
    date_from: datetime.date | Unset = UNSET,
    date_to: datetime.date | Unset = UNSET,
    date_time_from: str | Unset = UNSET,
    date_time_to: str | Unset = UNSET,
) -> Response[ErrorBody | GetSubtransactionsResponse200]:
    """Subtransactions: Get

     Get subtransactions. Useful to find subtransactions of the past time period.

    ***Requires authorization.***

    Args:
        limit (int | Unset):  Default: 100. Example: 100.
        offset (int | Unset):  Default: 0.
        id (str | Unset): The subtransaction ID (can be multiple (array or comma separated))
            Example: 1.
        transaction_id (float | Unset): The transaction ID. Deleted links are excluded. Example:
            1.
        create_date_from (datetime.date | Unset): The subtransaction create date (>=) (Please use
            UTC) Example: 2024-02-04.
        create_date_to (datetime.date | Unset): The subtransaction create date (<) (Please use
            UTC) Example: 2024-02-04.
        create_date_time_from (str | Unset): The subtransaction create date time (>=) (Please use
            the zero UTC offset (Zulu) format) Example: 2024-02-04T00:00:00.000Z.
        create_date_time_to (str | Unset): The subtransaction create date time (<) (Please use the
            zero UTC offset (Zulu) format) Example: 2024-02-04T23:59:59.000Z.
        amount_from (float | Unset): The subtransaction amount (>=) Example: 500.
        amount_to (float | Unset): The subtransaction amount (<) Example: 2000.
        deleted (bool | Unset): The subtransaction deleted flag
        company_name (str | Unset): The company name (contains, case insensitive) Example: ABC
            Bank.
        external_key (str | Unset): The internal key used by bank customer (can be multiple)
            Example: EXT12345.
        purpose (str | Unset): The subtransaction purpose (contains, please combine with
            `date_from`, case insensitive) Example: Test 01.
        origin_subclient_name (str | Unset): The origin subclient name (contains, case
            insensitive) Example: Max Mustermann.
        destination_subclient_name (str | Unset): The destination subclient name (contains, case
            insensitive) Example: Max Mustermann.
        transfer_direction (GetSubtransactionsTransferDirection | Unset): The direction of the
            transfer. `outbound` means money left your account, `inbound` means money was added to
            your account Example: outbound.
        reference (str | Unset): The subtransaction reference (contains, case insensitive, please
            combine with `date_from`) (can be multiple) Example: Test 01.
        date_from (datetime.date | Unset): The subtransaction date (>=) (Please use UTC) Example:
            2024-02-04.
        date_to (datetime.date | Unset): The subtransaction date (<) (Please use UTC) Example:
            2024-02-04.
        date_time_from (str | Unset): The subtransaction date time(>=) (Please use the zero UTC
            offset (Zulu) format) Example: 2024-02-04T23:59:59.000Z.
        date_time_to (str | Unset): The subtransaction date time (<) (Please use the zero UTC
            offset (Zulu) format) Example: 2024-02-04T23:59:59.000Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | GetSubtransactionsResponse200]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        id=id,
        transaction_id=transaction_id,
        create_date_from=create_date_from,
        create_date_to=create_date_to,
        create_date_time_from=create_date_time_from,
        create_date_time_to=create_date_time_to,
        amount_from=amount_from,
        amount_to=amount_to,
        deleted=deleted,
        company_name=company_name,
        external_key=external_key,
        purpose=purpose,
        origin_subclient_name=origin_subclient_name,
        destination_subclient_name=destination_subclient_name,
        transfer_direction=transfer_direction,
        reference=reference,
        date_from=date_from,
        date_to=date_to,
        date_time_from=date_time_from,
        date_time_to=date_time_to,
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
    transaction_id: float | Unset = UNSET,
    create_date_from: datetime.date | Unset = UNSET,
    create_date_to: datetime.date | Unset = UNSET,
    create_date_time_from: str | Unset = UNSET,
    create_date_time_to: str | Unset = UNSET,
    amount_from: float | Unset = UNSET,
    amount_to: float | Unset = UNSET,
    deleted: bool | Unset = UNSET,
    company_name: str | Unset = UNSET,
    external_key: str | Unset = UNSET,
    purpose: str | Unset = UNSET,
    origin_subclient_name: str | Unset = UNSET,
    destination_subclient_name: str | Unset = UNSET,
    transfer_direction: GetSubtransactionsTransferDirection | Unset = UNSET,
    reference: str | Unset = UNSET,
    date_from: datetime.date | Unset = UNSET,
    date_to: datetime.date | Unset = UNSET,
    date_time_from: str | Unset = UNSET,
    date_time_to: str | Unset = UNSET,
) -> ErrorBody | GetSubtransactionsResponse200 | None:
    """Subtransactions: Get

     Get subtransactions. Useful to find subtransactions of the past time period.

    ***Requires authorization.***

    Args:
        limit (int | Unset):  Default: 100. Example: 100.
        offset (int | Unset):  Default: 0.
        id (str | Unset): The subtransaction ID (can be multiple (array or comma separated))
            Example: 1.
        transaction_id (float | Unset): The transaction ID. Deleted links are excluded. Example:
            1.
        create_date_from (datetime.date | Unset): The subtransaction create date (>=) (Please use
            UTC) Example: 2024-02-04.
        create_date_to (datetime.date | Unset): The subtransaction create date (<) (Please use
            UTC) Example: 2024-02-04.
        create_date_time_from (str | Unset): The subtransaction create date time (>=) (Please use
            the zero UTC offset (Zulu) format) Example: 2024-02-04T00:00:00.000Z.
        create_date_time_to (str | Unset): The subtransaction create date time (<) (Please use the
            zero UTC offset (Zulu) format) Example: 2024-02-04T23:59:59.000Z.
        amount_from (float | Unset): The subtransaction amount (>=) Example: 500.
        amount_to (float | Unset): The subtransaction amount (<) Example: 2000.
        deleted (bool | Unset): The subtransaction deleted flag
        company_name (str | Unset): The company name (contains, case insensitive) Example: ABC
            Bank.
        external_key (str | Unset): The internal key used by bank customer (can be multiple)
            Example: EXT12345.
        purpose (str | Unset): The subtransaction purpose (contains, please combine with
            `date_from`, case insensitive) Example: Test 01.
        origin_subclient_name (str | Unset): The origin subclient name (contains, case
            insensitive) Example: Max Mustermann.
        destination_subclient_name (str | Unset): The destination subclient name (contains, case
            insensitive) Example: Max Mustermann.
        transfer_direction (GetSubtransactionsTransferDirection | Unset): The direction of the
            transfer. `outbound` means money left your account, `inbound` means money was added to
            your account Example: outbound.
        reference (str | Unset): The subtransaction reference (contains, case insensitive, please
            combine with `date_from`) (can be multiple) Example: Test 01.
        date_from (datetime.date | Unset): The subtransaction date (>=) (Please use UTC) Example:
            2024-02-04.
        date_to (datetime.date | Unset): The subtransaction date (<) (Please use UTC) Example:
            2024-02-04.
        date_time_from (str | Unset): The subtransaction date time(>=) (Please use the zero UTC
            offset (Zulu) format) Example: 2024-02-04T23:59:59.000Z.
        date_time_to (str | Unset): The subtransaction date time (<) (Please use the zero UTC
            offset (Zulu) format) Example: 2024-02-04T23:59:59.000Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | GetSubtransactionsResponse200
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        id=id,
        transaction_id=transaction_id,
        create_date_from=create_date_from,
        create_date_to=create_date_to,
        create_date_time_from=create_date_time_from,
        create_date_time_to=create_date_time_to,
        amount_from=amount_from,
        amount_to=amount_to,
        deleted=deleted,
        company_name=company_name,
        external_key=external_key,
        purpose=purpose,
        origin_subclient_name=origin_subclient_name,
        destination_subclient_name=destination_subclient_name,
        transfer_direction=transfer_direction,
        reference=reference,
        date_from=date_from,
        date_to=date_to,
        date_time_from=date_time_from,
        date_time_to=date_time_to,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    id: str | Unset = UNSET,
    transaction_id: float | Unset = UNSET,
    create_date_from: datetime.date | Unset = UNSET,
    create_date_to: datetime.date | Unset = UNSET,
    create_date_time_from: str | Unset = UNSET,
    create_date_time_to: str | Unset = UNSET,
    amount_from: float | Unset = UNSET,
    amount_to: float | Unset = UNSET,
    deleted: bool | Unset = UNSET,
    company_name: str | Unset = UNSET,
    external_key: str | Unset = UNSET,
    purpose: str | Unset = UNSET,
    origin_subclient_name: str | Unset = UNSET,
    destination_subclient_name: str | Unset = UNSET,
    transfer_direction: GetSubtransactionsTransferDirection | Unset = UNSET,
    reference: str | Unset = UNSET,
    date_from: datetime.date | Unset = UNSET,
    date_to: datetime.date | Unset = UNSET,
    date_time_from: str | Unset = UNSET,
    date_time_to: str | Unset = UNSET,
) -> Response[ErrorBody | GetSubtransactionsResponse200]:
    """Subtransactions: Get

     Get subtransactions. Useful to find subtransactions of the past time period.

    ***Requires authorization.***

    Args:
        limit (int | Unset):  Default: 100. Example: 100.
        offset (int | Unset):  Default: 0.
        id (str | Unset): The subtransaction ID (can be multiple (array or comma separated))
            Example: 1.
        transaction_id (float | Unset): The transaction ID. Deleted links are excluded. Example:
            1.
        create_date_from (datetime.date | Unset): The subtransaction create date (>=) (Please use
            UTC) Example: 2024-02-04.
        create_date_to (datetime.date | Unset): The subtransaction create date (<) (Please use
            UTC) Example: 2024-02-04.
        create_date_time_from (str | Unset): The subtransaction create date time (>=) (Please use
            the zero UTC offset (Zulu) format) Example: 2024-02-04T00:00:00.000Z.
        create_date_time_to (str | Unset): The subtransaction create date time (<) (Please use the
            zero UTC offset (Zulu) format) Example: 2024-02-04T23:59:59.000Z.
        amount_from (float | Unset): The subtransaction amount (>=) Example: 500.
        amount_to (float | Unset): The subtransaction amount (<) Example: 2000.
        deleted (bool | Unset): The subtransaction deleted flag
        company_name (str | Unset): The company name (contains, case insensitive) Example: ABC
            Bank.
        external_key (str | Unset): The internal key used by bank customer (can be multiple)
            Example: EXT12345.
        purpose (str | Unset): The subtransaction purpose (contains, please combine with
            `date_from`, case insensitive) Example: Test 01.
        origin_subclient_name (str | Unset): The origin subclient name (contains, case
            insensitive) Example: Max Mustermann.
        destination_subclient_name (str | Unset): The destination subclient name (contains, case
            insensitive) Example: Max Mustermann.
        transfer_direction (GetSubtransactionsTransferDirection | Unset): The direction of the
            transfer. `outbound` means money left your account, `inbound` means money was added to
            your account Example: outbound.
        reference (str | Unset): The subtransaction reference (contains, case insensitive, please
            combine with `date_from`) (can be multiple) Example: Test 01.
        date_from (datetime.date | Unset): The subtransaction date (>=) (Please use UTC) Example:
            2024-02-04.
        date_to (datetime.date | Unset): The subtransaction date (<) (Please use UTC) Example:
            2024-02-04.
        date_time_from (str | Unset): The subtransaction date time(>=) (Please use the zero UTC
            offset (Zulu) format) Example: 2024-02-04T23:59:59.000Z.
        date_time_to (str | Unset): The subtransaction date time (<) (Please use the zero UTC
            offset (Zulu) format) Example: 2024-02-04T23:59:59.000Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | GetSubtransactionsResponse200]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        id=id,
        transaction_id=transaction_id,
        create_date_from=create_date_from,
        create_date_to=create_date_to,
        create_date_time_from=create_date_time_from,
        create_date_time_to=create_date_time_to,
        amount_from=amount_from,
        amount_to=amount_to,
        deleted=deleted,
        company_name=company_name,
        external_key=external_key,
        purpose=purpose,
        origin_subclient_name=origin_subclient_name,
        destination_subclient_name=destination_subclient_name,
        transfer_direction=transfer_direction,
        reference=reference,
        date_from=date_from,
        date_to=date_to,
        date_time_from=date_time_from,
        date_time_to=date_time_to,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    id: str | Unset = UNSET,
    transaction_id: float | Unset = UNSET,
    create_date_from: datetime.date | Unset = UNSET,
    create_date_to: datetime.date | Unset = UNSET,
    create_date_time_from: str | Unset = UNSET,
    create_date_time_to: str | Unset = UNSET,
    amount_from: float | Unset = UNSET,
    amount_to: float | Unset = UNSET,
    deleted: bool | Unset = UNSET,
    company_name: str | Unset = UNSET,
    external_key: str | Unset = UNSET,
    purpose: str | Unset = UNSET,
    origin_subclient_name: str | Unset = UNSET,
    destination_subclient_name: str | Unset = UNSET,
    transfer_direction: GetSubtransactionsTransferDirection | Unset = UNSET,
    reference: str | Unset = UNSET,
    date_from: datetime.date | Unset = UNSET,
    date_to: datetime.date | Unset = UNSET,
    date_time_from: str | Unset = UNSET,
    date_time_to: str | Unset = UNSET,
) -> ErrorBody | GetSubtransactionsResponse200 | None:
    """Subtransactions: Get

     Get subtransactions. Useful to find subtransactions of the past time period.

    ***Requires authorization.***

    Args:
        limit (int | Unset):  Default: 100. Example: 100.
        offset (int | Unset):  Default: 0.
        id (str | Unset): The subtransaction ID (can be multiple (array or comma separated))
            Example: 1.
        transaction_id (float | Unset): The transaction ID. Deleted links are excluded. Example:
            1.
        create_date_from (datetime.date | Unset): The subtransaction create date (>=) (Please use
            UTC) Example: 2024-02-04.
        create_date_to (datetime.date | Unset): The subtransaction create date (<) (Please use
            UTC) Example: 2024-02-04.
        create_date_time_from (str | Unset): The subtransaction create date time (>=) (Please use
            the zero UTC offset (Zulu) format) Example: 2024-02-04T00:00:00.000Z.
        create_date_time_to (str | Unset): The subtransaction create date time (<) (Please use the
            zero UTC offset (Zulu) format) Example: 2024-02-04T23:59:59.000Z.
        amount_from (float | Unset): The subtransaction amount (>=) Example: 500.
        amount_to (float | Unset): The subtransaction amount (<) Example: 2000.
        deleted (bool | Unset): The subtransaction deleted flag
        company_name (str | Unset): The company name (contains, case insensitive) Example: ABC
            Bank.
        external_key (str | Unset): The internal key used by bank customer (can be multiple)
            Example: EXT12345.
        purpose (str | Unset): The subtransaction purpose (contains, please combine with
            `date_from`, case insensitive) Example: Test 01.
        origin_subclient_name (str | Unset): The origin subclient name (contains, case
            insensitive) Example: Max Mustermann.
        destination_subclient_name (str | Unset): The destination subclient name (contains, case
            insensitive) Example: Max Mustermann.
        transfer_direction (GetSubtransactionsTransferDirection | Unset): The direction of the
            transfer. `outbound` means money left your account, `inbound` means money was added to
            your account Example: outbound.
        reference (str | Unset): The subtransaction reference (contains, case insensitive, please
            combine with `date_from`) (can be multiple) Example: Test 01.
        date_from (datetime.date | Unset): The subtransaction date (>=) (Please use UTC) Example:
            2024-02-04.
        date_to (datetime.date | Unset): The subtransaction date (<) (Please use UTC) Example:
            2024-02-04.
        date_time_from (str | Unset): The subtransaction date time(>=) (Please use the zero UTC
            offset (Zulu) format) Example: 2024-02-04T23:59:59.000Z.
        date_time_to (str | Unset): The subtransaction date time (<) (Please use the zero UTC
            offset (Zulu) format) Example: 2024-02-04T23:59:59.000Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | GetSubtransactionsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            id=id,
            transaction_id=transaction_id,
            create_date_from=create_date_from,
            create_date_to=create_date_to,
            create_date_time_from=create_date_time_from,
            create_date_time_to=create_date_time_to,
            amount_from=amount_from,
            amount_to=amount_to,
            deleted=deleted,
            company_name=company_name,
            external_key=external_key,
            purpose=purpose,
            origin_subclient_name=origin_subclient_name,
            destination_subclient_name=destination_subclient_name,
            transfer_direction=transfer_direction,
            reference=reference,
            date_from=date_from,
            date_to=date_to,
            date_time_from=date_time_from,
            date_time_to=date_time_to,
        )
    ).parsed
