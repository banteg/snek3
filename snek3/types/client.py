from typing import Literal

from msgspec import Struct

from snek3.types.base import uint


class SyncingProgress(Struct, rename="camel"):
    starting_block: uint
    current_block: uint
    highest_block: uint


SyncingStatus = SyncingProgress | Literal[False]
