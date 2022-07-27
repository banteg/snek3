from typing import List, Tuple


class IdentityDecoder:
    def decode(self, data: bytearray):
        return data


class Method:
    decoder = IdentityDecoder()

    def __init__(self, method, params):
        self.method, self.params = self.encode_payload(method, params)

    def encode_payload(self, *args, **kwargs) -> Tuple[str, List]:
        return self.method, self.params

    def decode_response(self, data: bytearray):
        return self.decoder.decode(data)
