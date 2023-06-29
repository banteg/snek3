from msgspec import Struct

from snek3.types.base import address, bytesn, hash32, uint64, uint256


class StorageProof(Struct, rename="camel"):
    key: hash32
    value: uint256
    proof: list[bytesn]


class AccountProof(Struct, rename="camel"):
    address: address
    account_proof: list[bytesn]
    balance: uint256
    code_hash: hash32
    nonce: uint64
    storage_hash: hash32
    storage_proof: list[StorageProof]
