from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient
from ...client import Client
from ...models.error_body import ErrorBody
from ...models.get_routing_number_info_response_200_item import (
    GetRoutingNumberInfoResponse200Item,
)
from ...models.get_routing_number_info_type import GetRoutingNumberInfoType
from ...types import UNSET
from ...types import Response


def _get_kwargs(
    routing_number: str,
    *,
    type_: GetRoutingNumberInfoType,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_type_ = type_.value
    params["type"] = json_type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/tools/routing_number_info/{routing_number}".format(
            routing_number=quote(str(routing_number), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorBody | list[GetRoutingNumberInfoResponse200Item] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetRoutingNumberInfoResponse200Item.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

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
) -> Response[ErrorBody | list[GetRoutingNumberInfoResponse200Item]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    routing_number: str,
    *,
    client: AuthenticatedClient,
    type_: GetRoutingNumberInfoType,
) -> Response[ErrorBody | list[GetRoutingNumberInfoResponse200Item]]:
    """Routing Number: Get Info

     Retrieves detailed information about a banking institution associated with the provided routing
    number and transaction type

    ***Requires authorization.***

    Args:
        routing_number (str):  Example: 091001322.
        type_ (GetRoutingNumberInfoType): The transaction type Example: icl.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | list[GetRoutingNumberInfoResponse200Item]]
    """

    kwargs = _get_kwargs(
        routing_number=routing_number,
        type_=type_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    routing_number: str,
    *,
    client: AuthenticatedClient,
    type_: GetRoutingNumberInfoType,
) -> ErrorBody | list[GetRoutingNumberInfoResponse200Item] | None:
    """Routing Number: Get Info

     Retrieves detailed information about a banking institution associated with the provided routing
    number and transaction type

    ***Requires authorization.***

    Args:
        routing_number (str):  Example: 091001322.
        type_ (GetRoutingNumberInfoType): The transaction type Example: icl.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | list[GetRoutingNumberInfoResponse200Item]
    """

    return sync_detailed(
        routing_number=routing_number,
        client=client,
        type_=type_,
    ).parsed


async def asyncio_detailed(
    routing_number: str,
    *,
    client: AuthenticatedClient,
    type_: GetRoutingNumberInfoType,
) -> Response[ErrorBody | list[GetRoutingNumberInfoResponse200Item]]:
    """Routing Number: Get Info

     Retrieves detailed information about a banking institution associated with the provided routing
    number and transaction type

    ***Requires authorization.***

    Args:
        routing_number (str):  Example: 091001322.
        type_ (GetRoutingNumberInfoType): The transaction type Example: icl.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | list[GetRoutingNumberInfoResponse200Item]]
    """

    kwargs = _get_kwargs(
        routing_number=routing_number,
        type_=type_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    routing_number: str,
    *,
    client: AuthenticatedClient,
    type_: GetRoutingNumberInfoType,
) -> ErrorBody | list[GetRoutingNumberInfoResponse200Item] | None:
    """Routing Number: Get Info

     Retrieves detailed information about a banking institution associated with the provided routing
    number and transaction type

    ***Requires authorization.***

    Args:
        routing_number (str):  Example: 091001322.
        type_ (GetRoutingNumberInfoType): The transaction type Example: icl.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | list[GetRoutingNumberInfoResponse200Item]
    """

    return (
        await asyncio_detailed(
            routing_number=routing_number,
            client=client,
            type_=type_,
        )
    ).parsed
