import base64
import binascii


def hex2hex_str(hex_val):
    return str(hex_val[2:])


def hex_str2hex(hex_str):
    return int(hex_str, 16)


def bin_str2hex_str(bin_str):
    return binascii.hexlify(bin_str)


def hex_str2bin_str(hex_str):
    return binascii.unhexlify(hex_str)


def hex_str2b64_str(hex_str):
    bin_str = hex_str2bin_str(hex_str)
    return base64.b64encode(bin_str)


def heXor(hex_str1, hex_str2):
    if len(hex_str1) != len(hex_str2):
        raise ValueError("The two strings have different length")

    hex_val1 = hex_str2hex(hex_str1)
    hex_val2 = hex_str2hex(hex_str2)

    hex_result = hex(hex_val1 ^ hex_val2)
    hex_str_result = hex2hex_str(hex_result)

    return hex_str_result
