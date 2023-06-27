import re

from eth_hash.backends.pysha3 import keccak256
from eth_utils import encode_hex

from snek3.types.base import address


def to_checksum_address(addr) -> address:
    hash_hex = keccak256(addr[2:].encode()).hex()
    mask = [int(x, 16) > 7 for x in hash_hex[:40]]
    return address("0x" + "".join([x.upper() if m else x for x, m in zip(addr[2:], mask)]))


def encode_block_id(value):
    match value:
        case "earliest" | "finalized" | "safe" | "latest" | "pending":
            return value
        case int() as i if i >= 0:
            return hex(value)
        case bytes():
            return encode_hex(value)
        case str() as v if re.match(r"0x[0-9a-f]{1,64}", v):
            return value
        case _:
            raise ValueError("invalid block identifier")
