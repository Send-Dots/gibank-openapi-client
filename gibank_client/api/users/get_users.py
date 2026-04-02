from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient
from ...client import Client
from ...models.error_body import ErrorBody
from ...models.user_response_base import UserResponseBase
from ...types import UNSET
from ...types import Response
from ...types import Unset


def _get_kwargs(
    *,
    id: int | Unset = UNSET,
    company_id: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["id"] = id

    params["company_id"] = company_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/user",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorBody | list[UserResponseBase] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = UserResponseBase.from_dict(response_200_item_data)

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
) -> Response[ErrorBody | list[UserResponseBase]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    id: int | Unset = UNSET,
    company_id: int | Unset = UNSET,
) -> Response[ErrorBody | list[UserResponseBase]]:
    """Users: Get

     Get users

    ***Requires authorization.***

    Args:
        id (int | Unset):
        company_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | list[UserResponseBase]]
    """

    kwargs = _get_kwargs(
        id=id,
        company_id=company_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    id: int | Unset = UNSET,
    company_id: int | Unset = UNSET,
) -> ErrorBody | list[UserResponseBase] | None:
    """Users: Get

     Get users

    ***Requires authorization.***

    Args:
        id (int | Unset):
        company_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | list[UserResponseBase]
    """

    return sync_detailed(
        client=client,
        id=id,
        company_id=company_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: int | Unset = UNSET,
    company_id: int | Unset = UNSET,
) -> Response[ErrorBody | list[UserResponseBase]]:
    """Users: Get

     Get users

    ***Requires authorization.***

    Args:
        id (int | Unset):
        company_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | list[UserResponseBase]]
    """

    kwargs = _get_kwargs(
        id=id,
        company_id=company_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    id: int | Unset = UNSET,
    company_id: int | Unset = UNSET,
) -> ErrorBody | list[UserResponseBase] | None:
    """Users: Get

     Get users

    ***Requires authorization.***

    Args:
        id (int | Unset):
        company_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | list[UserResponseBase]
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            company_id=company_id,
        )
    ).parsed
