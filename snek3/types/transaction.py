from typing import List, Optional

from msgspec import Struct

from snek3.types.base import address, hash32, uint, bytesn

transaction_rename = {
    "sender": "from",  # the culprit
    "chain_id": "chainId",
    "max_fee_per_gas": "maxFeePerGas",
    "max_priority_fee_per_gas": "maxPriorityFeePerGas",
    "access_list": "accessList",
    "gas_price": "gasPrice",
    "block_hash": "blockHash",
    "block_number": "blockNumber",
    "transaction_index": "transactionIndex",
}


class AccessListEntry(Struct, rename="camel"):
    address: address
    storage_keys: List[hash32]


AccessList = List[AccessListEntry]


class TransactionBase(Struct, rename=lambda item: transaction_rename.get(item, item)):
    # `type` field is omitted since it's used in the tagged union

    nonce: uint
    to: Optional[address]
    gas: uint
    value: uint
    input: bytesn
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
