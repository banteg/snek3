from snek3.rpc.base import RPC
from snek3.types.base import uint, bytesn
from snek3.types.transaction import GenericTransaction
from hexbytes import HexBytes
from eth_utils import encode_hex
from snek3.types.block import BlockExpanded, BlockShort
import re


class Snek3(RPC):
    @property
    def accounts(self):
        return self.make_request("eth_accounts", [], list[str])

    @property
    def block_number(self):
        return self.make_request("eth_blockNumber", [], uint)

    def call(self, tx: GenericTransaction, block="latest"):
        return self.make_request("eth_call", [tx, block], bytesn)

    @property
    def chain_id(self):
        return self.make_request("eth_chainId", [], uint)

    def get_balance(self, account, block="latest"):
        return self.make_request("eth_getBalance", [account, block], uint)

    def get_block(self, identifier, with_transactions=False):
        method = "eth_getBlockByHash"

        match identifier:
            # block number as int
            case int() as i if i >= 0:
                method = "eth_getBlockByNumber"
                params = [hex(identifier), with_transactions]
            # block tag
            case "pending" | "latest" | "finalized" | "safe" | "earliest":
                params = [identifier, with_transactions]
            # block hash as str
            case str() as i if re.match(r"0x[0-9a-f]{64}", i):
                params = [identifier, with_transactions]
            # block number as hex
            case str() as i if re.match(r"0x[0-9a-f]+", i):
                method = "eth_getBlockByNumber"
                params = [identifier, with_transactions]
            # block hash as bytes
            case bytes() | HexBytes() as i if len(i) == 32:
                params = [encode_hex(identifier), with_transactions]
            # unknown pattern
            case _:
                raise ValueError(f"unrecognized block identifier: {identifier!r}")

        response_type = BlockExpanded if with_transactions else BlockShort
        return self.make_request(method, params, response_type)
