from typing import Any
import httpx
from msgspec import Raw
from msgspec.json import Decoder

from snek3.hooks import dec_hook
from snek3.exceptions import RPCError
from snek3.types.rpc import Response


class _RPCBase:
    def get_payload(self, method, params):
        return {"method": method, "params": params, "jsonrpc": "2.0", "id": None}
        
class RPC(_RPCBase):
    def __init__(self, uri: str = "http://127.0.0.1:8545"):
        self.uri = uri
        self.client = httpx.Client()

    def raw_request(self, method, params) -> Raw:
        resp = self.client.post(self.uri, json=self.get_payload(method, params))
        data = Decoder(Response).decode(resp.content)
        if data.error:
            raise RPCError(data.error.message)

        return data.result

    def make_request(self, method, params, response_type=Any):
        result = self.raw_request(method, params)
        return Decoder(response_type, dec_hook=dec_hook).decode(result)

class AsyncRPC(_RPCBase):
    def __init__(self, uri: str = "http://127.0.0.1:8545"):
        self.uri = uri
        self.client = httpx.AsyncClient()

    async def raw_request(self, method, params) -> Raw:
        resp = await self.client.post(self.uri, json=self.get_payload(method, params))
        data = Decoder(Response).decode(resp.content)
        if data.error:
            raise RPCError(data.error.message)

        return data.result

    async def make_request(self, method, params, response_type=Any):
        result = await self.raw_request(method, params)
        return Decoder(response_type, dec_hook=dec_hook).decode(result)
