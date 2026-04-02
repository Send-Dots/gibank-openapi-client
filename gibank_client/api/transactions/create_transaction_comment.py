from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient
from ...client import Client
from ...models.comment_create import CommentCreate
from ...models.comment_fields import CommentFields
from ...models.error_body import ErrorBody
from ...types import Response


def _get_kwargs(
    transaction_id: int,
    *,
    body: CommentCreate,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/transaction/{transaction_id}/comment".format(
            transaction_id=quote(str(transaction_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CommentFields | ErrorBody | None:
    if response.status_code == 200:
        response_200 = CommentFields.from_dict(response.json())

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
) -> Response[CommentFields | ErrorBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    transaction_id: int,
    *,
    client: AuthenticatedClient,
    body: CommentCreate,
) -> Response[CommentFields | ErrorBody]:
    """Transaction: Create Comment

     Create a new transaction comment. Useful to add comments to transactions.

    ***Requires authorization.***

    Args:
        transaction_id (int):  Example: 1.
        body (CommentCreate):  Example: {'comment': 'This transaction needs further review due to
            amount mismatch.'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CommentFields | ErrorBody]
    """

    kwargs = _get_kwargs(
        transaction_id=transaction_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    transaction_id: int,
    *,
    client: AuthenticatedClient,
    body: CommentCreate,
) -> CommentFields | ErrorBody | None:
    """Transaction: Create Comment

     Create a new transaction comment. Useful to add comments to transactions.

    ***Requires authorization.***

    Args:
        transaction_id (int):  Example: 1.
        body (CommentCreate):  Example: {'comment': 'This transaction needs further review due to
            amount mismatch.'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CommentFields | ErrorBody
    """

    return sync_detailed(
        transaction_id=transaction_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    transaction_id: int,
    *,
    client: AuthenticatedClient,
    body: CommentCreate,
) -> Response[CommentFields | ErrorBody]:
    """Transaction: Create Comment

     Create a new transaction comment. Useful to add comments to transactions.

    ***Requires authorization.***

    Args:
        transaction_id (int):  Example: 1.
        body (CommentCreate):  Example: {'comment': 'This transaction needs further review due to
            amount mismatch.'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CommentFields | ErrorBody]
    """

    kwargs = _get_kwargs(
        transaction_id=transaction_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    transaction_id: int,
    *,
    client: AuthenticatedClient,
    body: CommentCreate,
) -> CommentFields | ErrorBody | None:
    """Transaction: Create Comment

     Create a new transaction comment. Useful to add comments to transactions.

    ***Requires authorization.***

    Args:
        transaction_id (int):  Example: 1.
        body (CommentCreate):  Example: {'comment': 'This transaction needs further review due to
            amount mismatch.'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CommentFields | ErrorBody
    """

    return (
        await asyncio_detailed(
            transaction_id=transaction_id,
            client=client,
            body=body,
        )
    ).parsed
