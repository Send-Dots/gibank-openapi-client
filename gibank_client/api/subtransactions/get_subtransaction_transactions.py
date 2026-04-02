from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient
from ...client import Client
from ...models.error_body import ErrorBody
from ...models.transaction_fields import TransactionFields
from ...types import UNSET
from ...types import Response
from ...types import Unset


def _get_kwargs(
    subtransaction_id: int,
    *,
    deleted: bool | None | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_deleted: bool | None | Unset
    if isinstance(deleted, Unset):
        json_deleted = UNSET
    else:
        json_deleted = deleted
    params["deleted"] = json_deleted

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/subtransaction/{subtransaction_id}/transaction".format(
            subtransaction_id=quote(str(subtransaction_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorBody | list[TransactionFields] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = TransactionFields.from_dict(response_200_item_data)

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
) -> Response[ErrorBody | list[TransactionFields]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    subtransaction_id: int,
    *,
    client: AuthenticatedClient,
    deleted: bool | None | Unset = UNSET,
) -> Response[ErrorBody | list[TransactionFields]]:
    """Subtransaction: Get transactions

     Get subtransaction transactions. Useful to load transactions of subtransactions.

    ***Requires authorization.***

    Args:
        subtransaction_id (int):  Example: 1.
        deleted (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | list[TransactionFields]]
    """

    kwargs = _get_kwargs(
        subtransaction_id=subtransaction_id,
        deleted=deleted,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    subtransaction_id: int,
    *,
    client: AuthenticatedClient,
    deleted: bool | None | Unset = UNSET,
) -> ErrorBody | list[TransactionFields] | None:
    """Subtransaction: Get transactions

     Get subtransaction transactions. Useful to load transactions of subtransactions.

    ***Requires authorization.***

    Args:
        subtransaction_id (int):  Example: 1.
        deleted (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | list[TransactionFields]
    """

    return sync_detailed(
        subtransaction_id=subtransaction_id,
        client=client,
        deleted=deleted,
    ).parsed


async def asyncio_detailed(
    subtransaction_id: int,
    *,
    client: AuthenticatedClient,
    deleted: bool | None | Unset = UNSET,
) -> Response[ErrorBody | list[TransactionFields]]:
    """Subtransaction: Get transactions

     Get subtransaction transactions. Useful to load transactions of subtransactions.

    ***Requires authorization.***

    Args:
        subtransaction_id (int):  Example: 1.
        deleted (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | list[TransactionFields]]
    """

    kwargs = _get_kwargs(
        subtransaction_id=subtransaction_id,
        deleted=deleted,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    subtransaction_id: int,
    *,
    client: AuthenticatedClient,
    deleted: bool | None | Unset = UNSET,
) -> ErrorBody | list[TransactionFields] | None:
    """Subtransaction: Get transactions

     Get subtransaction transactions. Useful to load transactions of subtransactions.

    ***Requires authorization.***

    Args:
        subtransaction_id (int):  Example: 1.
        deleted (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | list[TransactionFields]
    """

    return (
        await asyncio_detailed(
            subtransaction_id=subtransaction_id,
            client=client,
            deleted=deleted,
        )
    ).parsed
