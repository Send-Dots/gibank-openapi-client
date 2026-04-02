from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient
from ...client import Client
from ...models.error_body import ErrorBody
from ...models.webhook_subscription_create import WebhookSubscriptionCreate
from ...models.webhook_subscription_fields import WebhookSubscriptionFields
from ...types import Response


def _get_kwargs(
    *,
    body: WebhookSubscriptionCreate,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/webhook/subscription",
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
    *,
    client: AuthenticatedClient,
    body: WebhookSubscriptionCreate,
) -> Response[ErrorBody | WebhookSubscriptionFields]:
    """Webhook Subscription: Create

     Create a new Webhook Subscription. Needed if you want to get notified by Webhooks.

    ***Duplicate (Conflict) Check:*** (/)

    ***Requires authorization.***

    Args:
        body (WebhookSubscriptionCreate):  Example: {'name': 'My Transaction Processing Webhook',
            'url': 'https://webhooks.mydomain.com/listener', 'event_type_filter':
            '.*_transaction_processed', 'active': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | WebhookSubscriptionFields]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: WebhookSubscriptionCreate,
) -> ErrorBody | WebhookSubscriptionFields | None:
    """Webhook Subscription: Create

     Create a new Webhook Subscription. Needed if you want to get notified by Webhooks.

    ***Duplicate (Conflict) Check:*** (/)

    ***Requires authorization.***

    Args:
        body (WebhookSubscriptionCreate):  Example: {'name': 'My Transaction Processing Webhook',
            'url': 'https://webhooks.mydomain.com/listener', 'event_type_filter':
            '.*_transaction_processed', 'active': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | WebhookSubscriptionFields
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: WebhookSubscriptionCreate,
) -> Response[ErrorBody | WebhookSubscriptionFields]:
    """Webhook Subscription: Create

     Create a new Webhook Subscription. Needed if you want to get notified by Webhooks.

    ***Duplicate (Conflict) Check:*** (/)

    ***Requires authorization.***

    Args:
        body (WebhookSubscriptionCreate):  Example: {'name': 'My Transaction Processing Webhook',
            'url': 'https://webhooks.mydomain.com/listener', 'event_type_filter':
            '.*_transaction_processed', 'active': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | WebhookSubscriptionFields]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: WebhookSubscriptionCreate,
) -> ErrorBody | WebhookSubscriptionFields | None:
    """Webhook Subscription: Create

     Create a new Webhook Subscription. Needed if you want to get notified by Webhooks.

    ***Duplicate (Conflict) Check:*** (/)

    ***Requires authorization.***

    Args:
        body (WebhookSubscriptionCreate):  Example: {'name': 'My Transaction Processing Webhook',
            'url': 'https://webhooks.mydomain.com/listener', 'event_type_filter':
            '.*_transaction_processed', 'active': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | WebhookSubscriptionFields
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
