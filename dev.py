from typing import Dict, Optional
import httpx
from eth_api_spec.types.block import BlockShort, BlockExpanded
from eth_api_spec.types import rpc
from eth_api_spec.hooks import dec_hook
from msgspec.json import Decoder, Encoder
from msgspec import Struct, Raw
from typer import Typer
from devtools import debug
from eth_api_spec.rpc.base import Snek3

RPC_URL = "http://127.0.0.1:8545"

app = Typer()
snek = Snek3()


@app.command()
def get_block(identifier: str = "latest", transactions: bool = False):
    result = snek.get_block(identifier, transactions)
    debug(result)


if __name__ == "__main__":
    app()
