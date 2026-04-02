from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient
from ...client import Client
from ...models.error_body import ErrorBody
from ...models.subclient_create import SubclientCreate
from ...models.subclient_response import SubclientResponse
from ...types import Response


def _get_kwargs(
    *,
    body: SubclientCreate,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/subclient",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorBody | SubclientResponse | None:
    if response.status_code == 200:
        response_200 = SubclientResponse.from_dict(response.json())

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
) -> Response[ErrorBody | SubclientResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: SubclientCreate,
) -> Response[ErrorBody | SubclientResponse]:
    """Subclient: Create

     Create a new Subclient.

    ***Duplicate (Conflict) Check:*** By Type, (External Key or Name (If External Key is empty))

    ***Requires authorization.***

    Args:
        body (SubclientCreate):  Example: {'name': 'Innovatech Solutions', 'external_key':
            'IS-2025-001', 'active': True, 'type': 'business', 'data': {'type': 'business',
            'legal_name': 'Innovatech Solutions LLC', 'onboarding_date': '2025-01-10'}, 'address':
            {'country_alpha_2_code': 'US', 'street_address_1': '123 Tech Park', 'city': 'Silicon
            Valley', 'state_province': 'CA', 'postal_code': '94000'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | SubclientResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: SubclientCreate,
) -> ErrorBody | SubclientResponse | None:
    """Subclient: Create

     Create a new Subclient.

    ***Duplicate (Conflict) Check:*** By Type, (External Key or Name (If External Key is empty))

    ***Requires authorization.***

    Args:
        body (SubclientCreate):  Example: {'name': 'Innovatech Solutions', 'external_key':
            'IS-2025-001', 'active': True, 'type': 'business', 'data': {'type': 'business',
            'legal_name': 'Innovatech Solutions LLC', 'onboarding_date': '2025-01-10'}, 'address':
            {'country_alpha_2_code': 'US', 'street_address_1': '123 Tech Park', 'city': 'Silicon
            Valley', 'state_province': 'CA', 'postal_code': '94000'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | SubclientResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: SubclientCreate,
) -> Response[ErrorBody | SubclientResponse]:
    """Subclient: Create

     Create a new Subclient.

    ***Duplicate (Conflict) Check:*** By Type, (External Key or Name (If External Key is empty))

    ***Requires authorization.***

    Args:
        body (SubclientCreate):  Example: {'name': 'Innovatech Solutions', 'external_key':
            'IS-2025-001', 'active': True, 'type': 'business', 'data': {'type': 'business',
            'legal_name': 'Innovatech Solutions LLC', 'onboarding_date': '2025-01-10'}, 'address':
            {'country_alpha_2_code': 'US', 'street_address_1': '123 Tech Park', 'city': 'Silicon
            Valley', 'state_province': 'CA', 'postal_code': '94000'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | SubclientResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: SubclientCreate,
) -> ErrorBody | SubclientResponse | None:
    """Subclient: Create

     Create a new Subclient.

    ***Duplicate (Conflict) Check:*** By Type, (External Key or Name (If External Key is empty))

    ***Requires authorization.***

    Args:
        body (SubclientCreate):  Example: {'name': 'Innovatech Solutions', 'external_key':
            'IS-2025-001', 'active': True, 'type': 'business', 'data': {'type': 'business',
            'legal_name': 'Innovatech Solutions LLC', 'onboarding_date': '2025-01-10'}, 'address':
            {'country_alpha_2_code': 'US', 'street_address_1': '123 Tech Park', 'city': 'Silicon
            Valley', 'state_province': 'CA', 'postal_code': '94000'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | SubclientResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
