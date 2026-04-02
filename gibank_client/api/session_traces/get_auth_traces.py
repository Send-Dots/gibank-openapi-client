from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient
from ...client import Client
from ...models.error_body import ErrorBody
from ...models.get_auth_traces_response_200 import GetAuthTracesResponse200
from ...types import UNSET
from ...types import Response
from ...types import Unset


def _get_kwargs(
    *,
    user_id: int | Unset = UNSET,
    user_apikey_id: int | Unset = UNSET,
    company_id: int | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["user_id"] = user_id

    params["user_apikey_id"] = user_apikey_id

    params["company_id"] = company_id

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/auth-traces",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorBody | GetAuthTracesResponse200 | None:
    if response.status_code == 200:
        response_200 = GetAuthTracesResponse200.from_dict(response.json())

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
) -> Response[ErrorBody | GetAuthTracesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    user_id: int | Unset = UNSET,
    user_apikey_id: int | Unset = UNSET,
    company_id: int | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
) -> Response[ErrorBody | GetAuthTracesResponse200]:
    """Auth Traces: Get

     Get authentication trace history for the current user.
    You may pass an optional `user_id` query parameter to view traces for any user (of your company).
    Optionally filter by `company_id` to see all traces for users of a specific company.
    Optionally filter by `user_apikey_id` to see usage history for a specific API key.
    Defaults to your user.
    Going back maximum 365 days.

    ***Requires authorization.***

    Args:
        user_id (int | Unset):
        user_apikey_id (int | Unset):
        company_id (int | Unset):
        limit (int | Unset):  Default: 100. Example: 100.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | GetAuthTracesResponse200]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        user_apikey_id=user_apikey_id,
        company_id=company_id,
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
    user_id: int | Unset = UNSET,
    user_apikey_id: int | Unset = UNSET,
    company_id: int | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
) -> ErrorBody | GetAuthTracesResponse200 | None:
    """Auth Traces: Get

     Get authentication trace history for the current user.
    You may pass an optional `user_id` query parameter to view traces for any user (of your company).
    Optionally filter by `company_id` to see all traces for users of a specific company.
    Optionally filter by `user_apikey_id` to see usage history for a specific API key.
    Defaults to your user.
    Going back maximum 365 days.

    ***Requires authorization.***

    Args:
        user_id (int | Unset):
        user_apikey_id (int | Unset):
        company_id (int | Unset):
        limit (int | Unset):  Default: 100. Example: 100.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | GetAuthTracesResponse200
    """

    return sync_detailed(
        client=client,
        user_id=user_id,
        user_apikey_id=user_apikey_id,
        company_id=company_id,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    user_id: int | Unset = UNSET,
    user_apikey_id: int | Unset = UNSET,
    company_id: int | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
) -> Response[ErrorBody | GetAuthTracesResponse200]:
    """Auth Traces: Get

     Get authentication trace history for the current user.
    You may pass an optional `user_id` query parameter to view traces for any user (of your company).
    Optionally filter by `company_id` to see all traces for users of a specific company.
    Optionally filter by `user_apikey_id` to see usage history for a specific API key.
    Defaults to your user.
    Going back maximum 365 days.

    ***Requires authorization.***

    Args:
        user_id (int | Unset):
        user_apikey_id (int | Unset):
        company_id (int | Unset):
        limit (int | Unset):  Default: 100. Example: 100.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | GetAuthTracesResponse200]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        user_apikey_id=user_apikey_id,
        company_id=company_id,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    user_id: int | Unset = UNSET,
    user_apikey_id: int | Unset = UNSET,
    company_id: int | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
) -> ErrorBody | GetAuthTracesResponse200 | None:
    """Auth Traces: Get

     Get authentication trace history for the current user.
    You may pass an optional `user_id` query parameter to view traces for any user (of your company).
    Optionally filter by `company_id` to see all traces for users of a specific company.
    Optionally filter by `user_apikey_id` to see usage history for a specific API key.
    Defaults to your user.
    Going back maximum 365 days.

    ***Requires authorization.***

    Args:
        user_id (int | Unset):
        user_apikey_id (int | Unset):
        company_id (int | Unset):
        limit (int | Unset):  Default: 100. Example: 100.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | GetAuthTracesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            user_id=user_id,
            user_apikey_id=user_apikey_id,
            company_id=company_id,
            limit=limit,
            offset=offset,
        )
    ).parsed
