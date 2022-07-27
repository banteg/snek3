import pytest
from hexbytes import HexBytes

from eth_api_spec.methods.block import GetBlock

block_number = 15_000_000
block_hash = "0x" + "".zfill(64)
block_cases = {
    block_number: ("eth_getBlockByNumber", [hex(block_number), False]),
    hex(block_number): ("eth_getBlockByNumber", [hex(block_number), False]),
    "pending": ("eth_getBlockByHash", ["pending", False]),
    block_hash: ("eth_getBlockByHash", [block_hash, False]),
    bytes.fromhex(block_hash[2:]): ("eth_getBlockByHash", [block_hash, False]),
    HexBytes(block_hash): ("eth_getBlockByHash", [block_hash, False]),
}


@pytest.mark.parametrize("identifier", block_cases)
def test_encode_get_block_payload(identifier):
    handler = GetBlock(identifier)
    assert handler.method, handler.params == block_cases[identifier]


@pytest.mark.parametrize("identifier", ["bunny", -1])
def test_encode_get_block_payload_fail(identifier):
    with pytest.raises(ValueError):
        GetBlock(identifier)
