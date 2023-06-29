from msgspec import Struct, field

from snek3.types.base import address, hash32, uint, bytesn


class AccessListEntry(Struct, rename="camel"):
    address: address
    storage_keys: list[hash32]


AccessList = list[AccessListEntry]


class TransactionBase(Struct, rename="camel"):
    # `type` field is omitted since it's used in the tagged union

    nonce: uint
    to: address | None  # null for contract deployments
    gas: uint
    value: uint
    input: bytesn
    chain_id: uint | None  # null for v in {27, 28}, otherwise derived from eip-155

    # details
    block_hash: hash32
    block_number: uint
    sender: address = field(name="from")
    hash: hash32
    transaction_index: uint

    # signature
    v: uint
    r: uint
    s: uint


class TransactionLegacy(TransactionBase, tag="0x0"):
    gas_price: uint


class Transaction2930(TransactionBase, tag="0x1"):
    gas_price: uint
    access_list: AccessList | None = None


class Transaction1559(TransactionBase, tag="0x2"):
    max_fee_per_gas: uint
    max_priority_fee_per_gas: uint
    access_list: AccessList | None = None


Transaction = TransactionLegacy | Transaction1559 | Transaction2930
