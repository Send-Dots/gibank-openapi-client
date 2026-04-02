from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient
from ...client import Client
from ...models.attachment_fields import AttachmentFields
from ...models.attachment_update import AttachmentUpdate
from ...models.error_body import ErrorBody
from ...types import Response


def _get_kwargs(
    subclient_id: int,
    subclient_owner_id: int,
    attachment_id: int,
    *,
    body: AttachmentUpdate,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/subclient/{subclient_id}/owner/{subclient_owner_id}/attachment/{attachment_id}".format(
            subclient_id=quote(str(subclient_id), safe=""),
            subclient_owner_id=quote(str(subclient_owner_id), safe=""),
            attachment_id=quote(str(attachment_id), safe=""),
        ),
    }

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
) -> Response[AttachmentFields | ErrorBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    subclient_id: int,
    subclient_owner_id: int,
    attachment_id: int,
    *,
    client: AuthenticatedClient,
    body: AttachmentUpdate,
) -> Response[AttachmentFields | ErrorBody]:
    """Subclient UBO: Update Attachment

     Update an existing Subclient UBO attachment. Useful to change a Subclient UBO attachment.

    ***Requires authorization.***

    Args:
        subclient_id (int):  Example: 1.
        subclient_owner_id (int):  Example: 1.
        attachment_id (int):  Example: 1.
        body (AttachmentUpdate):  Example: {'description': "John Doe's Passport Scan (verified)",
            'active': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AttachmentFields | ErrorBody]
    """

    kwargs = _get_kwargs(
        subclient_id=subclient_id,
        subclient_owner_id=subclient_owner_id,
        attachment_id=attachment_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    subclient_id: int,
    subclient_owner_id: int,
    attachment_id: int,
    *,
    client: AuthenticatedClient,
    body: AttachmentUpdate,
) -> AttachmentFields | ErrorBody | None:
    """Subclient UBO: Update Attachment

     Update an existing Subclient UBO attachment. Useful to change a Subclient UBO attachment.

    ***Requires authorization.***

    Args:
        subclient_id (int):  Example: 1.
        subclient_owner_id (int):  Example: 1.
        attachment_id (int):  Example: 1.
        body (AttachmentUpdate):  Example: {'description': "John Doe's Passport Scan (verified)",
            'active': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AttachmentFields | ErrorBody
    """

    return sync_detailed(
        subclient_id=subclient_id,
        subclient_owner_id=subclient_owner_id,
        attachment_id=attachment_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    subclient_id: int,
    subclient_owner_id: int,
    attachment_id: int,
    *,
    client: AuthenticatedClient,
    body: AttachmentUpdate,
) -> Response[AttachmentFields | ErrorBody]:
    """Subclient UBO: Update Attachment

     Update an existing Subclient UBO attachment. Useful to change a Subclient UBO attachment.

    ***Requires authorization.***

    Args:
        subclient_id (int):  Example: 1.
        subclient_owner_id (int):  Example: 1.
        attachment_id (int):  Example: 1.
        body (AttachmentUpdate):  Example: {'description': "John Doe's Passport Scan (verified)",
            'active': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AttachmentFields | ErrorBody]
    """

    kwargs = _get_kwargs(
        subclient_id=subclient_id,
        subclient_owner_id=subclient_owner_id,
        attachment_id=attachment_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    subclient_id: int,
    subclient_owner_id: int,
    attachment_id: int,
    *,
    client: AuthenticatedClient,
    body: AttachmentUpdate,
) -> AttachmentFields | ErrorBody | None:
    """Subclient UBO: Update Attachment

     Update an existing Subclient UBO attachment. Useful to change a Subclient UBO attachment.

    ***Requires authorization.***

    Args:
        subclient_id (int):  Example: 1.
        subclient_owner_id (int):  Example: 1.
        attachment_id (int):  Example: 1.
        body (AttachmentUpdate):  Example: {'description': "John Doe's Passport Scan (verified)",
            'active': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AttachmentFields | ErrorBody
    """

    return (
        await asyncio_detailed(
            subclient_id=subclient_id,
            subclient_owner_id=subclient_owner_id,
            attachment_id=attachment_id,
            client=client,
            body=body,
        )
    ).parsed
