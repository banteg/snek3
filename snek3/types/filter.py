from __future__ import annotations

from typing import List, Optional

from msgspec import Struct

from snek3.types.base import address, bytes32, hash32, uint
from snek3.types.receipt import Log

FilterResults = List[Log]

FilterTopics = List[bytes32 | List[bytes32] | None]


class Filter(Struct, rename="camel"):
    from_block: Optional[uint]
    to_block: Optional[uint]
    address = address | List[address]
    topics: Optional[FilterTopics]
