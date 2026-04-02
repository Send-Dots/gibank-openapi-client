from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient
from ...client import Client
from ...models.error_body import ErrorBody
from ...models.get_file_upload_url_response_200 import GetFileUploadUrlResponse200
from ...types import UNSET
from ...types import Response


def _get_kwargs(
    *,
    content_type: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["content_type"] = content_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/file/upload_url",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorBody | GetFileUploadUrlResponse200 | None:
    if response.status_code == 200:
        response_200 = GetFileUploadUrlResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorBody.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = ErrorBody.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorBody | GetFileUploadUrlResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    content_type: str,
) -> Response[ErrorBody | GetFileUploadUrlResponse200]:
    """File: Get Upload URL

     Generate an upload URL. Can always be used, and especially needed if your data exceeds 10MB. The
    upload itself is a simply `HTTP-PUT` on the URL by passing the file bytes as body and the `Content-
    Type` header, which contains the same value as the `content_type` query parameter here.

    ***Requires authorization.***

    Args:
        content_type (str): The content type of the file that will be uploaded (Please use the
            file extension). Must be the same value as the `Content-Type` header value used when
            uploading the file. Note that `json` must be used if you are uploading a JSON file,
            because that value plays a special role in the transaction create API, to know if a raw or
            a JSON file is used. Example: icl.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | GetFileUploadUrlResponse200]
    """

    kwargs = _get_kwargs(
        content_type=content_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    content_type: str,
) -> ErrorBody | GetFileUploadUrlResponse200 | None:
    """File: Get Upload URL

     Generate an upload URL. Can always be used, and especially needed if your data exceeds 10MB. The
    upload itself is a simply `HTTP-PUT` on the URL by passing the file bytes as body and the `Content-
    Type` header, which contains the same value as the `content_type` query parameter here.

    ***Requires authorization.***

    Args:
        content_type (str): The content type of the file that will be uploaded (Please use the
            file extension). Must be the same value as the `Content-Type` header value used when
            uploading the file. Note that `json` must be used if you are uploading a JSON file,
            because that value plays a special role in the transaction create API, to know if a raw or
            a JSON file is used. Example: icl.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | GetFileUploadUrlResponse200
    """

    return sync_detailed(
        client=client,
        content_type=content_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    content_type: str,
) -> Response[ErrorBody | GetFileUploadUrlResponse200]:
    """File: Get Upload URL

     Generate an upload URL. Can always be used, and especially needed if your data exceeds 10MB. The
    upload itself is a simply `HTTP-PUT` on the URL by passing the file bytes as body and the `Content-
    Type` header, which contains the same value as the `content_type` query parameter here.

    ***Requires authorization.***

    Args:
        content_type (str): The content type of the file that will be uploaded (Please use the
            file extension). Must be the same value as the `Content-Type` header value used when
            uploading the file. Note that `json` must be used if you are uploading a JSON file,
            because that value plays a special role in the transaction create API, to know if a raw or
            a JSON file is used. Example: icl.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | GetFileUploadUrlResponse200]
    """

    kwargs = _get_kwargs(
        content_type=content_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    content_type: str,
) -> ErrorBody | GetFileUploadUrlResponse200 | None:
    """File: Get Upload URL

     Generate an upload URL. Can always be used, and especially needed if your data exceeds 10MB. The
    upload itself is a simply `HTTP-PUT` on the URL by passing the file bytes as body and the `Content-
    Type` header, which contains the same value as the `content_type` query parameter here.

    ***Requires authorization.***

    Args:
        content_type (str): The content type of the file that will be uploaded (Please use the
            file extension). Must be the same value as the `Content-Type` header value used when
            uploading the file. Note that `json` must be used if you are uploading a JSON file,
            because that value plays a special role in the transaction create API, to know if a raw or
            a JSON file is used. Example: icl.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | GetFileUploadUrlResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            content_type=content_type,
        )
    ).parsed
