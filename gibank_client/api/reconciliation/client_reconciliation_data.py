from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient
from ...client import Client
from ...models.client_reconciliation_data_body import ClientReconciliationDataBody
from ...models.client_reconciliation_data_response_200 import (
    ClientReconciliationDataResponse200,
)
from ...models.error_body import ErrorBody
from ...types import Response


def _get_kwargs(
    *,
    body: ClientReconciliationDataBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/reconciliation",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ClientReconciliationDataResponse200 | ErrorBody | None:
    if response.status_code == 200:
        response_200 = ClientReconciliationDataResponse200.from_dict(response.json())

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
) -> Response[ClientReconciliationDataResponse200 | ErrorBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ClientReconciliationDataBody,
) -> Response[ClientReconciliationDataResponse200 | ErrorBody]:
    """Reconciliation: Client Data

     Provide data tracked by the Client to reconcile with GIB API data.

    Virtual account balances are recalculated everyday at 5:40 PM Central Time.
    Client to provide expected virtual account balances after 6 PM Central Time on the same day.
    Client to provide all transactions created between 5:40 PM the day before and 5:40 PM that day.

    Data will be compared and results will be reviewed by the GIB reconciliation team.

    If the Client needs to make corrections they will be contacted by the GIB reconciliation team.

    ***Requires authorization.***

    Args:
        body (ClientReconciliationDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ClientReconciliationDataResponse200 | ErrorBody]
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
    body: ClientReconciliationDataBody,
) -> ClientReconciliationDataResponse200 | ErrorBody | None:
    """Reconciliation: Client Data

     Provide data tracked by the Client to reconcile with GIB API data.

    Virtual account balances are recalculated everyday at 5:40 PM Central Time.
    Client to provide expected virtual account balances after 6 PM Central Time on the same day.
    Client to provide all transactions created between 5:40 PM the day before and 5:40 PM that day.

    Data will be compared and results will be reviewed by the GIB reconciliation team.

    If the Client needs to make corrections they will be contacted by the GIB reconciliation team.

    ***Requires authorization.***

    Args:
        body (ClientReconciliationDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ClientReconciliationDataResponse200 | ErrorBody
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ClientReconciliationDataBody,
) -> Response[ClientReconciliationDataResponse200 | ErrorBody]:
    """Reconciliation: Client Data

     Provide data tracked by the Client to reconcile with GIB API data.

    Virtual account balances are recalculated everyday at 5:40 PM Central Time.
    Client to provide expected virtual account balances after 6 PM Central Time on the same day.
    Client to provide all transactions created between 5:40 PM the day before and 5:40 PM that day.

    Data will be compared and results will be reviewed by the GIB reconciliation team.

    If the Client needs to make corrections they will be contacted by the GIB reconciliation team.

    ***Requires authorization.***

    Args:
        body (ClientReconciliationDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ClientReconciliationDataResponse200 | ErrorBody]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ClientReconciliationDataBody,
) -> ClientReconciliationDataResponse200 | ErrorBody | None:
    """Reconciliation: Client Data

     Provide data tracked by the Client to reconcile with GIB API data.

    Virtual account balances are recalculated everyday at 5:40 PM Central Time.
    Client to provide expected virtual account balances after 6 PM Central Time on the same day.
    Client to provide all transactions created between 5:40 PM the day before and 5:40 PM that day.

    Data will be compared and results will be reviewed by the GIB reconciliation team.

    If the Client needs to make corrections they will be contacted by the GIB reconciliation team.

    ***Requires authorization.***

    Args:
        body (ClientReconciliationDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ClientReconciliationDataResponse200 | ErrorBody
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
