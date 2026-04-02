from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient
from ...client import Client
from ...models.error_body import ErrorBody
from ...models.subclient_owner_response import SubclientOwnerResponse
from ...types import Response


def _get_kwargs(
    subclient_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/subclient/{subclient_id}/owner".format(
            subclient_id=quote(str(subclient_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorBody | list[SubclientOwnerResponse] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = SubclientOwnerResponse.from_dict(response_200_item_data)

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
) -> Response[ErrorBody | list[SubclientOwnerResponse]]:
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
) -> Response[ErrorBody | list[SubclientOwnerResponse]]:
    """Subclient UBOs: Get

     Get Subclient UBOs. Useful to get ultimate benificial owners of a business Subclient.

    ***Requires authorization.***

    Args:
        subclient_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | list[SubclientOwnerResponse]]
    """

    kwargs = _get_kwargs(
        subclient_id=subclient_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    subclient_id: int,
    *,
    client: AuthenticatedClient,
) -> ErrorBody | list[SubclientOwnerResponse] | None:
    """Subclient UBOs: Get

     Get Subclient UBOs. Useful to get ultimate benificial owners of a business Subclient.

    ***Requires authorization.***

    Args:
        subclient_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | list[SubclientOwnerResponse]
    """

    return sync_detailed(
        subclient_id=subclient_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    subclient_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorBody | list[SubclientOwnerResponse]]:
    """Subclient UBOs: Get

     Get Subclient UBOs. Useful to get ultimate benificial owners of a business Subclient.

    ***Requires authorization.***

    Args:
        subclient_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | list[SubclientOwnerResponse]]
    """

    kwargs = _get_kwargs(
        subclient_id=subclient_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    subclient_id: int,
    *,
    client: AuthenticatedClient,
) -> ErrorBody | list[SubclientOwnerResponse] | None:
    """Subclient UBOs: Get

     Get Subclient UBOs. Useful to get ultimate benificial owners of a business Subclient.

    ***Requires authorization.***

    Args:
        subclient_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | list[SubclientOwnerResponse]
    """

    return (
        await asyncio_detailed(
            subclient_id=subclient_id,
            client=client,
        )
    ).parsed
