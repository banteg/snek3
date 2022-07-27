from abc import abstractmethod, ABCMeta
from typing import List, Tuple


class IdentityDecoder:
    def decode(self, data: bytearray):
        return data


class Method(metaclass=ABCMeta):

    decoder = IdentityDecoder()

    def __init__(self, *args, **kwargs):
        self.method, self.params = self.encode_payload(*args, **kwargs)

    @abstractmethod
    def encode_payload(self, *args, **kwargs) -> Tuple[str, List]:
        pass

    def decode_response(self, data: bytearray):
        return self.decoder.decode(data)
