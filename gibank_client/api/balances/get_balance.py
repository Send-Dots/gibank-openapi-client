import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient
from ...client import Client
from ...models.account_balance_fields import AccountBalanceFields
from ...models.error_body import ErrorBody
from ...types import UNSET
from ...types import Response
from ...types import Unset


def _get_kwargs(
    *,
    date: datetime.date | Unset = UNSET,
    account_id: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_date: str | Unset = UNSET
    if not isinstance(date, Unset):
        json_date = date.isoformat()
    params["date"] = json_date

    params["account_id"] = account_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/balance",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorBody | list[AccountBalanceFields] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AccountBalanceFields.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[ErrorBody | list[AccountBalanceFields]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    date: datetime.date | Unset = UNSET,
    account_id: int | Unset = UNSET,
) -> Response[ErrorBody | list[AccountBalanceFields]]:
    """Balance: Get

     Get the [Available Balance](docs/concepts/balances.html#available-balance) for all user accounts
    associated with users from your company.

    If a date is specified, the balance returned for each account will be the closing balance at the end
    of that day.

    ***Requires authorization.***

    Args:
        date (datetime.date | Unset):  Example: 2024-02-04.
        account_id (int | Unset):  Example: 123.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | list[AccountBalanceFields]]
    """

    kwargs = _get_kwargs(
        date=date,
        account_id=account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    date: datetime.date | Unset = UNSET,
    account_id: int | Unset = UNSET,
) -> ErrorBody | list[AccountBalanceFields] | None:
    """Balance: Get

     Get the [Available Balance](docs/concepts/balances.html#available-balance) for all user accounts
    associated with users from your company.

    If a date is specified, the balance returned for each account will be the closing balance at the end
    of that day.

    ***Requires authorization.***

    Args:
        date (datetime.date | Unset):  Example: 2024-02-04.
        account_id (int | Unset):  Example: 123.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | list[AccountBalanceFields]
    """

    return sync_detailed(
        client=client,
        date=date,
        account_id=account_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    date: datetime.date | Unset = UNSET,
    account_id: int | Unset = UNSET,
) -> Response[ErrorBody | list[AccountBalanceFields]]:
    """Balance: Get

     Get the [Available Balance](docs/concepts/balances.html#available-balance) for all user accounts
    associated with users from your company.

    If a date is specified, the balance returned for each account will be the closing balance at the end
    of that day.

    ***Requires authorization.***

    Args:
        date (datetime.date | Unset):  Example: 2024-02-04.
        account_id (int | Unset):  Example: 123.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | list[AccountBalanceFields]]
    """

    kwargs = _get_kwargs(
        date=date,
        account_id=account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    date: datetime.date | Unset = UNSET,
    account_id: int | Unset = UNSET,
) -> ErrorBody | list[AccountBalanceFields] | None:
    """Balance: Get

     Get the [Available Balance](docs/concepts/balances.html#available-balance) for all user accounts
    associated with users from your company.

    If a date is specified, the balance returned for each account will be the closing balance at the end
    of that day.

    ***Requires authorization.***

    Args:
        date (datetime.date | Unset):  Example: 2024-02-04.
        account_id (int | Unset):  Example: 123.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | list[AccountBalanceFields]
    """

    return (
        await asyncio_detailed(
            client=client,
            date=date,
            account_id=account_id,
        )
    ).parsed
