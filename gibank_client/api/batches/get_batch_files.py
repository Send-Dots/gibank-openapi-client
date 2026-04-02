from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient
from ...client import Client
from ...models.batch_files_response import BatchFilesResponse
from ...models.error_body import ErrorBody
from ...types import Response


def _get_kwargs(
    batch_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/batch/{batch_id}/files".format(
            batch_id=quote(str(batch_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BatchFilesResponse | ErrorBody | None:
    if response.status_code == 200:
        response_200 = BatchFilesResponse.from_dict(response.json())

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
) -> Response[BatchFilesResponse | ErrorBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    batch_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[BatchFilesResponse | ErrorBody]:
    """Batch: Get Files

     Get the raw file or the parsed data that were used to create a batch. Useful to get the raw file or
    the parsed data you used when the batch has been submitted.

    For Fintech clients, access is restricted to batches where all transactions belong to their company.

    ***Requires authorization.***

    Args:
        batch_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BatchFilesResponse | ErrorBody]
    """

    kwargs = _get_kwargs(
        batch_id=batch_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    batch_id: int,
    *,
    client: AuthenticatedClient,
) -> BatchFilesResponse | ErrorBody | None:
    """Batch: Get Files

     Get the raw file or the parsed data that were used to create a batch. Useful to get the raw file or
    the parsed data you used when the batch has been submitted.

    For Fintech clients, access is restricted to batches where all transactions belong to their company.

    ***Requires authorization.***

    Args:
        batch_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BatchFilesResponse | ErrorBody
    """

    return sync_detailed(
        batch_id=batch_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    batch_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[BatchFilesResponse | ErrorBody]:
    """Batch: Get Files

     Get the raw file or the parsed data that were used to create a batch. Useful to get the raw file or
    the parsed data you used when the batch has been submitted.

    For Fintech clients, access is restricted to batches where all transactions belong to their company.

    ***Requires authorization.***

    Args:
        batch_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BatchFilesResponse | ErrorBody]
    """

    kwargs = _get_kwargs(
        batch_id=batch_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    batch_id: int,
    *,
    client: AuthenticatedClient,
) -> BatchFilesResponse | ErrorBody | None:
    """Batch: Get Files

     Get the raw file or the parsed data that were used to create a batch. Useful to get the raw file or
    the parsed data you used when the batch has been submitted.

    For Fintech clients, access is restricted to batches where all transactions belong to their company.

    ***Requires authorization.***

    Args:
        batch_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BatchFilesResponse | ErrorBody
    """

    return (
        await asyncio_detailed(
            batch_id=batch_id,
            client=client,
        )
    ).parsed
