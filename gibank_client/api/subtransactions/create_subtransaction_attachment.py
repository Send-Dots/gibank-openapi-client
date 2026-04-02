from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient
from ...client import Client
from ...models.attachment_create_with_file import AttachmentCreateWithFile
from ...models.attachment_create_with_text import AttachmentCreateWithText
from ...models.attachment_fields import AttachmentFields
from ...models.error_body import ErrorBody
from ...types import Response


def _get_kwargs(
    subtransaction_id: int,
    *,
    body: AttachmentCreateWithFile | AttachmentCreateWithText,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/subtransaction/{subtransaction_id}/attachment".format(
            subtransaction_id=quote(str(subtransaction_id), safe=""),
        ),
    }

    if isinstance(body, AttachmentCreateWithFile):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AttachmentFields | ErrorBody | None:
    if response.status_code == 200:
        response_200 = AttachmentFields.from_dict(response.json())

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
) -> Response[AttachmentFields | ErrorBody]:
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
    body: AttachmentCreateWithFile | AttachmentCreateWithText,
) -> Response[AttachmentFields | ErrorBody]:
    """Subtransaction: Create Attachment

     Create a new Subtransaction attachment. Useful to add attachments to Subtransactions.

    ***Requires authorization.***

    Args:
        subtransaction_id (int):  Example: 1.
        body (AttachmentCreateWithFile | AttachmentCreateWithText):  Example:
            {'category_and_type': {'category': 'natural_person_identification', 'type': 'passport'},
            'description': "John Doe's Passport Scan (File)", 'active': True, 'url':
            'https://s3-temporary-url.example.com/temp/passport_johndoe.pdf', 'file_name_original':
            'passport_johndoe.pdf', 'file_extension': 'pdf', 'file_create_date_time':
            '2022-08-15T00:00:00.000Z'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AttachmentFields | ErrorBody]
    """

    kwargs = _get_kwargs(
        subtransaction_id=subtransaction_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    subtransaction_id: int,
    *,
    client: AuthenticatedClient,
    body: AttachmentCreateWithFile | AttachmentCreateWithText,
) -> AttachmentFields | ErrorBody | None:
    """Subtransaction: Create Attachment

     Create a new Subtransaction attachment. Useful to add attachments to Subtransactions.

    ***Requires authorization.***

    Args:
        subtransaction_id (int):  Example: 1.
        body (AttachmentCreateWithFile | AttachmentCreateWithText):  Example:
            {'category_and_type': {'category': 'natural_person_identification', 'type': 'passport'},
            'description': "John Doe's Passport Scan (File)", 'active': True, 'url':
            'https://s3-temporary-url.example.com/temp/passport_johndoe.pdf', 'file_name_original':
            'passport_johndoe.pdf', 'file_extension': 'pdf', 'file_create_date_time':
            '2022-08-15T00:00:00.000Z'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AttachmentFields | ErrorBody
    """

    return sync_detailed(
        subtransaction_id=subtransaction_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    subtransaction_id: int,
    *,
    client: AuthenticatedClient,
    body: AttachmentCreateWithFile | AttachmentCreateWithText,
) -> Response[AttachmentFields | ErrorBody]:
    """Subtransaction: Create Attachment

     Create a new Subtransaction attachment. Useful to add attachments to Subtransactions.

    ***Requires authorization.***

    Args:
        subtransaction_id (int):  Example: 1.
        body (AttachmentCreateWithFile | AttachmentCreateWithText):  Example:
            {'category_and_type': {'category': 'natural_person_identification', 'type': 'passport'},
            'description': "John Doe's Passport Scan (File)", 'active': True, 'url':
            'https://s3-temporary-url.example.com/temp/passport_johndoe.pdf', 'file_name_original':
            'passport_johndoe.pdf', 'file_extension': 'pdf', 'file_create_date_time':
            '2022-08-15T00:00:00.000Z'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AttachmentFields | ErrorBody]
    """

    kwargs = _get_kwargs(
        subtransaction_id=subtransaction_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    subtransaction_id: int,
    *,
    client: AuthenticatedClient,
    body: AttachmentCreateWithFile | AttachmentCreateWithText,
) -> AttachmentFields | ErrorBody | None:
    """Subtransaction: Create Attachment

     Create a new Subtransaction attachment. Useful to add attachments to Subtransactions.

    ***Requires authorization.***

    Args:
        subtransaction_id (int):  Example: 1.
        body (AttachmentCreateWithFile | AttachmentCreateWithText):  Example:
            {'category_and_type': {'category': 'natural_person_identification', 'type': 'passport'},
            'description': "John Doe's Passport Scan (File)", 'active': True, 'url':
            'https://s3-temporary-url.example.com/temp/passport_johndoe.pdf', 'file_name_original':
            'passport_johndoe.pdf', 'file_extension': 'pdf', 'file_create_date_time':
            '2022-08-15T00:00:00.000Z'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AttachmentFields | ErrorBody
    """

    return (
        await asyncio_detailed(
            subtransaction_id=subtransaction_id,
            client=client,
            body=body,
        )
    ).parsed
