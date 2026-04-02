from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient
from ...client import Client
from ...models.error_body import ErrorBody
from ...models.paginated_configuration_history import PaginatedConfigurationHistory
from ...types import UNSET
from ...types import Response
from ...types import Unset


def _get_kwargs(
    subtransaction_id: int,
    attachment_id: int,
    *,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/subtransaction/{subtransaction_id}/attachment/{attachment_id}/history".format(
            subtransaction_id=quote(str(subtransaction_id), safe=""),
            attachment_id=quote(str(attachment_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorBody | PaginatedConfigurationHistory | None:
    if response.status_code == 200:
        response_200 = PaginatedConfigurationHistory.from_dict(response.json())

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
) -> Response[ErrorBody | PaginatedConfigurationHistory]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    subtransaction_id: int,
    attachment_id: int,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
) -> Response[ErrorBody | PaginatedConfigurationHistory]:
    """Subtransaction: Get Attachment History

     Get Subtransaction Attachment history

    ***Requires authorization.***

    Args:
        subtransaction_id (int):  Example: 1.
        attachment_id (int):  Example: 1.
        limit (int | Unset):  Default: 100. Example: 100.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | PaginatedConfigurationHistory]
    """

    kwargs = _get_kwargs(
        subtransaction_id=subtransaction_id,
        attachment_id=attachment_id,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    subtransaction_id: int,
    attachment_id: int,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
) -> ErrorBody | PaginatedConfigurationHistory | None:
    """Subtransaction: Get Attachment History

     Get Subtransaction Attachment history

    ***Requires authorization.***

    Args:
        subtransaction_id (int):  Example: 1.
        attachment_id (int):  Example: 1.
        limit (int | Unset):  Default: 100. Example: 100.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | PaginatedConfigurationHistory
    """

    return sync_detailed(
        subtransaction_id=subtransaction_id,
        attachment_id=attachment_id,
        client=client,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    subtransaction_id: int,
    attachment_id: int,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
) -> Response[ErrorBody | PaginatedConfigurationHistory]:
    """Subtransaction: Get Attachment History

     Get Subtransaction Attachment history

    ***Requires authorization.***

    Args:
        subtransaction_id (int):  Example: 1.
        attachment_id (int):  Example: 1.
        limit (int | Unset):  Default: 100. Example: 100.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | PaginatedConfigurationHistory]
    """

    kwargs = _get_kwargs(
        subtransaction_id=subtransaction_id,
        attachment_id=attachment_id,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    subtransaction_id: int,
    attachment_id: int,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
) -> ErrorBody | PaginatedConfigurationHistory | None:
    """Subtransaction: Get Attachment History

     Get Subtransaction Attachment history

    ***Requires authorization.***

    Args:
        subtransaction_id (int):  Example: 1.
        attachment_id (int):  Example: 1.
        limit (int | Unset):  Default: 100. Example: 100.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | PaginatedConfigurationHistory
    """

    return (
        await asyncio_detailed(
            subtransaction_id=subtransaction_id,
            attachment_id=attachment_id,
            client=client,
            limit=limit,
            offset=offset,
        )
    ).parsed
