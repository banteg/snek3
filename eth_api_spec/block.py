from typing import List, Literal

from msgspec import Struct

from eth_api_spec.transaction import TransactionSigned
from eth_api_spec.types import address, bytes8, bytes256, hash32, uint


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
    extra_data: bytes
    mix_hash: hash32
    nonce: bytes8
    size: uint
    transactions: hash32 | List[TransactionSigned]
    uncles: List[hash32]


BlockTag = Literal["earliest", "finalized", "safe", "latest", "pending"]

BlockNumberOrTag = uint | BlockTag
