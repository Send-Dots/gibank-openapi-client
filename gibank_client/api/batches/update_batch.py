from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient
from ...client import Client
from ...models.batch_client_update import BatchClientUpdate
from ...models.batch_fields import BatchFields
from ...models.error_body import ErrorBody
from ...types import UNSET
from ...types import Response


def _get_kwargs(
    *,
    body: BatchClientUpdate,
    id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["id"] = id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/batch",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BatchFields | ErrorBody | None:
    if response.status_code == 200:
        response_200 = BatchFields.from_dict(response.json())

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
) -> Response[BatchFields | ErrorBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BatchClientUpdate,
    id: str,
) -> Response[BatchFields | ErrorBody]:
    """Batch: Update

     Update a batches.

    Currently a client can only update a batch to be 'canceled', and only if the batch is still in the
    'created' state.

    ***Requires authorization.***

    Args:
        id (str): The batch ID (can be multiple (array or comma separated)) Example: 1.
        body (BatchClientUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BatchFields | ErrorBody]
    """

    kwargs = _get_kwargs(
        body=body,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: BatchClientUpdate,
    id: str,
) -> BatchFields | ErrorBody | None:
    """Batch: Update

     Update a batches.

    Currently a client can only update a batch to be 'canceled', and only if the batch is still in the
    'created' state.

    ***Requires authorization.***

    Args:
        id (str): The batch ID (can be multiple (array or comma separated)) Example: 1.
        body (BatchClientUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BatchFields | ErrorBody
    """

    return sync_detailed(
        client=client,
        body=body,
        id=id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BatchClientUpdate,
    id: str,
) -> Response[BatchFields | ErrorBody]:
    """Batch: Update

     Update a batches.

    Currently a client can only update a batch to be 'canceled', and only if the batch is still in the
    'created' state.

    ***Requires authorization.***

    Args:
        id (str): The batch ID (can be multiple (array or comma separated)) Example: 1.
        body (BatchClientUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BatchFields | ErrorBody]
    """

    kwargs = _get_kwargs(
        body=body,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: BatchClientUpdate,
    id: str,
) -> BatchFields | ErrorBody | None:
    """Batch: Update

     Update a batches.

    Currently a client can only update a batch to be 'canceled', and only if the batch is still in the
    'created' state.

    ***Requires authorization.***

    Args:
        id (str): The batch ID (can be multiple (array or comma separated)) Example: 1.
        body (BatchClientUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BatchFields | ErrorBody
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            id=id,
        )
    ).parsed
