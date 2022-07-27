from functools import partial

import httpx
from msgspec import Raw
from msgspec.json import Decoder

from snek3.rpc.exceptions import RPCError
from snek3.types.rpc import Response
from snek3.methods.block import GetBlock

method_handlers = {
    "get_block": GetBlock,
}


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

    def call_method(self, method, *args, **kwargs):
        print(method, args, **kwargs)
        handler = method_handlers[method](*args, **kwargs)
        result = self.make_request(handler.method, handler.params)
        return handler.decode_response(result)
