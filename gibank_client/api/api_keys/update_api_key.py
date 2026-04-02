from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient
from ...client import Client
from ...models.api_key_fields import ApiKeyFields
from ...models.api_key_update import ApiKeyUpdate
from ...models.error_body import ErrorBody
from ...types import Response


def _get_kwargs(
    apikey_id: int,
    *,
    body: ApiKeyUpdate,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/apikey/{apikey_id}".format(
            apikey_id=quote(str(apikey_id), safe=""),
        ),
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
) -> Response[ApiKeyFields | ErrorBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    apikey_id: int,
    *,
    client: AuthenticatedClient,
    body: ApiKeyUpdate,
) -> Response[ApiKeyFields | ErrorBody]:
    """API Key: Update

     Update an existing API Key. Useful to inactivate Keys or to inactivate and existing key.

    ***Requires authorization.***

    Args:
        apikey_id (int):  Example: 1.
        body (ApiKeyUpdate):  Example: {'description': 'Nightly batch processing script
            (Revoked)', 'active': False}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiKeyFields | ErrorBody]
    """

    kwargs = _get_kwargs(
        apikey_id=apikey_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    apikey_id: int,
    *,
    client: AuthenticatedClient,
    body: ApiKeyUpdate,
) -> ApiKeyFields | ErrorBody | None:
    """API Key: Update

     Update an existing API Key. Useful to inactivate Keys or to inactivate and existing key.

    ***Requires authorization.***

    Args:
        apikey_id (int):  Example: 1.
        body (ApiKeyUpdate):  Example: {'description': 'Nightly batch processing script
            (Revoked)', 'active': False}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiKeyFields | ErrorBody
    """

    return sync_detailed(
        apikey_id=apikey_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    apikey_id: int,
    *,
    client: AuthenticatedClient,
    body: ApiKeyUpdate,
) -> Response[ApiKeyFields | ErrorBody]:
    """API Key: Update

     Update an existing API Key. Useful to inactivate Keys or to inactivate and existing key.

    ***Requires authorization.***

    Args:
        apikey_id (int):  Example: 1.
        body (ApiKeyUpdate):  Example: {'description': 'Nightly batch processing script
            (Revoked)', 'active': False}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiKeyFields | ErrorBody]
    """

    kwargs = _get_kwargs(
        apikey_id=apikey_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    apikey_id: int,
    *,
    client: AuthenticatedClient,
    body: ApiKeyUpdate,
) -> ApiKeyFields | ErrorBody | None:
    """API Key: Update

     Update an existing API Key. Useful to inactivate Keys or to inactivate and existing key.

    ***Requires authorization.***

    Args:
        apikey_id (int):  Example: 1.
        body (ApiKeyUpdate):  Example: {'description': 'Nightly batch processing script
            (Revoked)', 'active': False}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiKeyFields | ErrorBody
    """

    return (
        await asyncio_detailed(
            apikey_id=apikey_id,
            client=client,
            body=body,
        )
    ).parsed
