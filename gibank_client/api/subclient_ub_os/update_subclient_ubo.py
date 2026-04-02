from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient
from ...client import Client
from ...models.error_body import ErrorBody
from ...models.subclient_owner_response import SubclientOwnerResponse
from ...models.subclient_owner_update import SubclientOwnerUpdate
from ...types import Response


def _get_kwargs(
    subclient_id: int,
    subclient_owner_id: int,
    *,
    body: SubclientOwnerUpdate,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/subclient/{subclient_id}/owner/{subclient_owner_id}".format(
            subclient_id=quote(str(subclient_id), safe=""),
            subclient_owner_id=quote(str(subclient_owner_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorBody | SubclientOwnerResponse | None:
    if response.status_code == 200:
        response_200 = SubclientOwnerResponse.from_dict(response.json())

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
) -> Response[ErrorBody | SubclientOwnerResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    subclient_id: int,
    subclient_owner_id: int,
    *,
    client: AuthenticatedClient,
    body: SubclientOwnerUpdate,
) -> Response[ErrorBody | SubclientOwnerResponse]:
    """Subclient UBO: Update

     Update an existing Subclient UBOs. Useful to inactivate ultimate beneficial owners.

    ***Requires authorization.***

    Args:
        subclient_id (int):  Example: 1.
        subclient_owner_id (int):  Example: 1.
        body (SubclientOwnerUpdate):  Example: {'title': 'Majority Shareholder',
            'prong_percentage': 55, 'address': {'street_address_1': '456 Looking Glass Road'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | SubclientOwnerResponse]
    """

    kwargs = _get_kwargs(
        subclient_id=subclient_id,
        subclient_owner_id=subclient_owner_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    subclient_id: int,
    subclient_owner_id: int,
    *,
    client: AuthenticatedClient,
    body: SubclientOwnerUpdate,
) -> ErrorBody | SubclientOwnerResponse | None:
    """Subclient UBO: Update

     Update an existing Subclient UBOs. Useful to inactivate ultimate beneficial owners.

    ***Requires authorization.***

    Args:
        subclient_id (int):  Example: 1.
        subclient_owner_id (int):  Example: 1.
        body (SubclientOwnerUpdate):  Example: {'title': 'Majority Shareholder',
            'prong_percentage': 55, 'address': {'street_address_1': '456 Looking Glass Road'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | SubclientOwnerResponse
    """

    return sync_detailed(
        subclient_id=subclient_id,
        subclient_owner_id=subclient_owner_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    subclient_id: int,
    subclient_owner_id: int,
    *,
    client: AuthenticatedClient,
    body: SubclientOwnerUpdate,
) -> Response[ErrorBody | SubclientOwnerResponse]:
    """Subclient UBO: Update

     Update an existing Subclient UBOs. Useful to inactivate ultimate beneficial owners.

    ***Requires authorization.***

    Args:
        subclient_id (int):  Example: 1.
        subclient_owner_id (int):  Example: 1.
        body (SubclientOwnerUpdate):  Example: {'title': 'Majority Shareholder',
            'prong_percentage': 55, 'address': {'street_address_1': '456 Looking Glass Road'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | SubclientOwnerResponse]
    """

    kwargs = _get_kwargs(
        subclient_id=subclient_id,
        subclient_owner_id=subclient_owner_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    subclient_id: int,
    subclient_owner_id: int,
    *,
    client: AuthenticatedClient,
    body: SubclientOwnerUpdate,
) -> ErrorBody | SubclientOwnerResponse | None:
    """Subclient UBO: Update

     Update an existing Subclient UBOs. Useful to inactivate ultimate beneficial owners.

    ***Requires authorization.***

    Args:
        subclient_id (int):  Example: 1.
        subclient_owner_id (int):  Example: 1.
        body (SubclientOwnerUpdate):  Example: {'title': 'Majority Shareholder',
            'prong_percentage': 55, 'address': {'street_address_1': '456 Looking Glass Road'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | SubclientOwnerResponse
    """

    return (
        await asyncio_detailed(
            subclient_id=subclient_id,
            subclient_owner_id=subclient_owner_id,
            client=client,
            body=body,
        )
    ).parsed
