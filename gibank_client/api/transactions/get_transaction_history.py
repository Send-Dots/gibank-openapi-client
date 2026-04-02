from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient
from ...client import Client
from ...models.error_body import ErrorBody
from ...models.paginated_production_history import PaginatedProductionHistory
from ...types import UNSET
from ...types import Response
from ...types import Unset


def _get_kwargs(
    transaction_id: int,
    *,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/transaction/{transaction_id}/history".format(
            transaction_id=quote(str(transaction_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorBody | PaginatedProductionHistory | None:
    if response.status_code == 200:
        response_200 = PaginatedProductionHistory.from_dict(response.json())

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
) -> Response[ErrorBody | PaginatedProductionHistory]:
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
    limit: int | Unset = 100,
    offset: int | Unset = 0,
) -> Response[ErrorBody | PaginatedProductionHistory]:
    """Transaction: Get History

     Get transaction history, so actions that were logged regarding a certain transaction. Useful to
    understand what happened when with your transaction.

    ***Requires authorization.***

    Args:
        transaction_id (int):  Example: 1.
        limit (int | Unset):  Default: 100. Example: 100.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | PaginatedProductionHistory]
    """

    kwargs = _get_kwargs(
        transaction_id=transaction_id,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    transaction_id: int,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
) -> ErrorBody | PaginatedProductionHistory | None:
    """Transaction: Get History

     Get transaction history, so actions that were logged regarding a certain transaction. Useful to
    understand what happened when with your transaction.

    ***Requires authorization.***

    Args:
        transaction_id (int):  Example: 1.
        limit (int | Unset):  Default: 100. Example: 100.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | PaginatedProductionHistory
    """

    return sync_detailed(
        transaction_id=transaction_id,
        client=client,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    transaction_id: int,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
) -> Response[ErrorBody | PaginatedProductionHistory]:
    """Transaction: Get History

     Get transaction history, so actions that were logged regarding a certain transaction. Useful to
    understand what happened when with your transaction.

    ***Requires authorization.***

    Args:
        transaction_id (int):  Example: 1.
        limit (int | Unset):  Default: 100. Example: 100.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | PaginatedProductionHistory]
    """

    kwargs = _get_kwargs(
        transaction_id=transaction_id,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    transaction_id: int,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
) -> ErrorBody | PaginatedProductionHistory | None:
    """Transaction: Get History

     Get transaction history, so actions that were logged regarding a certain transaction. Useful to
    understand what happened when with your transaction.

    ***Requires authorization.***

    Args:
        transaction_id (int):  Example: 1.
        limit (int | Unset):  Default: 100. Example: 100.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | PaginatedProductionHistory
    """

    return (
        await asyncio_detailed(
            transaction_id=transaction_id,
            client=client,
            limit=limit,
            offset=offset,
        )
    ).parsed
