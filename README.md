# gibank-openapi-client

Auto-generated Python client for the [GiBank Base API](https://sandbox-base-api.gibank-api.com/swagger.json), built with [`openapi-python-client`](https://github.com/openapi-generators/openapi-python-client).

## Installation

```bash
pip install git+https://github.com/Send-Dots/gibank-openapi-client.git
```

Or pin to a specific branch/tag:

```bash
pip install git+https://github.com/Send-Dots/gibank-openapi-client.git@main#egg=gibank-openapi-client
```

## Usage

```python
from gibank_client import AuthenticatedClient
from gibank_client.api.transactions import get_transactions

client = AuthenticatedClient(base_url="https://sandbox-base-api.gibank-api.com", token="...")
response = get_transactions.sync(client=client)
```

## Regenerating from swagger.json

1. Install dev dependencies:

   ```bash
   pip install -e ".[dev]"
   ```

2. Update `swagger.json` with the latest spec from GiBank.

3. Run the generator:

   ```bash
   make generate
   ```

   This runs `openapi-python-client update` using `openapi-python-client.yaml` for config.

4. **Re-apply manual fixes** — the generator does not correctly parse list responses for these 5 endpoints. After regeneration, manually fix them (see pattern below):

   - `gibank_client/api/balances/get_balance.py`
   - `gibank_client/api/subtransactions/get_subtransaction_transactions.py`
   - `gibank_client/api/tasks/get_tasks.py`
   - `gibank_client/api/transactions/get_transactions.py`
   - `gibank_client/api/transactions/search_transactions.py`

   In each file, the `_parse_response` function needs to handle a `200` response as a list. The generated code incorrectly parses it as a single object. Replace the 200-response block with logic that iterates and parses each item from the response JSON array.
