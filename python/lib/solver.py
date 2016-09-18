import base64
import binascii


UTF8 = "utf-8"


class Solver(object):

    def load_str(self, input_str):
        self._bytes = bytearray(input_str, UTF8)

    def load_hex(self, hex_str):
        input_bytes = binascii.unhexlify(hex_str)

        self._bytes = bytearray(input_bytes)

    def load_b64(self, b64_str):
        input_bytes = base64.b64decode(b64_str)

        self._bytes = bytearray(input_bytes)

    def load_bytes(self, bytes_input):
        self._bytes = bytearray(bytes_input)

    def get_bytes(self):
        return self._bytes

    def get_str(self):
        _str = self._bytes.decode(UTF8, errors="replace")

        return _str

    def get_hex(self):
        hex_str = ""
        for byte in self._bytes:
            _hex = hex(byte)
            len_hex = len(_hex)

            if len_hex % 2:
                clean_hex = "{}{}".format("0", _hex[2:])
            else:
                clean_hex = "{}".format(_hex[2:])

            hex_str += clean_hex

        return hex_str

    def get_b64(self):
        b64 = base64.b64encode(self._bytes)
        b64_str = b64.decode(UTF8)

        return b64_str
