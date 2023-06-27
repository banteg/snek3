import pytest
from hexbytes import HexBytes

from snek3.utils import encode_block_id

block_number = 15_000_000
block_hash = "0x9a71a95be3fe957457b11817587e5af4c7e24836d5b383c430ff25b9286a457f"
block_cases = {
    block_number: ("eth_getBlockByNumber", [hex(block_number), False]),
    hex(block_number): ("eth_getBlockByNumber", [hex(block_number), False]),
    "latest": ("eth_getBlockByHash", ["latest", False]),
    block_hash: ("eth_getBlockByHash", [block_hash, False]),
    bytes.fromhex(block_hash[2:]): ("eth_getBlockByHash", [block_hash, False]),
    HexBytes(block_hash): ("eth_getBlockByHash", [block_hash, False]),
}


@pytest.mark.parametrize("identifier", block_cases)
def test_encode_get_block_payload(identifier):
    assert encode_block_id(identifier) == block_cases[identifier][1][0]


@pytest.mark.parametrize("identifier", ["bunny", -1])
def test_encode_get_block_payload_fail(identifier):
    with pytest.raises(ValueError):
        encode_block_id(identifier)
