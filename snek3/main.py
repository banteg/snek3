import re

from snek3.rpc import RPC
from snek3.types.base import bytesn, uint
from snek3.types.block import BlockExpanded, BlockShort
from snek3.types.receipt import Log, Receipt
from snek3.types.transaction import Transaction
from snek3.utils import encode_block_id


class Snek3(RPC):
    @property
    def accounts(self):
        return self.make_request("eth_accounts", [], list[str])

    @property
    def block_number(self):
        return self.make_request("eth_blockNumber", [], uint)

    def call(self, tx, block_id="latest"):
        return self.make_request("eth_call", [tx, encode_block_id(block_id)], bytesn)

    @property
    def chain_id(self):
        return self.make_request("eth_chainId", [], uint)

    def get_balance(self, account, block_id="latest"):
        return self.make_request("eth_getBalance", [account, encode_block_id(block_id)], uint)

    def get_block(self, block_id, with_transactions=False):
        block_id = encode_block_id(block_id)

        match block_id:
            case "pending" | "latest" | "finalized" | "safe" | "earliest":
                method = "eth_getBlockByNumber"
            case str() as i if re.match(r"0x[0-9a-f]{1,63}", i):
                method = "eth_getBlockByNumber"
            case _:
                method = "eth_getBlockByHash"

        response_type = BlockExpanded if with_transactions else BlockShort
        return self.make_request(method, [block_id, with_transactions], response_type)

    def get_code(self, account, block_id="latest"):
        return self.make_request("eth_getCode", [account, encode_block_id(block_id)], bytesn)

    def get_logs(self, params):
        return self.make_request("eth_getLogs", [params], list[Log])

    def get_storage_at(self, account, slot: int, block_id="latest"):
        return self.make_request(
            "eth_getStorageAt", [account, hex(slot), encode_block_id(block_id)], bytesn
        )

    def get_transaction(self, hash):
        return self.make_request("eth_getTransactionByHash", [hash], Transaction)

    def get_nonce(self, account, block="latest"):
        return self.make_request("eth_getTransactionCount", [account, encode_block_id(block)], uint)

    def get_receipt(self, hash):
        return self.make_request("eth_getTransactionReceipt", [hash], Receipt)

    @property
    def client_version(self):
        return self.make_request("web3_clientVersion", [])
