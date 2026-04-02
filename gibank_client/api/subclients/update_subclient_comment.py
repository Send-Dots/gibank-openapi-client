from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient
from ...client import Client
from ...models.comment_fields import CommentFields
from ...models.comment_update import CommentUpdate
from ...models.error_body import ErrorBody
from ...types import Response


def _get_kwargs(
    subclient_id: int,
    comment_id: int,
    *,
    body: CommentUpdate,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/subclient/{subclient_id}/comment/{comment_id}".format(
            subclient_id=quote(str(subclient_id), safe=""),
            comment_id=quote(str(comment_id), safe=""),
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
) -> Response[CommentFields | ErrorBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    subclient_id: int,
    comment_id: int,
    *,
    client: AuthenticatedClient,
    body: CommentUpdate,
) -> Response[CommentFields | ErrorBody]:
    """Subclient: Update Comment

     Update an existing subclient comment. Useful to change a subclient comment.

    ***Requires authorization.***

    Args:
        subclient_id (int):  Example: 1.
        comment_id (int):  Example: 1.
        body (CommentUpdate):  Example: {'comment': 'Further review completed. All clear.
            (Updated)'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CommentFields | ErrorBody]
    """

    kwargs = _get_kwargs(
        subclient_id=subclient_id,
        comment_id=comment_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    subclient_id: int,
    comment_id: int,
    *,
    client: AuthenticatedClient,
    body: CommentUpdate,
) -> CommentFields | ErrorBody | None:
    """Subclient: Update Comment

     Update an existing subclient comment. Useful to change a subclient comment.

    ***Requires authorization.***

    Args:
        subclient_id (int):  Example: 1.
        comment_id (int):  Example: 1.
        body (CommentUpdate):  Example: {'comment': 'Further review completed. All clear.
            (Updated)'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CommentFields | ErrorBody
    """

    return sync_detailed(
        subclient_id=subclient_id,
        comment_id=comment_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    subclient_id: int,
    comment_id: int,
    *,
    client: AuthenticatedClient,
    body: CommentUpdate,
) -> Response[CommentFields | ErrorBody]:
    """Subclient: Update Comment

     Update an existing subclient comment. Useful to change a subclient comment.

    ***Requires authorization.***

    Args:
        subclient_id (int):  Example: 1.
        comment_id (int):  Example: 1.
        body (CommentUpdate):  Example: {'comment': 'Further review completed. All clear.
            (Updated)'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CommentFields | ErrorBody]
    """

    kwargs = _get_kwargs(
        subclient_id=subclient_id,
        comment_id=comment_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    subclient_id: int,
    comment_id: int,
    *,
    client: AuthenticatedClient,
    body: CommentUpdate,
) -> CommentFields | ErrorBody | None:
    """Subclient: Update Comment

     Update an existing subclient comment. Useful to change a subclient comment.

    ***Requires authorization.***

    Args:
        subclient_id (int):  Example: 1.
        comment_id (int):  Example: 1.
        body (CommentUpdate):  Example: {'comment': 'Further review completed. All clear.
            (Updated)'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CommentFields | ErrorBody
    """

    return (
        await asyncio_detailed(
            subclient_id=subclient_id,
            comment_id=comment_id,
            client=client,
            body=body,
        )
    ).parsed
