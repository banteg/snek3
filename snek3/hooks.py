from typing import Type, Any
from snek3.types.base import uint, bytes256, address, hash32, bytes8, bytes32, bytesn
from snek3.utils import to_checksum_address


def dec_hook(type: Type, obj: Any) -> Any:
    if type is uint:
        return uint(obj, 16)
    if type in (bytesn, bytes256, hash32, bytes8, bytes32):
        return type.fromhex(obj[2:])
    if type is address:
        return to_checksum_address(obj)
