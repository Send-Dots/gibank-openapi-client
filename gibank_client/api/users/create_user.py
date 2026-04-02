from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient
from ...client import Client
from ...models.error_body import ErrorBody
from ...models.user_create_base import UserCreateBase
from ...models.user_response_base import UserResponseBase
from ...types import Response


def _get_kwargs(
    *,
    body: UserCreateBase,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/user",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorBody | UserResponseBase | None:
    if response.status_code == 200:
        response_200 = UserResponseBase.from_dict(response.json())

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
) -> Response[ErrorBody | UserResponseBase]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: UserCreateBase,
) -> Response[ErrorBody | UserResponseBase]:
    """User: Create

     Create (invite) a new user

    ***Duplicate (Conflict) Check:*** By E-Mail

    ***Requires authorization.***

    Args:
        body (UserCreateBase):  Example: {'email': 'new.user@example.com', 'full_name': 'New User
            Name', 'relationship': 'employee', 'role_id': 5}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | UserResponseBase]
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
    body: UserCreateBase,
) -> ErrorBody | UserResponseBase | None:
    """User: Create

     Create (invite) a new user

    ***Duplicate (Conflict) Check:*** By E-Mail

    ***Requires authorization.***

    Args:
        body (UserCreateBase):  Example: {'email': 'new.user@example.com', 'full_name': 'New User
            Name', 'relationship': 'employee', 'role_id': 5}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | UserResponseBase
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: UserCreateBase,
) -> Response[ErrorBody | UserResponseBase]:
    """User: Create

     Create (invite) a new user

    ***Duplicate (Conflict) Check:*** By E-Mail

    ***Requires authorization.***

    Args:
        body (UserCreateBase):  Example: {'email': 'new.user@example.com', 'full_name': 'New User
            Name', 'relationship': 'employee', 'role_id': 5}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | UserResponseBase]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: UserCreateBase,
) -> ErrorBody | UserResponseBase | None:
    """User: Create

     Create (invite) a new user

    ***Duplicate (Conflict) Check:*** By E-Mail

    ***Requires authorization.***

    Args:
        body (UserCreateBase):  Example: {'email': 'new.user@example.com', 'full_name': 'New User
            Name', 'relationship': 'employee', 'role_id': 5}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | UserResponseBase
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
