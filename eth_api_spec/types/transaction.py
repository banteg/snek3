from typing import List, Optional

from msgspec import Struct

from eth_api_spec.types.base import address, byte, hash32, uint


class AccessListEntry(Struct, rename="camel"):
    address: address
    storage_keys: List[hash32]


AccessList = List[AccessListEntry]

# field renames

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

# common properties


class TransactionBase(Struct, rename=transaction_rename.get):
    type: byte
    nonce: uint
    to: Optional[address]
    gas: uint
    value: uint
    input: bytes
    chain_id: Optional[uint]


# unsigned transactions


class Transaction1559Unsigned(TransactionBase):
    max_fee_per_gas: uint
    max_priority_fee_per_gas: uint
    access_list: AccessList


class Transaction2930Unsigned(TransactionBase):
    gas_price: uint
    access_list: AccessList


class TransactionLegacyUnsigned(TransactionBase):
    gas_price: uint


# signed transactions


class Transaction1559Signed(Transaction1559Unsigned):
    y_parity: uint
    r: uint
    s: uint


class Transaction2930Signed(Transaction2930Unsigned):
    y_parity: uint
    r: uint
    s: uint


class TransactionLegacySigned(TransactionLegacyUnsigned):
    v: uint
    r: uint
    s: uint


# transaction info


class Transaction1559Info(Transaction1559Signed):
    block_hash: hash32
    block_number: uint
    sender: address
    hash: hash32
    transaction_index: uint


class Transaction2930Info(Transaction2930Signed):
    block_hash: hash32
    block_number: uint
    sender: address
    hash: hash32
    transaction_index: uint


class TransactionLegacyInfo(TransactionLegacySigned):
    block_hash: hash32
    block_number: uint
    sender: address
    hash: hash32
    transaction_index: uint


TransactionUnsigned = Transaction1559Unsigned | Transaction2930Unsigned | TransactionLegacyUnsigned
TransactionSigned = Transaction1559Signed | Transaction2930Signed | TransactionLegacySigned
TransactionInfo = Transaction1559Info | Transaction2930Info | TransactionLegacyInfo
