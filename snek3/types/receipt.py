from typing import List

from msgspec import Struct

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


receipt_rename = {
    "transaction_hash": "transactionHash",
    "transaction_index": "transactionIndex",
    "block_hash": "blockHash",
    "block_number": "blockNumber",
    "sender": "from",  # the culprit
    "cumulative_gas_used": "cumulativeGasUsed",
    "gas_used": "gasUsed",
    "contract_address": "contractAddress",
    "logs_bloom": "logsBloom",
    "effective_gas_price": "effectiveGasPrice",
}


class Receipt(Struct, rename=lambda item: receipt_rename.get(item, item)):
    transaction_hash: hash32
    transaction_index: uint
    block_hash: hash32
    block_number: uint
    sender: address
    to: address | None
    cumulative_gas_used: uint
    gas_used: uint
    contract_address: address | None
    logs: List[Log]
    logs_bloom: bytes256
    status: uint
    effective_gas_price: uint
