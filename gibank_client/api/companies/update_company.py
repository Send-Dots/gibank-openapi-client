from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient
from ...client import Client
from ...models.company_response_base import CompanyResponseBase
from ...models.company_update_base import CompanyUpdateBase
from ...models.error_body import ErrorBody
from ...types import Response


def _get_kwargs(
    company_id: int,
    *,
    body: CompanyUpdateBase,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/company/{company_id}".format(
            company_id=quote(str(company_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CompanyResponseBase | ErrorBody | None:
    if response.status_code == 200:
        response_200 = CompanyResponseBase.from_dict(response.json())

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
) -> Response[CompanyResponseBase | ErrorBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    company_id: int,
    *,
    client: AuthenticatedClient,
    body: CompanyUpdateBase,
) -> Response[CompanyResponseBase | ErrorBody]:
    """Company: Update

     Update company

    ***Requires authorization.***

    Args:
        company_id (int):
        body (CompanyUpdateBase):  Example: {'name': 'New Innovations Group'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompanyResponseBase | ErrorBody]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    company_id: int,
    *,
    client: AuthenticatedClient,
    body: CompanyUpdateBase,
) -> CompanyResponseBase | ErrorBody | None:
    """Company: Update

     Update company

    ***Requires authorization.***

    Args:
        company_id (int):
        body (CompanyUpdateBase):  Example: {'name': 'New Innovations Group'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompanyResponseBase | ErrorBody
    """

    return sync_detailed(
        company_id=company_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    company_id: int,
    *,
    client: AuthenticatedClient,
    body: CompanyUpdateBase,
) -> Response[CompanyResponseBase | ErrorBody]:
    """Company: Update

     Update company

    ***Requires authorization.***

    Args:
        company_id (int):
        body (CompanyUpdateBase):  Example: {'name': 'New Innovations Group'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompanyResponseBase | ErrorBody]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: int,
    *,
    client: AuthenticatedClient,
    body: CompanyUpdateBase,
) -> CompanyResponseBase | ErrorBody | None:
    """Company: Update

     Update company

    ***Requires authorization.***

    Args:
        company_id (int):
        body (CompanyUpdateBase):  Example: {'name': 'New Innovations Group'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompanyResponseBase | ErrorBody
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            client=client,
            body=body,
        )
    ).parsed
