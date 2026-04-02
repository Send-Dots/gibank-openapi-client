from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient
from ...client import Client
from ...models.error_body import ErrorBody
from ...models.webhook_subscription_fields import WebhookSubscriptionFields
from ...models.webhook_subscription_update import WebhookSubscriptionUpdate
from ...types import Response


def _get_kwargs(
    webhook_subscription_id: int,
    *,
    body: WebhookSubscriptionUpdate,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/webhook/subscription/{webhook_subscription_id}".format(
            webhook_subscription_id=quote(str(webhook_subscription_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorBody | WebhookSubscriptionFields | None:
    if response.status_code == 200:
        response_200 = WebhookSubscriptionFields.from_dict(response.json())

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
) -> Response[ErrorBody | WebhookSubscriptionFields]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    webhook_subscription_id: int,
    *,
    client: AuthenticatedClient,
    body: WebhookSubscriptionUpdate,
) -> Response[ErrorBody | WebhookSubscriptionFields]:
    """Webhook Subscription: Update

     Update an existing Webhook Subscription. Useful to inactivate subscriptions or to update the URL or
    the filter.

    ***Requires authorization.***

    Args:
        webhook_subscription_id (int):  Example: 1.
        body (WebhookSubscriptionUpdate):  Example: {'name': 'My Transaction Processing Webhook
            (Updated)', 'active': False}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | WebhookSubscriptionFields]
    """

    kwargs = _get_kwargs(
        webhook_subscription_id=webhook_subscription_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    webhook_subscription_id: int,
    *,
    client: AuthenticatedClient,
    body: WebhookSubscriptionUpdate,
) -> ErrorBody | WebhookSubscriptionFields | None:
    """Webhook Subscription: Update

     Update an existing Webhook Subscription. Useful to inactivate subscriptions or to update the URL or
    the filter.

    ***Requires authorization.***

    Args:
        webhook_subscription_id (int):  Example: 1.
        body (WebhookSubscriptionUpdate):  Example: {'name': 'My Transaction Processing Webhook
            (Updated)', 'active': False}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | WebhookSubscriptionFields
    """

    return sync_detailed(
        webhook_subscription_id=webhook_subscription_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    webhook_subscription_id: int,
    *,
    client: AuthenticatedClient,
    body: WebhookSubscriptionUpdate,
) -> Response[ErrorBody | WebhookSubscriptionFields]:
    """Webhook Subscription: Update

     Update an existing Webhook Subscription. Useful to inactivate subscriptions or to update the URL or
    the filter.

    ***Requires authorization.***

    Args:
        webhook_subscription_id (int):  Example: 1.
        body (WebhookSubscriptionUpdate):  Example: {'name': 'My Transaction Processing Webhook
            (Updated)', 'active': False}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | WebhookSubscriptionFields]
    """

    kwargs = _get_kwargs(
        webhook_subscription_id=webhook_subscription_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    webhook_subscription_id: int,
    *,
    client: AuthenticatedClient,
    body: WebhookSubscriptionUpdate,
) -> ErrorBody | WebhookSubscriptionFields | None:
    """Webhook Subscription: Update

     Update an existing Webhook Subscription. Useful to inactivate subscriptions or to update the URL or
    the filter.

    ***Requires authorization.***

    Args:
        webhook_subscription_id (int):  Example: 1.
        body (WebhookSubscriptionUpdate):  Example: {'name': 'My Transaction Processing Webhook
            (Updated)', 'active': False}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | WebhookSubscriptionFields
    """

    return (
        await asyncio_detailed(
            webhook_subscription_id=webhook_subscription_id,
            client=client,
            body=body,
        )
    ).parsed
