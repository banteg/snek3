from typing import Type, Any
from hexbytes import HexBytes
from eth_api_spec.types.base import uint, bytes256, address, hash32, bytes8
from eth_utils import to_checksum_address


def dec_hook(type: Type, obj: Any) -> Any:
    if type is uint:
        return uint(obj, 16)
    if type in (HexBytes, bytes256, hash32, bytes8):
        return type(obj)
    if type is address:
        return address(to_checksum_address(obj))
