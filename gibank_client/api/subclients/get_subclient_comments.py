from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient
from ...client import Client
from ...models.error_body import ErrorBody
from ...models.get_subclient_comments_response_200 import (
    GetSubclientCommentsResponse200,
)
from ...types import UNSET
from ...types import Response
from ...types import Unset


def _get_kwargs(
    subclient_id: int,
    *,
    limit: int | Unset = 10,
    offset: int | Unset = 0,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/subclient/{subclient_id}/comment".format(
            subclient_id=quote(str(subclient_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorBody | GetSubclientCommentsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetSubclientCommentsResponse200.from_dict(response.json())

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
) -> Response[ErrorBody | GetSubclientCommentsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    subclient_id: int,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 10,
    offset: int | Unset = 0,
) -> Response[ErrorBody | GetSubclientCommentsResponse200]:
    """Subclient: Get Comments

     Get subclient comments. Useful to load comments of subclients.

    ***Requires authorization.***

    Args:
        subclient_id (int):  Example: 1.
        limit (int | Unset):  Default: 10. Example: 10.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | GetSubclientCommentsResponse200]
    """

    kwargs = _get_kwargs(
        subclient_id=subclient_id,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    subclient_id: int,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 10,
    offset: int | Unset = 0,
) -> ErrorBody | GetSubclientCommentsResponse200 | None:
    """Subclient: Get Comments

     Get subclient comments. Useful to load comments of subclients.

    ***Requires authorization.***

    Args:
        subclient_id (int):  Example: 1.
        limit (int | Unset):  Default: 10. Example: 10.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | GetSubclientCommentsResponse200
    """

    return sync_detailed(
        subclient_id=subclient_id,
        client=client,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    subclient_id: int,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 10,
    offset: int | Unset = 0,
) -> Response[ErrorBody | GetSubclientCommentsResponse200]:
    """Subclient: Get Comments

     Get subclient comments. Useful to load comments of subclients.

    ***Requires authorization.***

    Args:
        subclient_id (int):  Example: 1.
        limit (int | Unset):  Default: 10. Example: 10.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | GetSubclientCommentsResponse200]
    """

    kwargs = _get_kwargs(
        subclient_id=subclient_id,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    subclient_id: int,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 10,
    offset: int | Unset = 0,
) -> ErrorBody | GetSubclientCommentsResponse200 | None:
    """Subclient: Get Comments

     Get subclient comments. Useful to load comments of subclients.

    ***Requires authorization.***

    Args:
        subclient_id (int):  Example: 1.
        limit (int | Unset):  Default: 10. Example: 10.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | GetSubclientCommentsResponse200
    """

    return (
        await asyncio_detailed(
            subclient_id=subclient_id,
            client=client,
            limit=limit,
            offset=offset,
        )
    ).parsed
