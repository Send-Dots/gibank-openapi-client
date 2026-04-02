from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient
from ...client import Client
from ...models.error_body import ErrorBody
from ...models.subclient_owner_create import SubclientOwnerCreate
from ...models.subclient_owner_response import SubclientOwnerResponse
from ...types import Response


def _get_kwargs(
    subclient_id: int,
    *,
    body: SubclientOwnerCreate,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/subclient/{subclient_id}/owner".format(
            subclient_id=quote(str(subclient_id), safe=""),
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
) -> Response[ErrorBody | SubclientOwnerResponse]:
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
    body: SubclientOwnerCreate,
) -> Response[ErrorBody | SubclientOwnerResponse]:
    """Subclient UBO: Create

     Create a new Subclient UBO.

    ***Duplicate (Conflict) Check:*** By External Key or Name if empty (If External Key is empty)

    ***Requires authorization.***

    Args:
        subclient_id (int):  Example: 1.
        body (SubclientOwnerCreate):  Example: {'name': 'Alice Wonderland', 'title':
            'Shareholder', 'active': True, 'external_key': 'AW001', 'birth_date': '1985-07-12',
            'prong_ownership': True, 'prong_percentage': 30, 'prong_control': False, 'address':
            {'street_address_1': '123 Rabbit Hole Lane', 'city': 'Curious City', 'postal_code':
            'CR123', 'country_alpha_2_code': 'GB'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | SubclientOwnerResponse]
    """

    kwargs = _get_kwargs(
        subclient_id=subclient_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    subclient_id: int,
    *,
    client: AuthenticatedClient,
    body: SubclientOwnerCreate,
) -> ErrorBody | SubclientOwnerResponse | None:
    """Subclient UBO: Create

     Create a new Subclient UBO.

    ***Duplicate (Conflict) Check:*** By External Key or Name if empty (If External Key is empty)

    ***Requires authorization.***

    Args:
        subclient_id (int):  Example: 1.
        body (SubclientOwnerCreate):  Example: {'name': 'Alice Wonderland', 'title':
            'Shareholder', 'active': True, 'external_key': 'AW001', 'birth_date': '1985-07-12',
            'prong_ownership': True, 'prong_percentage': 30, 'prong_control': False, 'address':
            {'street_address_1': '123 Rabbit Hole Lane', 'city': 'Curious City', 'postal_code':
            'CR123', 'country_alpha_2_code': 'GB'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | SubclientOwnerResponse
    """

    return sync_detailed(
        subclient_id=subclient_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    subclient_id: int,
    *,
    client: AuthenticatedClient,
    body: SubclientOwnerCreate,
) -> Response[ErrorBody | SubclientOwnerResponse]:
    """Subclient UBO: Create

     Create a new Subclient UBO.

    ***Duplicate (Conflict) Check:*** By External Key or Name if empty (If External Key is empty)

    ***Requires authorization.***

    Args:
        subclient_id (int):  Example: 1.
        body (SubclientOwnerCreate):  Example: {'name': 'Alice Wonderland', 'title':
            'Shareholder', 'active': True, 'external_key': 'AW001', 'birth_date': '1985-07-12',
            'prong_ownership': True, 'prong_percentage': 30, 'prong_control': False, 'address':
            {'street_address_1': '123 Rabbit Hole Lane', 'city': 'Curious City', 'postal_code':
            'CR123', 'country_alpha_2_code': 'GB'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | SubclientOwnerResponse]
    """

    kwargs = _get_kwargs(
        subclient_id=subclient_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    subclient_id: int,
    *,
    client: AuthenticatedClient,
    body: SubclientOwnerCreate,
) -> ErrorBody | SubclientOwnerResponse | None:
    """Subclient UBO: Create

     Create a new Subclient UBO.

    ***Duplicate (Conflict) Check:*** By External Key or Name if empty (If External Key is empty)

    ***Requires authorization.***

    Args:
        subclient_id (int):  Example: 1.
        body (SubclientOwnerCreate):  Example: {'name': 'Alice Wonderland', 'title':
            'Shareholder', 'active': True, 'external_key': 'AW001', 'birth_date': '1985-07-12',
            'prong_ownership': True, 'prong_percentage': 30, 'prong_control': False, 'address':
            {'street_address_1': '123 Rabbit Hole Lane', 'city': 'Curious City', 'postal_code':
            'CR123', 'country_alpha_2_code': 'GB'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | SubclientOwnerResponse
    """

    return (
        await asyncio_detailed(
            subclient_id=subclient_id,
            client=client,
            body=body,
        )
    ).parsed
