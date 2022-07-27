import httpx
from msgspec import Raw
from msgspec.json import Decoder

from eth_api_spec.rpc.exceptions import RPCError
from eth_api_spec.types.rpc import Response


class Snek3:
    def __init__(self, uri: str = "http://127.0.0.1:8545"):
        self.uri = uri

    def make_request(self, method, params) -> Raw:
        payload = {"method": method, "params": params, "jsonrpc": "2.0", "id": None}
        resp = httpx.post(self.uri, json=payload)
        data = Decoder(Response).decode(resp.content)
        if data.error:
            raise RPCError(data.error.message)

        return data.result
