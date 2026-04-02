from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient
from ...client import Client
from ...models.error_body import ErrorBody
from ...models.transaction_files_response import TransactionFilesResponse
from ...types import Response


def _get_kwargs(
    transaction_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/transaction/{transaction_id}/files".format(
            transaction_id=quote(str(transaction_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorBody | TransactionFilesResponse | None:
    if response.status_code == 200:
        response_200 = TransactionFilesResponse.from_dict(response.json())

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
) -> Response[ErrorBody | TransactionFilesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    transaction_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorBody | TransactionFilesResponse]:
    """Transaction: Get Files

     Get the raw file or the parsed data that were used to create a transaction. Useful to get the raw
    file or the parsed data you used when the transaction has been submitted.

    ***Requires authorization.***

    Args:
        transaction_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | TransactionFilesResponse]
    """

    kwargs = _get_kwargs(
        transaction_id=transaction_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    transaction_id: int,
    *,
    client: AuthenticatedClient,
) -> ErrorBody | TransactionFilesResponse | None:
    """Transaction: Get Files

     Get the raw file or the parsed data that were used to create a transaction. Useful to get the raw
    file or the parsed data you used when the transaction has been submitted.

    ***Requires authorization.***

    Args:
        transaction_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | TransactionFilesResponse
    """

    return sync_detailed(
        transaction_id=transaction_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    transaction_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorBody | TransactionFilesResponse]:
    """Transaction: Get Files

     Get the raw file or the parsed data that were used to create a transaction. Useful to get the raw
    file or the parsed data you used when the transaction has been submitted.

    ***Requires authorization.***

    Args:
        transaction_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | TransactionFilesResponse]
    """

    kwargs = _get_kwargs(
        transaction_id=transaction_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    transaction_id: int,
    *,
    client: AuthenticatedClient,
) -> ErrorBody | TransactionFilesResponse | None:
    """Transaction: Get Files

     Get the raw file or the parsed data that were used to create a transaction. Useful to get the raw
    file or the parsed data you used when the transaction has been submitted.

    ***Requires authorization.***

    Args:
        transaction_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | TransactionFilesResponse
    """

    return (
        await asyncio_detailed(
            transaction_id=transaction_id,
            client=client,
        )
    ).parsed
