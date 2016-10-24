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


def repeating_key_xor_cipher_str(smart_string, key):
    string_bytes = smart_string.get_bytes()
    len_str_bytes = len(string_bytes)

    key_bytes = padded_key_bytes(key, len_str_bytes)

    smart_key = Solver()
    smart_key.load_bytes(key_bytes)

    result = heXor(smart_string, smart_key)
    return result


def padded_key_bytes(key, len_str):
    key_len = len(key)
    key_bytes = bytearray(key, "utf-8")

    new_key = bytearray()
    for i in range(len_str):
        key_index = i % key_len
        new_key.append(key_bytes[key_index])

    return new_key


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


def hamming_distance(smart1, smart2):
    first_bin = smart1.get_binary()
    second_bin = smart2.get_binary()

    diff_bits = 0
    for bit_str_1, bit_str_2 in zip(first_bin, second_bin):
        if bit_str_1 != bit_str_2:
            diff_bits += 1

    return diff_bits


def recover_key_based_on_length(encripted_smart, key_length):
    # 1. Get the modulo letters
    encripted_str = encripted_smart.get_str()
    letters = []
    for i in range(key_length):
        sub_string = encripted_str[i::key_length]
        letters.append(sub_string)

    # 2. Try to decript using the best decryption
    decrypted_keys = []
    for letter_substring in letters:
        smart_str = Solver()
        smart_str.load_str(letter_substring)

        best_dict = single_byte_xor_cipher_str(smart_str)
        print(best_dict)
        key = best_dict['key']

        decrypted_keys.append(key)

    # 3. Construct the key
    final_key = ""
    for key in decrypted_keys:
        final_key += chr(key)

    # 4. Retrun the key
    return final_key

initial_str = "This string is to short to be good"
initial_smart = Solver()
initial_smart.load_str(initial_str)

key = "Boy"

encrypted_smart = repeating_key_xor_cipher_str(initial_smart, key)

recovered_key = recover_key_based_on_length(encrypted_smart, len(key))
print(recovered_key)
