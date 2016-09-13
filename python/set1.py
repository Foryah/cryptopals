import base64
import binascii
from lib.solver import Solver


VALUE = "value"
STRING = "string"
KEY = "key"

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

    return rs


def decrypt_single_byte(smart_string, key_int):
    message_bytes = smart_string.get_bytes()
    len_message = len(message_bytes)

    key_bytes = bytearray()
    for i in range(len_message):
        key_bytes.append(key_int)

    key_smart_string = Solver()
    key_smart_string.load_bytes(key_bytes)

    result = heXor(smart_string, key_smart_string)

    return result.get_str()


def get_str_value(input_str):
    total_value = 0
    for index in range(len(input_str)):
        letter = input_str[index].lower()

        if letter in english_letter_values.keys():
            total_value += english_letter_values[letter]

    return total_value


def single_byte_xor_cipher_str(smart_string, best_dict=None):
    if not best_dict:
        best_dict = {"value": 0}

    for key in range(256):
        decrypted_str = decrypt_single_byte(smart_string, key)
        update_best(best_dict, decrypted_str, key)

    return best_dict


def single_byte_xor_cipher_file(file_name):
    best_dict = {"value": 0}

    with open(file_name, "r") as f:
        for line in f.readlines():
            clean_line = line.strip()

            smart_string = Solver()
            smart_string.load_hex(clean_line)

            single_byte_xor_cipher_str(smart_string, best_dict)

    return best_dict


def update_best(best_dict, decrypted_str, key):
    str_value = get_str_value(decrypted_str)

    if str_value > best_dict[VALUE]:
        best_dict[VALUE] = str_value
        best_dict[STRING] = decrypted_str
        best_dict[KEY] = key
