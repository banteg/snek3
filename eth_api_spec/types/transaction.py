from typing import List, Optional
from hexbytes import HexBytes

from msgspec import Struct

from eth_api_spec.types.base import address, byte, hash32, uint


transaction_rename = {
    "type": "type",
    "nonce": "nonce",
    "sender": "from",  # the culprit
    "to": "to",
    "gas": "gas",
    "value": "value",
    "input": "input",
    "chain_id": "chainId",
    "max_fee_per_gas": "maxFeePerGas",
    "max_priority_fee_per_gas": "maxPriorityFeePerGas",
    "access_list": "accessList",
    "gas_price": "gasPrice",
    "y_parity": "yParity",
    "v": "v",
    "r": "r",
    "s": "s",
    "block_hash": "blockHash",
    "block_number": "blockNumber",
    "sender": "from",
    "hash": "hash",
    "transaction_index": "transactionIndex",
}


class AccessListEntry(Struct, rename="camel"):
    address: address
    storage_keys: List[hash32]


AccessList = List[AccessListEntry]


class TransactionInfo(Struct, rename=transaction_rename.get):
    type: uint
    nonce: uint
    sender: address
    to: Optional[address]
    gas: uint
    value: uint
    input: HexBytes
    block_hash: hash32
    block_number: uint
    hash: hash32
    transaction_index: uint
    r: uint
    s: uint
    max_fee_per_gas: Optional[uint] = None
    max_priority_fee_per_gas: Optional[uint] = None
    access_list: Optional[AccessList] = None
    gas_price: Optional[uint] = None
    y_parity: Optional[uint] = None
    v: Optional[uint] = None
    chain_id: Optional[uint] = None
