from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient
from ...client import Client
from ...models.api_key_create import ApiKeyCreate
from ...models.api_key_fields import ApiKeyFields
from ...models.error_body import ErrorBody
from ...types import Response


def _get_kwargs(
    *,
    body: ApiKeyCreate,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/apikey",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiKeyFields | ErrorBody | None:
    if response.status_code == 200:
        response_200 = ApiKeyFields.from_dict(response.json())

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
) -> Response[ApiKeyFields | ErrorBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ApiKeyCreate,
) -> Response[ApiKeyFields | ErrorBody]:
    """API Key: Create

     Create a new API Key.

    ***Duplicate (Conflict) Check:*** (/)

    ***Requires authorization.***

    Args:
        body (ApiKeyCreate):  Example: {'description': 'Nightly batch processing script',
            'active': True, 'expiration_date_time': '2026-01-01T00:00:00.000Z', 'ip_whitelist':
            '203.0.113.42, 198.51.100.0/24', 'ip_blacklist': '192.0.2.10'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiKeyFields | ErrorBody]
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
    body: ApiKeyCreate,
) -> ApiKeyFields | ErrorBody | None:
    """API Key: Create

     Create a new API Key.

    ***Duplicate (Conflict) Check:*** (/)

    ***Requires authorization.***

    Args:
        body (ApiKeyCreate):  Example: {'description': 'Nightly batch processing script',
            'active': True, 'expiration_date_time': '2026-01-01T00:00:00.000Z', 'ip_whitelist':
            '203.0.113.42, 198.51.100.0/24', 'ip_blacklist': '192.0.2.10'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiKeyFields | ErrorBody
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ApiKeyCreate,
) -> Response[ApiKeyFields | ErrorBody]:
    """API Key: Create

     Create a new API Key.

    ***Duplicate (Conflict) Check:*** (/)

    ***Requires authorization.***

    Args:
        body (ApiKeyCreate):  Example: {'description': 'Nightly batch processing script',
            'active': True, 'expiration_date_time': '2026-01-01T00:00:00.000Z', 'ip_whitelist':
            '203.0.113.42, 198.51.100.0/24', 'ip_blacklist': '192.0.2.10'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiKeyFields | ErrorBody]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ApiKeyCreate,
) -> ApiKeyFields | ErrorBody | None:
    """API Key: Create

     Create a new API Key.

    ***Duplicate (Conflict) Check:*** (/)

    ***Requires authorization.***

    Args:
        body (ApiKeyCreate):  Example: {'description': 'Nightly batch processing script',
            'active': True, 'expiration_date_time': '2026-01-01T00:00:00.000Z', 'ip_whitelist':
            '203.0.113.42, 198.51.100.0/24', 'ip_blacklist': '192.0.2.10'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiKeyFields | ErrorBody
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
