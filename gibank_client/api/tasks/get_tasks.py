from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient
from ...client import Client
from ...models.error_body import ErrorBody
from ...models.get_tasks_involvement import GetTasksInvolvement
from ...models.get_tasks_state import GetTasksState
from ...models.get_tasks_type import GetTasksType
from ...types import UNSET
from ...types import Response
from ...types import Unset


def _get_kwargs(
    *,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    id: str | Unset = UNSET,
    type_: GetTasksType | Unset = UNSET,
    state: GetTasksState | Unset = UNSET,
    involvement: GetTasksInvolvement | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params["id"] = id

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    json_state: str | Unset = UNSET
    if not isinstance(state, Unset):
        json_state = state.value

    params["state"] = json_state

    json_involvement: str | Unset = UNSET
    if not isinstance(involvement, Unset):
        json_involvement = involvement.value

    params["involvement"] = json_involvement

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/task",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorBody | None:
    if response.status_code == 200:
        response_200 = response.json()

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
) -> Response[Any | ErrorBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    id: str | Unset = UNSET,
    type_: GetTasksType | Unset = UNSET,
    state: GetTasksState | Unset = UNSET,
    involvement: GetTasksInvolvement | Unset = UNSET,
) -> Response[Any | ErrorBody]:
    """Tasks: Get

     Get created/assigned tasks.

    ***Requires authorization.***

    Args:
        limit (int | Unset):  Default: 100. Example: 100.
        offset (int | Unset):  Default: 0.
        id (str | Unset):  Example: 1.
        type_ (GetTasksType | Unset):  Example: subclient_pending.
        state (GetTasksState | Unset):  Example: todo.
        involvement (GetTasksInvolvement | Unset):  Example: creator.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorBody]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        id=id,
        type_=type_,
        state=state,
        involvement=involvement,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    id: str | Unset = UNSET,
    type_: GetTasksType | Unset = UNSET,
    state: GetTasksState | Unset = UNSET,
    involvement: GetTasksInvolvement | Unset = UNSET,
) -> Any | ErrorBody | None:
    """Tasks: Get

     Get created/assigned tasks.

    ***Requires authorization.***

    Args:
        limit (int | Unset):  Default: 100. Example: 100.
        offset (int | Unset):  Default: 0.
        id (str | Unset):  Example: 1.
        type_ (GetTasksType | Unset):  Example: subclient_pending.
        state (GetTasksState | Unset):  Example: todo.
        involvement (GetTasksInvolvement | Unset):  Example: creator.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorBody
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        id=id,
        type_=type_,
        state=state,
        involvement=involvement,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    id: str | Unset = UNSET,
    type_: GetTasksType | Unset = UNSET,
    state: GetTasksState | Unset = UNSET,
    involvement: GetTasksInvolvement | Unset = UNSET,
) -> Response[Any | ErrorBody]:
    """Tasks: Get

     Get created/assigned tasks.

    ***Requires authorization.***

    Args:
        limit (int | Unset):  Default: 100. Example: 100.
        offset (int | Unset):  Default: 0.
        id (str | Unset):  Example: 1.
        type_ (GetTasksType | Unset):  Example: subclient_pending.
        state (GetTasksState | Unset):  Example: todo.
        involvement (GetTasksInvolvement | Unset):  Example: creator.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorBody]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        id=id,
        type_=type_,
        state=state,
        involvement=involvement,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    id: str | Unset = UNSET,
    type_: GetTasksType | Unset = UNSET,
    state: GetTasksState | Unset = UNSET,
    involvement: GetTasksInvolvement | Unset = UNSET,
) -> Any | ErrorBody | None:
    """Tasks: Get

     Get created/assigned tasks.

    ***Requires authorization.***

    Args:
        limit (int | Unset):  Default: 100. Example: 100.
        offset (int | Unset):  Default: 0.
        id (str | Unset):  Example: 1.
        type_ (GetTasksType | Unset):  Example: subclient_pending.
        state (GetTasksState | Unset):  Example: todo.
        involvement (GetTasksInvolvement | Unset):  Example: creator.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorBody
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            id=id,
            type_=type_,
            state=state,
            involvement=involvement,
        )
    ).parsed
