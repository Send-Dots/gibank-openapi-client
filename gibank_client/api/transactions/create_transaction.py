from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient
from ...client import Client
from ...models.create_transaction_body import CreateTransactionBody
from ...models.error_body import ErrorBody
from ...types import UNSET
from ...types import Response
from ...types import Unset


def _get_kwargs(
    *,
    body: CreateTransactionBody,
    x_duplicate_override_reason: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_duplicate_override_reason, Unset):
        headers["X-Duplicate-Override-Reason"] = x_duplicate_override_reason

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/transaction/from-subledger",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorBody | None:
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
) -> Response[ErrorBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateTransactionBody,
    x_duplicate_override_reason: str | Unset = UNSET,
) -> Response[ErrorBody]:
    """Transaction: Create From Subledger [BETA]

     Create a Transaction using subledger.

    Transaction will be a push from origin Subclient to destination Subclient.

    A Subclient Account ID should be specified if a Subclient has more than one Account.

    A True Sender and/or Ultimate Beneficiary may be supplied for a subtransaction to be created.

    For a simple 1:1 transaction, see our [Create a BOOK Transfer from Subledger
    Guide](docs/guides/create-book-transfer-from-subledger.html)

    ***Duplicate (Conflict) Check:*** By (User, External Key and Type) or (User, Type, Transfer Type,
    Transfer Code, Amount, File Create Date Time, Reference, Origin Routing Number, Origin Account
    Number, Destination Routing Number, Destination Account Number, Batch Amount, Batch nbr of
    Transactions) (If External Key is empty)

    ***Requires authorization.***

    Args:
        x_duplicate_override_reason (str | Unset):
        body (CreateTransactionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody]
    """

    kwargs = _get_kwargs(
        body=body,
        x_duplicate_override_reason=x_duplicate_override_reason,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CreateTransactionBody,
    x_duplicate_override_reason: str | Unset = UNSET,
) -> ErrorBody | None:
    """Transaction: Create From Subledger [BETA]

     Create a Transaction using subledger.

    Transaction will be a push from origin Subclient to destination Subclient.

    A Subclient Account ID should be specified if a Subclient has more than one Account.

    A True Sender and/or Ultimate Beneficiary may be supplied for a subtransaction to be created.

    For a simple 1:1 transaction, see our [Create a BOOK Transfer from Subledger
    Guide](docs/guides/create-book-transfer-from-subledger.html)

    ***Duplicate (Conflict) Check:*** By (User, External Key and Type) or (User, Type, Transfer Type,
    Transfer Code, Amount, File Create Date Time, Reference, Origin Routing Number, Origin Account
    Number, Destination Routing Number, Destination Account Number, Batch Amount, Batch nbr of
    Transactions) (If External Key is empty)

    ***Requires authorization.***

    Args:
        x_duplicate_override_reason (str | Unset):
        body (CreateTransactionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody
    """

    return sync_detailed(
        client=client,
        body=body,
        x_duplicate_override_reason=x_duplicate_override_reason,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateTransactionBody,
    x_duplicate_override_reason: str | Unset = UNSET,
) -> Response[ErrorBody]:
    """Transaction: Create From Subledger [BETA]

     Create a Transaction using subledger.

    Transaction will be a push from origin Subclient to destination Subclient.

    A Subclient Account ID should be specified if a Subclient has more than one Account.

    A True Sender and/or Ultimate Beneficiary may be supplied for a subtransaction to be created.

    For a simple 1:1 transaction, see our [Create a BOOK Transfer from Subledger
    Guide](docs/guides/create-book-transfer-from-subledger.html)

    ***Duplicate (Conflict) Check:*** By (User, External Key and Type) or (User, Type, Transfer Type,
    Transfer Code, Amount, File Create Date Time, Reference, Origin Routing Number, Origin Account
    Number, Destination Routing Number, Destination Account Number, Batch Amount, Batch nbr of
    Transactions) (If External Key is empty)

    ***Requires authorization.***

    Args:
        x_duplicate_override_reason (str | Unset):
        body (CreateTransactionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody]
    """

    kwargs = _get_kwargs(
        body=body,
        x_duplicate_override_reason=x_duplicate_override_reason,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateTransactionBody,
    x_duplicate_override_reason: str | Unset = UNSET,
) -> ErrorBody | None:
    """Transaction: Create From Subledger [BETA]

     Create a Transaction using subledger.

    Transaction will be a push from origin Subclient to destination Subclient.

    A Subclient Account ID should be specified if a Subclient has more than one Account.

    A True Sender and/or Ultimate Beneficiary may be supplied for a subtransaction to be created.

    For a simple 1:1 transaction, see our [Create a BOOK Transfer from Subledger
    Guide](docs/guides/create-book-transfer-from-subledger.html)

    ***Duplicate (Conflict) Check:*** By (User, External Key and Type) or (User, Type, Transfer Type,
    Transfer Code, Amount, File Create Date Time, Reference, Origin Routing Number, Origin Account
    Number, Destination Routing Number, Destination Account Number, Batch Amount, Batch nbr of
    Transactions) (If External Key is empty)

    ***Requires authorization.***

    Args:
        x_duplicate_override_reason (str | Unset):
        body (CreateTransactionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_duplicate_override_reason=x_duplicate_override_reason,
        )
    ).parsed
