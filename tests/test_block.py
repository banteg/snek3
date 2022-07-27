import pytest
from hexbytes import HexBytes

from eth_api_spec.eth.block import get_block

block_hash = "0x6b5cfb96ddfe26113edf9e75076c5527f70cae6ad6164493e96e1e5c79ba42ba"
block_cases = {
    15_000_000: ("eth_getBlockByNumber", [hex(15_000_000), False]),
    hex(15_000_000): ("eth_getBlockByNumber", [hex(15_000_000), False]),
    "pending": ("eth_getBlockByHash", ["pending", False]),
    block_hash: ("eth_getBlockByHash", [block_hash, False]),
    bytes.fromhex(block_hash[2:]): ("eth_getBlockByHash", [block_hash, False]),
    HexBytes(block_hash): ("eth_getBlockByHash", [block_hash, False]),
}


@pytest.mark.parametrize("identifier", block_cases)
def test_encode_get_block_payload(identifier):
    assert get_block(identifier) == block_cases[identifier]


def test_encode_get_block_payload_fail():
    with pytest.raises(ValueError):
        get_block("bunny")
