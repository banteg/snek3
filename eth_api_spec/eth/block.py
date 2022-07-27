from hexbytes import HexBytes
from eth_utils import encode_hex
import re


def get_block(identifier: int | str | bytes, with_transactions: bool = False):
    method = "eth_getBlockByHash"

    match identifier:
        # block number as int
        case int():
            method = "eth_getBlockByNumber"
            params = [hex(identifier), with_transactions]
        # block tag
        case "pending" | "latest" | "finalized" | "safe" | "earliest":
            params = [identifier, with_transactions]
        # block hash as str
        case str() as i if re.match(r"0x[0-9a-f]{64}", i):
            params = [identifier, with_transactions]
        # block number as hex
        case str() as i if re.match(r"0x[0-9a-f]+", i):
            method = "eth_getBlockByNumber"
            params = [identifier, with_transactions]
        # block hash as bytes
        case bytes() | HexBytes() as i if len(i) == 32:
            params = [encode_hex(identifier), with_transactions]
        # unknown pattern
        case _:
            raise ValueError(f"unrecognized block identifier: {identifier!r}")

    return method, params
