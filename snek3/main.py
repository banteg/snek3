from snek3.rpc.base import RPC
from snek3.types.base import uint, bytesn
from snek3.types.block import BlockNumberOrTag
from snek3.types.transaction import GenericTransaction


class Snek3(RPC):
    @property
    def accounts(self):
        return self.make_request("eth_accounts", [], list[str])

    @property
    def block_number(self):
        return self.make_request("eth_blockNumber", [], uint)

    def call(self, tx: GenericTransaction, block: BlockNumberOrTag = "latest"):
        if isinstance(block, int):
            block = hex(block)
       
        return self.make_request("eth_call", [tx, block], bytesn)

    