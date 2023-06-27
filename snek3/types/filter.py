from typing import List

from msgspec import Struct

from snek3.types.base import address, bytes32, uint
from snek3.types.receipt import Log

FilterResults = List[Log]

FilterTopics = List[bytes32 | List[bytes32] | None]


class Filter(Struct, rename="camel"):
    from_block: uint | None
    to_block: uint | None
    address: address | list[address]  # invalid in msgspec
    topics: FilterTopics | None
