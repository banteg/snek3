from typing import List, Optional

from hexbytes import HexBytes
from msgspec import Struct

from eth_api_spec.types.base import address, hash32, uint

transaction_rename = {
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


class TransactionBase(Struct, rename=transaction_rename.get):
    # `type` field is omitted since it's used in the tagged union

    nonce: uint
    to: Optional[address]
    gas: uint
    value: uint
    input: HexBytes
    chain_id: Optional[uint]

    # details
    block_hash: hash32
    block_number: uint
    sender: address
    hash: hash32
    transaction_index: uint

    # signature
    v: uint
    r: uint
    s: uint


class Transaction1559(TransactionBase, tag="0x2"):
    max_fee_per_gas: uint
    max_priority_fee_per_gas: uint
    access_list: Optional[AccessList] = None


class Transaction2930(TransactionBase, tag="0x1"):
    gas_price: uint
    access_list: Optional[AccessList] = None


class TransactionLegacy(TransactionBase, tag="0x0"):
    gas_price: uint


Transaction = Transaction1559 | Transaction2930 | TransactionLegacy
