from hexbytes import HexBytes
from eth_utils import encode_hex
import re
from snek3.rpc.method import Method
from snek3.types.filter import FilterResults
from msgspec.json import Decoder
from snek3.hooks import dec_hook


class GetLogs(Method):
    def encode_payload(self, address=None, topics=None, from_block=None, to_block=None):
        method = "eth_getLogs"
        params = [
            {
                "address": address,
                "topics": topics,
                "fromBlock": hex(from_block),
                "toBlock": hex(to_block),
            }
        ]
        self.decoder = Decoder(FilterResults, dec_hook=dec_hook)

        return method, params
