from eth_hash.backends.pysha3 import keccak256
from snek3.types.base import address


def to_checksum_address(addr) -> address:
    hash_hex = keccak256(addr[2:].encode()).hex()
    mask = [int(x, 16) > 7 for x in hash_hex[:40]]
    return address("0x" + "".join([x.upper() if m else x for x, m in zip(addr[2:], mask)]))
