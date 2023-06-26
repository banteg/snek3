from abc import abstractmethod, ABCMeta
from typing import List, Tuple
from msgspec.json import Decoder
from snek3.hooks import dec_hook
from typing import Any


class IdentityDecoder:
    def decode(self, data: bytearray):
        return data


class Method(metaclass=ABCMeta):
    response_type: Any = None

    def __init__(self, *args, **kwargs):
        self.method, self.params = self.encode_payload(*args, **kwargs)

    @abstractmethod
    def encode_payload(self, *args, **kwargs) -> Tuple[str, List]:
        return "method", ["params"]

    def decode_response(self, data: bytearray):
        decoder = Decoder(self.response_type, dec_hook=dec_hook)
        return decoder.decode(data)
