from functools import partial

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

    def __getattr__(self, method):
        return partial(self.call_method, method)

    def call_method(self, method, *params):
        print(method, params)
        # validate and convert params
        method, params = self.encode_payload(method, *params)

    def encode_payload(self, method, *params):
