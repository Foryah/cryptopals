import base64
import binascii


class Solver(object):

    def load_str(self, input_str):
        self._bytes = bytearray(input_str, "utf-8")

    def load_hex(self, hex_str):
        input_bytes = binascii.unhexlify(hex_str)

        self._bytes = bytearray(input_bytes)

    def load_b64(self, b64_str):
        input_bytes = base64.b64decode(b64_str)

        self._bytes = bytearray(input_bytes)

    def get_str(self):
        _str = self._bytes.decode("utf-8")

        return _str

    def get_hex(self):
        hex_str = ""
        for byte in self._bytes:
            _hex = hex(byte)
            hex_str += _hex[2:]

        return hex_str

    def get_b64(self):
        b64 = base64.b64encode(self._bytes)
        b64_str = b64.decode("utf-8")

        return b64_str
