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

    def get_binary(self):
        bin_str = ""
        for byte in self._bytes:
            bin_str += "{:08b}".format(byte)

        return bin_str

    def get_hex(self):
        hex_str = ""
        for byte in self._bytes:
            hex_str += "{:02x}".format(byte)

        return hex_str

    def get_b64(self):
        b64 = base64.b64encode(self._bytes)
        b64_str = b64.decode(UTF8)

        return b64_str
