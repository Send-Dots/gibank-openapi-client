from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient
from ...client import Client
from ...models.error_body import ErrorBody
from ...models.subclient_account_response import SubclientAccountResponse
from ...models.subclient_account_update import SubclientAccountUpdate
from ...types import Response


def _get_kwargs(
    subclient_id: int,
    subclient_account_id: int,
    *,
    body: SubclientAccountUpdate,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/subclient/{subclient_id}/account/{subclient_account_id}".format(
            subclient_id=quote(str(subclient_id), safe=""),
            subclient_account_id=quote(str(subclient_account_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorBody | SubclientAccountResponse | None:
    if response.status_code == 200:
        response_200 = SubclientAccountResponse.from_dict(response.json())

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

    if response.status_code == 409:
        response_409 = ErrorBody.from_dict(response.json())

        return response_409

    if response.status_code == 500:
        response_500 = ErrorBody.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorBody | SubclientAccountResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    subclient_id: int,
    subclient_account_id: int,
    *,
    client: AuthenticatedClient,
    body: SubclientAccountUpdate,
) -> Response[ErrorBody | SubclientAccountResponse]:
    """Subclient Account: Update

     Update subclient account

    ***Duplicate (Conflict) Check:*** By Routing and Account Number

    ***Requires authorization.***

    Args:
        subclient_id (int):  Example: 1.
        subclient_account_id (int):  Example: 1.
        body (SubclientAccountUpdate):  Example: {'description': 'Updated account information',
            'active': False}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | SubclientAccountResponse]
    """

    kwargs = _get_kwargs(
        subclient_id=subclient_id,
        subclient_account_id=subclient_account_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    subclient_id: int,
    subclient_account_id: int,
    *,
    client: AuthenticatedClient,
    body: SubclientAccountUpdate,
) -> ErrorBody | SubclientAccountResponse | None:
    """Subclient Account: Update

     Update subclient account

    ***Duplicate (Conflict) Check:*** By Routing and Account Number

    ***Requires authorization.***

    Args:
        subclient_id (int):  Example: 1.
        subclient_account_id (int):  Example: 1.
        body (SubclientAccountUpdate):  Example: {'description': 'Updated account information',
            'active': False}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | SubclientAccountResponse
    """

    return sync_detailed(
        subclient_id=subclient_id,
        subclient_account_id=subclient_account_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    subclient_id: int,
    subclient_account_id: int,
    *,
    client: AuthenticatedClient,
    body: SubclientAccountUpdate,
) -> Response[ErrorBody | SubclientAccountResponse]:
    """Subclient Account: Update

     Update subclient account

    ***Duplicate (Conflict) Check:*** By Routing and Account Number

    ***Requires authorization.***

    Args:
        subclient_id (int):  Example: 1.
        subclient_account_id (int):  Example: 1.
        body (SubclientAccountUpdate):  Example: {'description': 'Updated account information',
            'active': False}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | SubclientAccountResponse]
    """

    kwargs = _get_kwargs(
        subclient_id=subclient_id,
        subclient_account_id=subclient_account_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    subclient_id: int,
    subclient_account_id: int,
    *,
    client: AuthenticatedClient,
    body: SubclientAccountUpdate,
) -> ErrorBody | SubclientAccountResponse | None:
    """Subclient Account: Update

     Update subclient account

    ***Duplicate (Conflict) Check:*** By Routing and Account Number

    ***Requires authorization.***

    Args:
        subclient_id (int):  Example: 1.
        subclient_account_id (int):  Example: 1.
        body (SubclientAccountUpdate):  Example: {'description': 'Updated account information',
            'active': False}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | SubclientAccountResponse
    """

    return (
        await asyncio_detailed(
            subclient_id=subclient_id,
            subclient_account_id=subclient_account_id,
            client=client,
            body=body,
        )
    ).parsed
