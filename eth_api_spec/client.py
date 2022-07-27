from typing import Optional

from msgspec import Struct

from eth_api_spec.types import uint


class SyncingProgress(Struct, rename='camel'):
    starting_block: uint
    current_block: uint
    highest_block: uint


SyncingStatus = Optional[SyncingProgress]
