# https://www.jsonrpc.org/specification

from typing import Any, Literal

from msgspec import Raw, Struct


class Error(Struct):
    code: int
    message: str
    data: Any = None


class Response(Struct):
    result: Raw = None  # type: ignore
    error: Error | None = None
    id: str | int | None = None
    jsonrpc: Literal["2.0"] = "2.0"


class Request(Struct):
    method: str
    params: Any = None
    id: str | int | None = None
    jsonrpc: Literal["2.0"] = "2.0"


BatchRequest = list[Request]
