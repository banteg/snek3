from __future__ import annotations

from typing import List

from msgspec import Struct

from snek3.types.base import address, hash32, uint64, uint256


class AccountProof(Struct, rename="camel"):
    address: address
    account_proof: List[bytes]
    balance: uint256
    code_hash: hash32
    nonce: uint64
    storage_hash: hash32
    storage_proof: list[StorageProof]


class StorageProof(Struct, rename="camel"):
    key: hash32
    value: uint256
    proof: List[bytes]
