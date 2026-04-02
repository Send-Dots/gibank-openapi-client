import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient
from ...client import Client
from ...models.check_banking_day_response_200 import CheckBankingDayResponse200
from ...models.error_body import ErrorBody
from ...types import UNSET
from ...types import Response
from ...types import Unset


def _get_kwargs(
    *,
    date: datetime.date | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_date: str | Unset = UNSET
    if not isinstance(date, Unset):
        json_date = date.isoformat()
    params["date"] = json_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/tools/is_banking_day",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CheckBankingDayResponse200 | ErrorBody | None:
    if response.status_code == 200:
        response_200 = CheckBankingDayResponse200.from_dict(response.json())

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
) -> Response[CheckBankingDayResponse200 | ErrorBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    date: datetime.date | Unset = UNSET,
) -> Response[CheckBankingDayResponse200 | ErrorBody]:
    """Banking Day: Check

     Checks if the current or another day is a banking day

    ***Available by public without authorization.***

    Args:
        date (datetime.date | Unset): The date to check Example: 2024-02-04.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CheckBankingDayResponse200 | ErrorBody]
    """

    kwargs = _get_kwargs(
        date=date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    date: datetime.date | Unset = UNSET,
) -> CheckBankingDayResponse200 | ErrorBody | None:
    """Banking Day: Check

     Checks if the current or another day is a banking day

    ***Available by public without authorization.***

    Args:
        date (datetime.date | Unset): The date to check Example: 2024-02-04.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CheckBankingDayResponse200 | ErrorBody
    """

    return sync_detailed(
        client=client,
        date=date,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    date: datetime.date | Unset = UNSET,
) -> Response[CheckBankingDayResponse200 | ErrorBody]:
    """Banking Day: Check

     Checks if the current or another day is a banking day

    ***Available by public without authorization.***

    Args:
        date (datetime.date | Unset): The date to check Example: 2024-02-04.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CheckBankingDayResponse200 | ErrorBody]
    """

    kwargs = _get_kwargs(
        date=date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    date: datetime.date | Unset = UNSET,
) -> CheckBankingDayResponse200 | ErrorBody | None:
    """Banking Day: Check

     Checks if the current or another day is a banking day

    ***Available by public without authorization.***

    Args:
        date (datetime.date | Unset): The date to check Example: 2024-02-04.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CheckBankingDayResponse200 | ErrorBody
    """

    return (
        await asyncio_detailed(
            client=client,
            date=date,
        )
    ).parsed
