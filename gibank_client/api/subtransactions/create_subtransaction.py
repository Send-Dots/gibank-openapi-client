from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient
from ...client import Client
from ...models.error_body import ErrorBody
from ...models.subtransaction_create import SubtransactionCreate
from ...models.subtransaction_fields import SubtransactionFields
from ...types import Response


def _get_kwargs(
    *,
    body: SubtransactionCreate,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/subtransaction",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorBody | SubtransactionFields | None:
    if response.status_code == 200:
        response_200 = SubtransactionFields.from_dict(response.json())

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

    if response.status_code == 404:
        response_404 = ErrorBody.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = ErrorBody.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorBody | SubtransactionFields]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: SubtransactionCreate,
) -> Response[ErrorBody | SubtransactionFields]:
    """Subtransaction: Create

     Create Subtransaction

    ***Duplicate (Conflict) Check:*** By External Key

    ***Requires authorization.***

    Args:
        body (SubtransactionCreate):  Example: {'transaction_id': 101, 'external_key': 'MY-
            TX-007', 'subclient_origin_id': 1, 'subclient_destination_id': 2, 'amount': 25075,
            'currency': 'USD', 'fees': 250, 'purpose': 'Consulting services Q1', 'transfer_direction':
            'outbound', 'reference': 'INV-2025-Q1-003', 'date_time': '2025-02-10T10:30:00.000Z'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | SubtransactionFields]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: SubtransactionCreate,
) -> ErrorBody | SubtransactionFields | None:
    """Subtransaction: Create

     Create Subtransaction

    ***Duplicate (Conflict) Check:*** By External Key

    ***Requires authorization.***

    Args:
        body (SubtransactionCreate):  Example: {'transaction_id': 101, 'external_key': 'MY-
            TX-007', 'subclient_origin_id': 1, 'subclient_destination_id': 2, 'amount': 25075,
            'currency': 'USD', 'fees': 250, 'purpose': 'Consulting services Q1', 'transfer_direction':
            'outbound', 'reference': 'INV-2025-Q1-003', 'date_time': '2025-02-10T10:30:00.000Z'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | SubtransactionFields
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: SubtransactionCreate,
) -> Response[ErrorBody | SubtransactionFields]:
    """Subtransaction: Create

     Create Subtransaction

    ***Duplicate (Conflict) Check:*** By External Key

    ***Requires authorization.***

    Args:
        body (SubtransactionCreate):  Example: {'transaction_id': 101, 'external_key': 'MY-
            TX-007', 'subclient_origin_id': 1, 'subclient_destination_id': 2, 'amount': 25075,
            'currency': 'USD', 'fees': 250, 'purpose': 'Consulting services Q1', 'transfer_direction':
            'outbound', 'reference': 'INV-2025-Q1-003', 'date_time': '2025-02-10T10:30:00.000Z'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | SubtransactionFields]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: SubtransactionCreate,
) -> ErrorBody | SubtransactionFields | None:
    """Subtransaction: Create

     Create Subtransaction

    ***Duplicate (Conflict) Check:*** By External Key

    ***Requires authorization.***

    Args:
        body (SubtransactionCreate):  Example: {'transaction_id': 101, 'external_key': 'MY-
            TX-007', 'subclient_origin_id': 1, 'subclient_destination_id': 2, 'amount': 25075,
            'currency': 'USD', 'fees': 250, 'purpose': 'Consulting services Q1', 'transfer_direction':
            'outbound', 'reference': 'INV-2025-Q1-003', 'date_time': '2025-02-10T10:30:00.000Z'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | SubtransactionFields
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
