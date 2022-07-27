from typing import List, Optional

from msgspec import Struct

from eth_api_spec.types.base import address, bytes256, bytes32, hash32, uint


class Log(Struct, rename="camel"):
    removed: Optional[bool]
    log_index: Optional[uint]
    transaction_index: Optional[uint]
    transaction_hash: hash32
    block_hash: Optional[hash32]
    block_number: Optional[uint]
    address: Optional[address]
    data: Optional[bytes]
    topics: Optional[List[bytes32]]


receipt_rename = {
    "transaction_hash": "transactionHash",
    "transaction_index": "transactionIndex",
    "block_hash": "blockHash",
    "block_number": "blockNumber",
    "sender": "from",  # the culprit
    "to": "to",
    "cumulative_gas_used": "cumulativeGasUsed",
    "gas_used": "gasUsed",
    "contract_address": "contractAddress",
    "logs": "logs",
    "logs_bloom": "logsBloom",
    "root": "root",
    "status": "status",
    "effective_gas_price": "effectiveGasPrice",
}


class ReceiptInfo(Struct, rename=receipt_rename.get):
    transaction_hash: hash32
    transaction_index: uint
    block_hash: hash32
    block_number: uint
    sender: address
    to: Optional[address]
    cumulative_gas_used: uint
    gas_used: uint
    contract_address: Optional[address]
    logs: List[Log]
    logs_bloom: bytes256
    root: Optional[bytes32]
    status: uint
    effective_gas_price: uint
