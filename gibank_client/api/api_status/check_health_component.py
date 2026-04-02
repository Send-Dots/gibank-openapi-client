from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient
from ...client import Client
from ...models.check_health_component_component import CheckHealthComponentComponent
from ...models.error_body import ErrorBody
from ...models.health_result import HealthResult
from ...types import Response


def _get_kwargs(
    component: CheckHealthComponentComponent,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/health/{component}".format(
            component=quote(str(component), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorBody | HealthResult | None:
    if response.status_code == 200:
        response_200 = HealthResult.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorBody.from_dict(response.json())

        return response_400

    if response.status_code == 503:
        response_503 = HealthResult.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorBody | HealthResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    component: CheckHealthComponentComponent,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ErrorBody | HealthResult]:
    """API Status: Health Check (Component)

     Check health of a specific component

    ***Available by public without authorization.***

    Args:
        component (CheckHealthComponentComponent):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | HealthResult]
    """

    kwargs = _get_kwargs(
        component=component,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    component: CheckHealthComponentComponent,
    *,
    client: AuthenticatedClient | Client,
) -> ErrorBody | HealthResult | None:
    """API Status: Health Check (Component)

     Check health of a specific component

    ***Available by public without authorization.***

    Args:
        component (CheckHealthComponentComponent):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | HealthResult
    """

    return sync_detailed(
        component=component,
        client=client,
    ).parsed


async def asyncio_detailed(
    component: CheckHealthComponentComponent,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ErrorBody | HealthResult]:
    """API Status: Health Check (Component)

     Check health of a specific component

    ***Available by public without authorization.***

    Args:
        component (CheckHealthComponentComponent):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | HealthResult]
    """

    kwargs = _get_kwargs(
        component=component,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    component: CheckHealthComponentComponent,
    *,
    client: AuthenticatedClient | Client,
) -> ErrorBody | HealthResult | None:
    """API Status: Health Check (Component)

     Check health of a specific component

    ***Available by public without authorization.***

    Args:
        component (CheckHealthComponentComponent):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | HealthResult
    """

    return (
        await asyncio_detailed(
            component=component,
            client=client,
        )
    ).parsed
