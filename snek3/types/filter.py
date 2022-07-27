from __future__ import annotations

from typing import List, Literal, Optional

from msgspec import Struct

from snek3.types.__init__2 import address, bytes32, hash32, uint, Log

FilterResults = List[hash32] | List[Log]


class Filter(Struct, rename="camel"):
    from_block: Optional[uint]
    to_block: Optional[uint]
    address = address | List[address]
    topics: Optional[FilterTopics]


FilterTopic = Literal[None] | bytes32 | List[bytes32]

FilterTopics = List[FilterTopic]
