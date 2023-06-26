from typing import Any
import httpx
from msgspec import Raw
from msgspec.json import Decoder

from snek3.hooks import dec_hook
from snek3.rpc.exceptions import RPCError
from snek3.types.rpc import Response


class RPC:
    def __init__(self, uri: str = "http://127.0.0.1:8545"):
        self.uri = uri
        self.client = httpx.Client()

    def raw_request(self, method, params) -> Raw:
        payload = {"method": method, "params": params, "jsonrpc": "2.0", "id": None}
        resp = self.client.post(self.uri, json=payload)
        data = Decoder(Response).decode(resp.content)
        if data.error:
            raise RPCError(data.error.message)

        return data.result

    def make_request(self, method, params, response_type=Any):
        result = self.raw_request(method, params)
        return Decoder(response_type, dec_hook=dec_hook).decode(result)
