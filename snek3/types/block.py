from typing import Dict, List, Literal
from hexbytes import HexBytes

from msgspec import Struct

from snek3.types.base import address, bytes8, bytes256, hash32, uint
from snek3.types.transaction import Transaction


class Block(Struct, rename="camel"):
    parent_hash: hash32
    sha3_uncles: hash32
    miner: address
    state_root: hash32
    transactions_root: hash32
    receipts_root: hash32
    logs_bloom: bytes256
    number: uint
    gas_limit: uint
    gas_used: uint
    timestamp: uint
    extra_data: HexBytes
    mix_hash: hash32
    nonce: bytes8
    size: uint
    uncles: List[hash32]


class BlockShort(Block):
    transactions: List[hash32]


class BlockExpanded(Block):
    transactions: List[Transaction]


BlockTag = Literal["earliest", "finalized", "safe", "latest", "pending"]

BlockNumberOrTag = uint | BlockTag
