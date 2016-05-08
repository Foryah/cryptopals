import base64
import binascii


def hex2bin_str(hex_str):
    return binascii.unhexlify(hex_str)


def hex2b64(hex_str):
    bin_str = hex2bin_str(hex_str)
    return base64.b64encode(bin_str)
