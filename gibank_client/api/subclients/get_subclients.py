from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient
from ...client import Client
from ...models.error_body import ErrorBody
from ...models.get_subclients_relationship_type import GetSubclientsRelationshipType
from ...models.get_subclients_response_200 import GetSubclientsResponse200
from ...models.get_subclients_state import GetSubclientsState
from ...models.get_subclients_type import GetSubclientsType
from ...types import UNSET
from ...types import Response
from ...types import Unset


def _get_kwargs(
    *,
    limit: int | Unset = 25,
    offset: int | Unset = 0,
    id: str | Unset = UNSET,
    type_: GetSubclientsType | Unset = UNSET,
    relationship_type: GetSubclientsRelationshipType | Unset = UNSET,
    state: GetSubclientsState | Unset = UNSET,
    external_key: str | Unset = UNSET,
    name: str | Unset = UNSET,
    company_name: str | Unset = UNSET,
    account_number: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params["id"] = id

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    json_relationship_type: str | Unset = UNSET
    if not isinstance(relationship_type, Unset):
        json_relationship_type = relationship_type.value

    params["relationship_type"] = json_relationship_type

    json_state: str | Unset = UNSET
    if not isinstance(state, Unset):
        json_state = state.value

    params["state"] = json_state

    params["external_key"] = external_key

    params["name"] = name

    params["company_name"] = company_name

    params["account_number"] = account_number

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/subclient",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorBody | GetSubclientsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetSubclientsResponse200.from_dict(response.json())

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
) -> Response[ErrorBody | GetSubclientsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 25,
    offset: int | Unset = 0,
    id: str | Unset = UNSET,
    type_: GetSubclientsType | Unset = UNSET,
    relationship_type: GetSubclientsRelationshipType | Unset = UNSET,
    state: GetSubclientsState | Unset = UNSET,
    external_key: str | Unset = UNSET,
    name: str | Unset = UNSET,
    company_name: str | Unset = UNSET,
    account_number: str | Unset = UNSET,
) -> Response[ErrorBody | GetSubclientsResponse200]:
    """Subclients: Get

     Get Subclients. Useful to see which Subclients have been created.

    ***Requires authorization.***

    Args:
        limit (int | Unset):  Default: 25. Example: 10.
        offset (int | Unset):  Default: 0.
        id (str | Unset): The subclient ID (can be multiple (array or comma separated)) Example:
            1.
        type_ (GetSubclientsType | Unset): The type of the subclient Example: business.
        relationship_type (GetSubclientsRelationshipType | Unset): The relationship of the
            subclient to the client Example: customer.
        state (GetSubclientsState | Unset): The state of the subclient Example: pending.
        external_key (str | Unset): The internal key used by bank customer (can be multiple)
            Example: EXT12345.
        name (str | Unset): The subclient name (contains, case insensitive) Example: Max
            Mustermann.
        company_name (str | Unset): The company name (contains, case insensitive) Example: ABC
            Bank.
        account_number (str | Unset): A subclient account number. Example: 12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | GetSubclientsResponse200]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        id=id,
        type_=type_,
        relationship_type=relationship_type,
        state=state,
        external_key=external_key,
        name=name,
        company_name=company_name,
        account_number=account_number,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 25,
    offset: int | Unset = 0,
    id: str | Unset = UNSET,
    type_: GetSubclientsType | Unset = UNSET,
    relationship_type: GetSubclientsRelationshipType | Unset = UNSET,
    state: GetSubclientsState | Unset = UNSET,
    external_key: str | Unset = UNSET,
    name: str | Unset = UNSET,
    company_name: str | Unset = UNSET,
    account_number: str | Unset = UNSET,
) -> ErrorBody | GetSubclientsResponse200 | None:
    """Subclients: Get

     Get Subclients. Useful to see which Subclients have been created.

    ***Requires authorization.***

    Args:
        limit (int | Unset):  Default: 25. Example: 10.
        offset (int | Unset):  Default: 0.
        id (str | Unset): The subclient ID (can be multiple (array or comma separated)) Example:
            1.
        type_ (GetSubclientsType | Unset): The type of the subclient Example: business.
        relationship_type (GetSubclientsRelationshipType | Unset): The relationship of the
            subclient to the client Example: customer.
        state (GetSubclientsState | Unset): The state of the subclient Example: pending.
        external_key (str | Unset): The internal key used by bank customer (can be multiple)
            Example: EXT12345.
        name (str | Unset): The subclient name (contains, case insensitive) Example: Max
            Mustermann.
        company_name (str | Unset): The company name (contains, case insensitive) Example: ABC
            Bank.
        account_number (str | Unset): A subclient account number. Example: 12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | GetSubclientsResponse200
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        id=id,
        type_=type_,
        relationship_type=relationship_type,
        state=state,
        external_key=external_key,
        name=name,
        company_name=company_name,
        account_number=account_number,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 25,
    offset: int | Unset = 0,
    id: str | Unset = UNSET,
    type_: GetSubclientsType | Unset = UNSET,
    relationship_type: GetSubclientsRelationshipType | Unset = UNSET,
    state: GetSubclientsState | Unset = UNSET,
    external_key: str | Unset = UNSET,
    name: str | Unset = UNSET,
    company_name: str | Unset = UNSET,
    account_number: str | Unset = UNSET,
) -> Response[ErrorBody | GetSubclientsResponse200]:
    """Subclients: Get

     Get Subclients. Useful to see which Subclients have been created.

    ***Requires authorization.***

    Args:
        limit (int | Unset):  Default: 25. Example: 10.
        offset (int | Unset):  Default: 0.
        id (str | Unset): The subclient ID (can be multiple (array or comma separated)) Example:
            1.
        type_ (GetSubclientsType | Unset): The type of the subclient Example: business.
        relationship_type (GetSubclientsRelationshipType | Unset): The relationship of the
            subclient to the client Example: customer.
        state (GetSubclientsState | Unset): The state of the subclient Example: pending.
        external_key (str | Unset): The internal key used by bank customer (can be multiple)
            Example: EXT12345.
        name (str | Unset): The subclient name (contains, case insensitive) Example: Max
            Mustermann.
        company_name (str | Unset): The company name (contains, case insensitive) Example: ABC
            Bank.
        account_number (str | Unset): A subclient account number. Example: 12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | GetSubclientsResponse200]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        id=id,
        type_=type_,
        relationship_type=relationship_type,
        state=state,
        external_key=external_key,
        name=name,
        company_name=company_name,
        account_number=account_number,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 25,
    offset: int | Unset = 0,
    id: str | Unset = UNSET,
    type_: GetSubclientsType | Unset = UNSET,
    relationship_type: GetSubclientsRelationshipType | Unset = UNSET,
    state: GetSubclientsState | Unset = UNSET,
    external_key: str | Unset = UNSET,
    name: str | Unset = UNSET,
    company_name: str | Unset = UNSET,
    account_number: str | Unset = UNSET,
) -> ErrorBody | GetSubclientsResponse200 | None:
    """Subclients: Get

     Get Subclients. Useful to see which Subclients have been created.

    ***Requires authorization.***

    Args:
        limit (int | Unset):  Default: 25. Example: 10.
        offset (int | Unset):  Default: 0.
        id (str | Unset): The subclient ID (can be multiple (array or comma separated)) Example:
            1.
        type_ (GetSubclientsType | Unset): The type of the subclient Example: business.
        relationship_type (GetSubclientsRelationshipType | Unset): The relationship of the
            subclient to the client Example: customer.
        state (GetSubclientsState | Unset): The state of the subclient Example: pending.
        external_key (str | Unset): The internal key used by bank customer (can be multiple)
            Example: EXT12345.
        name (str | Unset): The subclient name (contains, case insensitive) Example: Max
            Mustermann.
        company_name (str | Unset): The company name (contains, case insensitive) Example: ABC
            Bank.
        account_number (str | Unset): A subclient account number. Example: 12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | GetSubclientsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            id=id,
            type_=type_,
            relationship_type=relationship_type,
            state=state,
            external_key=external_key,
            name=name,
            company_name=company_name,
            account_number=account_number,
        )
    ).parsed
