import base64
import binascii
from lib.solver import Solver

english_letter_values = {"e": 13,
                         "t": 9,
                         "a": 8,
                         "o": 8,
                         "n": 7,
                         "i": 7,
                         "r": 7,
                         "s": 6,
                         "h": 6,
                         "l": 4,
                         "d": 4,
                         " ": 4,
                         "c": 3,
                         "u": 3,
                         "p": 3,
                         "f": 3,
                         "m": 2,
                         "w": 2,
                         "y": 2,
                         "b": 1,
                         "g": 1,
                         "v": 1}


def int2hex(int_val):
    b16_str = int("{0:x}".format(int_val), 16)
    return hex(b16_str)


def hex2hex_str(hex_val):
    return str(hex_val[2:])


def hex_str2int(hex_str):
    return int(hex_str, 16)


def bin_str2hex_str(bin_str):
    return binascii.hexlify(bin_str)


def hex_str2bin_str(hex_str):
    return binascii.unhexlify(hex_str)


def hex_str2b64_str(hex_str):
    bin_str = hex_str2bin_str(hex_str)
    return base64.b64encode(bin_str)

# TODO: Maybe this logic should not be here... Maybe another object that
# knows how to talk with the Solver

# TODO: Solver is an awful name... rename it to SmartString ?


def heXor(smart_string_1, smart_string_2):
    bytes_1 = smart_string_1.get_bytes()
    bytes_2 = smart_string_2.get_bytes()

    if len(bytes_1) != len(bytes_2):
        raise ValueError("The two strings have different length")

    result = bytearray()

    for i in range(0, len(bytes_1)):
        result.append(bytes_1[i] ^ bytes_2[i])

    rs = Solver()
    rs.load_bytes(result)

    return rs.get_hex()


def decrypt_single_byte(encrypted_hex_str, key_int):
    hex_key = int2hex(key_int)
    hex_str_key = hex2hex_str(hex_key)

    key_len = len(hex_str_key)
    str_len = len(encrypted_hex_str)
    padded_hex_key = hex_str_key * int(str_len / key_len)

    decrypted_hex_str = heXor(encrypted_hex_str, padded_hex_key)
    try:
        decrypted_str = hex_str2bin_str(decrypted_hex_str).decode('utf-8')
    except (Exception, binascii.Error):
        decrypted_str = ""

    return decrypted_str


def get_str_value(input_str):
    total_value = 0
    for index in range(len(input_str)):
        letter = input_str[index].lower()

        if letter in english_letter_values.keys():
            total_value += english_letter_values[letter]

    return total_value


def single_byte_xor_cipher_str(encrypted_hex_str):
    best_value = 0
    best_str = ""
    best_key = 0

    for key in range(256):
        decrypted_str = decrypt_single_byte(encrypted_hex_str, key)
        str_value = get_str_value(decrypted_str)

        if str_value > best_value:
            best_value = str_value
            best_str = decrypted_str
            best_key = key

    return best_str


def single_byte_xor_cipher_file(file_name):
    # TODO: You need to rewrite all the operations ( xor ) to happen on a bit level
    #       not on the hex level...
    best_value = 0
    best_str = ""

    with open(file_name, "r") as f:
        line = f.readline()
        decrypted_str = single_byte_xor_cipher_str(line)
        str_value = get_str_value(decrypted_str)

        if str_value > best_value:
            best_value = str_value
            best_str = decrypted_str

    return best_str
