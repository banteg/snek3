from __future__ import annotations

from typing import List, Literal, Optional

from msgspec import Struct

from eth_api_spec.types import address, bytes32, hash32, uint

FilterResults = List[hash32] | List[Log]


class Filter(Struct, rename="camel"):
    from_block: Optional[uint]
    to_block: Optional[uint]
    address = address | List[address]
    topics: Optional[FilterTopics]


FilterTopic = Literal[None] | bytes32 | List[bytes32]

FilterTopics = List[FilterTopic]
