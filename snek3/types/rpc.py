# https://www.jsonrpc.org/specification

from typing import Any, Literal, Optional

from msgspec import Raw, Struct


class Error(Struct):
    code: int
    message: str
    data: Optional[Any] = None


class Response(Struct):
    result: Raw = None  # type: ignore
    error: Optional[Error] = None
    id: Optional[str | int] = None
    jsonrpc: Literal["2.0"] = "2.0"


class Request(Struct):
    method: str
    params: Optional[Any] = None
    id: Optional[str | int] = None
    jsonrpc: Literal["2.0"] = "2.0"
