from typing import List, Optional

from msgspec import Struct

from eth_api_spec.types import address, byte, hash32, uint


class AccessListEntry(Struct, rename="camel"):
    address: address
    storage_keys: List[hash32]


AccessList = List[AccessListEntry]


class Transaction1559Unsigned(Struct, rename="camel"):
    type: byte
    nonce: uint
    to: Optional[address]
    gas: uint
    value: uint
    input: bytes
    max_fee_per_gas: uint
    max_priority_fee_per_gas: uint
    chain_id: uint
    access_list: AccessList


class Transaction2930Unsigned(Struct, rename="camel"):
    type: byte
    nonce: uint
    to: Optional[address]
    gas: uint
    value: uint
    input: bytes
    gas_price: uint
    chain_id: uint
    access_list: AccessList


class TransactionLegacyUnsigned(Struct, rename="camel"):
    type: bytes
    nonce: uint
    to: Optional[address]
    gas: uint
    value: uint
    input: bytes
    gas_price: uint


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


TransactionUnsigned = Transaction1559Unsigned | Transaction2930Unsigned | TransactionLegacyUnsigned
TransactionSigned = Transaction1559Signed | Transaction2930Signed | TransactionLegacySigned

rename_transaction_info = {
    "block_hash": "blockHash",
    "block_number": "blockNumber",
    "sender": "from",
    "hash": "hash",
    "transaction_index": "transactionIndex",
}


class TransactionInfo(TransactionSigned, rename=rename_transaction_info.get):
    block_hash: hash32
    block_number: uint
    sender: address
    hash: hash32
    transaction_index: uint
