from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient
from ...client import Client
from ...models.error_body import ErrorBody
from ...models.subtransaction_fields import SubtransactionFields
from ...models.update_transaction_subtransaction_link_body import (
    UpdateTransactionSubtransactionLinkBody,
)
from ...types import Response


def _get_kwargs(
    transaction_id: int,
    subtransaction_id: int,
    *,
    body: UpdateTransactionSubtransactionLinkBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/transaction/{transaction_id}/subtransaction/{subtransaction_id}".format(
            transaction_id=quote(str(transaction_id), safe=""),
            subtransaction_id=quote(str(subtransaction_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorBody | SubtransactionFields | None:
    if response.status_code == 200:
        response_200 = SubtransactionFields.from_dict(response.json())

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
) -> Response[ErrorBody | SubtransactionFields]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    transaction_id: int,
    subtransaction_id: int,
    *,
    client: AuthenticatedClient,
    body: UpdateTransactionSubtransactionLinkBody,
) -> Response[ErrorBody | SubtransactionFields]:
    """Transaction: Update Subtransaction Link

     Update an existing transaction subtransaction link. Useful to delete a transaction subtransaction
    link.

    ***Requires authorization.***

    Args:
        transaction_id (int):  Example: 1.
        subtransaction_id (int):  Example: 1.
        body (UpdateTransactionSubtransactionLinkBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | SubtransactionFields]
    """

    kwargs = _get_kwargs(
        transaction_id=transaction_id,
        subtransaction_id=subtransaction_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    transaction_id: int,
    subtransaction_id: int,
    *,
    client: AuthenticatedClient,
    body: UpdateTransactionSubtransactionLinkBody,
) -> ErrorBody | SubtransactionFields | None:
    """Transaction: Update Subtransaction Link

     Update an existing transaction subtransaction link. Useful to delete a transaction subtransaction
    link.

    ***Requires authorization.***

    Args:
        transaction_id (int):  Example: 1.
        subtransaction_id (int):  Example: 1.
        body (UpdateTransactionSubtransactionLinkBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | SubtransactionFields
    """

    return sync_detailed(
        transaction_id=transaction_id,
        subtransaction_id=subtransaction_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    transaction_id: int,
    subtransaction_id: int,
    *,
    client: AuthenticatedClient,
    body: UpdateTransactionSubtransactionLinkBody,
) -> Response[ErrorBody | SubtransactionFields]:
    """Transaction: Update Subtransaction Link

     Update an existing transaction subtransaction link. Useful to delete a transaction subtransaction
    link.

    ***Requires authorization.***

    Args:
        transaction_id (int):  Example: 1.
        subtransaction_id (int):  Example: 1.
        body (UpdateTransactionSubtransactionLinkBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | SubtransactionFields]
    """

    kwargs = _get_kwargs(
        transaction_id=transaction_id,
        subtransaction_id=subtransaction_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    transaction_id: int,
    subtransaction_id: int,
    *,
    client: AuthenticatedClient,
    body: UpdateTransactionSubtransactionLinkBody,
) -> ErrorBody | SubtransactionFields | None:
    """Transaction: Update Subtransaction Link

     Update an existing transaction subtransaction link. Useful to delete a transaction subtransaction
    link.

    ***Requires authorization.***

    Args:
        transaction_id (int):  Example: 1.
        subtransaction_id (int):  Example: 1.
        body (UpdateTransactionSubtransactionLinkBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | SubtransactionFields
    """

    return (
        await asyncio_detailed(
            transaction_id=transaction_id,
            subtransaction_id=subtransaction_id,
            client=client,
            body=body,
        )
    ).parsed
