from typing import Dict, Optional
import httpx
from snek3.types.block import BlockShort, BlockExpanded
from snek3.types import rpc
from snek3.hooks import dec_hook
from msgspec.json import Decoder, Encoder
from msgspec import Struct, Raw
from typer import Typer
from devtools import debug
from snek3.rpc.base import Snek3

RPC_URL = "http://127.0.0.1:8545"

app = Typer()
snek = Snek3()


@app.command()
def get_block(identifier: str = "latest", transactions: bool = False):
    result = snek.get_block(identifier, transactions)
    debug(result)


if __name__ == "__main__":
    app()
