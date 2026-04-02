from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient
from ...client import Client
from ...models.error_body import ErrorBody
from ...models.update_subtransaction_transaction_link_body import (
    UpdateSubtransactionTransactionLinkBody,
)
from ...types import Response


def _get_kwargs(
    subtransaction_id: int,
    transaction_id: int,
    *,
    body: UpdateSubtransactionTransactionLinkBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/subtransaction/{subtransaction_id}/transaction/{transaction_id}".format(
            subtransaction_id=quote(str(subtransaction_id), safe=""),
            transaction_id=quote(str(transaction_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorBody | None:
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
) -> Response[ErrorBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    subtransaction_id: int,
    transaction_id: int,
    *,
    client: AuthenticatedClient,
    body: UpdateSubtransactionTransactionLinkBody,
) -> Response[ErrorBody]:
    """Subtransaction: Update Transaction Link

     Update an existing subtransaction transaction link. Useful to delete a subtransaction transaction
    link.

    ***Requires authorization.***

    Args:
        subtransaction_id (int):  Example: 1.
        transaction_id (int):  Example: 1.
        body (UpdateSubtransactionTransactionLinkBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody]
    """

    kwargs = _get_kwargs(
        subtransaction_id=subtransaction_id,
        transaction_id=transaction_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    subtransaction_id: int,
    transaction_id: int,
    *,
    client: AuthenticatedClient,
    body: UpdateSubtransactionTransactionLinkBody,
) -> ErrorBody | None:
    """Subtransaction: Update Transaction Link

     Update an existing subtransaction transaction link. Useful to delete a subtransaction transaction
    link.

    ***Requires authorization.***

    Args:
        subtransaction_id (int):  Example: 1.
        transaction_id (int):  Example: 1.
        body (UpdateSubtransactionTransactionLinkBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody
    """

    return sync_detailed(
        subtransaction_id=subtransaction_id,
        transaction_id=transaction_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    subtransaction_id: int,
    transaction_id: int,
    *,
    client: AuthenticatedClient,
    body: UpdateSubtransactionTransactionLinkBody,
) -> Response[ErrorBody]:
    """Subtransaction: Update Transaction Link

     Update an existing subtransaction transaction link. Useful to delete a subtransaction transaction
    link.

    ***Requires authorization.***

    Args:
        subtransaction_id (int):  Example: 1.
        transaction_id (int):  Example: 1.
        body (UpdateSubtransactionTransactionLinkBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody]
    """

    kwargs = _get_kwargs(
        subtransaction_id=subtransaction_id,
        transaction_id=transaction_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    subtransaction_id: int,
    transaction_id: int,
    *,
    client: AuthenticatedClient,
    body: UpdateSubtransactionTransactionLinkBody,
) -> ErrorBody | None:
    """Subtransaction: Update Transaction Link

     Update an existing subtransaction transaction link. Useful to delete a subtransaction transaction
    link.

    ***Requires authorization.***

    Args:
        subtransaction_id (int):  Example: 1.
        transaction_id (int):  Example: 1.
        body (UpdateSubtransactionTransactionLinkBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody
    """

    return (
        await asyncio_detailed(
            subtransaction_id=subtransaction_id,
            transaction_id=transaction_id,
            client=client,
            body=body,
        )
    ).parsed
