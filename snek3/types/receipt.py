from typing import List

from msgspec import Struct, field

from snek3.types.base import address, bytes256, bytes32, hash32, uint, bytesn


class Log(Struct, rename="camel"):
    removed: bool | None
    log_index: uint | None
    transaction_index: uint | None
    transaction_hash: hash32
    block_hash: hash32 | None
    block_number: uint | None
    address: address | None
    data: bytesn | None
    topics: List[bytes32] | None


class Receipt(Struct, rename="camel"):
    transaction_hash: hash32
    transaction_index: uint
    block_hash: hash32
    block_number: uint
    sender: address = field(name="from")
    to: address | None
    cumulative_gas_used: uint
    gas_used: uint
    contract_address: address | None
    logs: List[Log]
    logs_bloom: bytes256
    status: uint
    effective_gas_price: uint
