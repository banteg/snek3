from functools import partial

import httpx
from msgspec import Raw
from msgspec.json import Decoder

from snek3.hooks import dec_hook
from snek3.methods.block import GetBlock
from snek3.methods.logs import GetLogs
from snek3.rpc.exceptions import RPCError
from snek3.types.rpc import Response

method_handlers = {
    "get_block": GetBlock,
    "get_logs": GetLogs,
}


class Snek3:
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

    def make_request(self, method, params):
        result = self.raw_request(method, params)
        return Decoder(dec_hook=dec_hook).decode(result)

    def __getattr__(self, method):
        return partial(self.call_method, method)

    def call_method(self, method, *args, **kwargs):
        handler = method_handlers[method](*args, **kwargs)
        result = self.raw_request(handler.method, handler.params)
        decoded = handler.decode_response(result)
        return decoded

    def batch_call(self, calls):
        handlers = []
        payloads = []
        for method, *args in calls:
            handler = method_handlers[method](*args)
            payload = [handler.method, handler.params]
            handlers.append(handler)
            payloads.append(payload)

        self.batch_request(payloads)