from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient
from ...client import Client
from ...models.error_body import ErrorBody
from ...models.get_balance_virtual_response_200 import GetBalanceVirtualResponse200
from ...types import UNSET
from ...types import Response
from ...types import Unset


def _get_kwargs(
    *,
    account_number: str | Unset = UNSET,
    account_id: float | Unset = UNSET,
    core_account_number: str | Unset = UNSET,
    core_account_id: float | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["account_number"] = account_number

    params["account_id"] = account_id

    params["core_account_number"] = core_account_number

    params["core_account_id"] = core_account_id

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/balance/virtual",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorBody | GetBalanceVirtualResponse200 | None:
    if response.status_code == 200:
        response_200 = GetBalanceVirtualResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorBody.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = ErrorBody.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorBody | GetBalanceVirtualResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    account_number: str | Unset = UNSET,
    account_id: float | Unset = UNSET,
    core_account_number: str | Unset = UNSET,
    core_account_id: float | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
) -> Response[ErrorBody | GetBalanceVirtualResponse200]:
    """Balance: Get Virtual

     Get [Pending](docs/concepts/balances.html#pending-balance) and
    [Available](docs/concepts/balances.html#available-balance) balances for virtual accounts

    ***Requires authorization.***

    Args:
        account_number (str | Unset):  Example: 12345.
        account_id (float | Unset):  Example: 12345.
        core_account_number (str | Unset):  Example: 12345.
        core_account_id (float | Unset):  Example: 12345.
        limit (int | Unset):  Default: 100. Example: 100.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | GetBalanceVirtualResponse200]
    """

    kwargs = _get_kwargs(
        account_number=account_number,
        account_id=account_id,
        core_account_number=core_account_number,
        core_account_id=core_account_id,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    account_number: str | Unset = UNSET,
    account_id: float | Unset = UNSET,
    core_account_number: str | Unset = UNSET,
    core_account_id: float | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
) -> ErrorBody | GetBalanceVirtualResponse200 | None:
    """Balance: Get Virtual

     Get [Pending](docs/concepts/balances.html#pending-balance) and
    [Available](docs/concepts/balances.html#available-balance) balances for virtual accounts

    ***Requires authorization.***

    Args:
        account_number (str | Unset):  Example: 12345.
        account_id (float | Unset):  Example: 12345.
        core_account_number (str | Unset):  Example: 12345.
        core_account_id (float | Unset):  Example: 12345.
        limit (int | Unset):  Default: 100. Example: 100.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | GetBalanceVirtualResponse200
    """

    return sync_detailed(
        client=client,
        account_number=account_number,
        account_id=account_id,
        core_account_number=core_account_number,
        core_account_id=core_account_id,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    account_number: str | Unset = UNSET,
    account_id: float | Unset = UNSET,
    core_account_number: str | Unset = UNSET,
    core_account_id: float | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
) -> Response[ErrorBody | GetBalanceVirtualResponse200]:
    """Balance: Get Virtual

     Get [Pending](docs/concepts/balances.html#pending-balance) and
    [Available](docs/concepts/balances.html#available-balance) balances for virtual accounts

    ***Requires authorization.***

    Args:
        account_number (str | Unset):  Example: 12345.
        account_id (float | Unset):  Example: 12345.
        core_account_number (str | Unset):  Example: 12345.
        core_account_id (float | Unset):  Example: 12345.
        limit (int | Unset):  Default: 100. Example: 100.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | GetBalanceVirtualResponse200]
    """

    kwargs = _get_kwargs(
        account_number=account_number,
        account_id=account_id,
        core_account_number=core_account_number,
        core_account_id=core_account_id,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    account_number: str | Unset = UNSET,
    account_id: float | Unset = UNSET,
    core_account_number: str | Unset = UNSET,
    core_account_id: float | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
) -> ErrorBody | GetBalanceVirtualResponse200 | None:
    """Balance: Get Virtual

     Get [Pending](docs/concepts/balances.html#pending-balance) and
    [Available](docs/concepts/balances.html#available-balance) balances for virtual accounts

    ***Requires authorization.***

    Args:
        account_number (str | Unset):  Example: 12345.
        account_id (float | Unset):  Example: 12345.
        core_account_number (str | Unset):  Example: 12345.
        core_account_id (float | Unset):  Example: 12345.
        limit (int | Unset):  Default: 100. Example: 100.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | GetBalanceVirtualResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            account_number=account_number,
            account_id=account_id,
            core_account_number=core_account_number,
            core_account_id=core_account_id,
            limit=limit,
            offset=offset,
        )
    ).parsed
