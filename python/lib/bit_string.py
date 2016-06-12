# -*- coding: utf-8 -*-

BIN_HEADER = "0b"
BIN_HEADER_SIZE = len(BIN_HEADER)
BIN_BYTE_SIZE = 8

HEX_HEADER = "0x"
HEX_HEADER_SIZE = len(HEX_HEADER)
HEX_BYTE_SIZE = 2

BINARY_BASE = 2
HEX_BASE = 16

CHAR_ON_SCREEN = 10
ENCODING = "utf-8"


class BitString(object):

    def __init__(self, input_string):
        self._process_string(input_string)

    # ########################### PRINT ############################### #
    def print(self):
        length = len(self.byte_string)

        for start in range(0, length, CHAR_ON_SCREEN):
            end = start + CHAR_ON_SCREEN
            if end > length:
                end = start + (length - start)

            self._print(start, end)

    def _print(self, start, end):
        print("{:5} : ".format("Char"), end="")
        for index in range(start, end):
            print('{:^9}'.format(chr(self.byte_string[index])), end="")

        print("")
        print("{:5} : ".format("Byte"), end="")
        for index in range(start, end):
            print('{:^9}'.format(self.byte_string[index]), end="")

        print("")
        print("{:5} : ".format("Hex"), end="")
        for index in range(start, end):
            print('{:^9}'.format(self.hex_string[index][HEX_HEADER_SIZE:]), end="")

        print("")
        print("{:5} : ".format("Bin"), end="")
        for index in range(start, end):
            print('{:^8} '.format(self.bit_string[index][BIN_HEADER_SIZE:]), end="")

        print("")
        print("")

    # ########################### GETs ############################### #
    def get_str(self):
        return self.unicode_string

    def get_byte(self):
        return self.byte_string

    def get_hex(self):
        return self.hex_string

    def get_bin(self):
        return self.bit_string

    # ########################### SETs ############################### #
    def set_str(self, string):
        if type(string) != str:
            raise ValueError("Unable to set str for : {} {}"
                             .format(type(string), string))

        self._process_string(string)

    def set_byte(self, byte_arr):
        if type(byte_arr) != list:
            raise ValueError("Unable to set byte for : {} {}"
                             .format(type(byte_arr), byte_arr))

        self.byte_string = byte_arr
        self._sync_with_byte_string()

    def set_hex(self, hex_arr):
        if type(hex_arr) != list:
            raise ValueError("Unable to set hex for : {} {}"
                             .format(type(hex_arr), hex_arr))

        byte_arr = self._hex_to_byte(hex_arr)

        self.byte_string = byte_arr
        self._sync_with_byte_string()

    def set_bin(self, binary):
        if type(binary) != list:
            raise ValueError("Unable to set bin for : {} {}"
                             .format(type(binary), binary))

        byte_arr = self._bin_to_byte(binary)

        self.byte_string = byte_arr
        self._sync_with_byte_string()

    # ########################### HELPER FUNCTIONS ############################### #
    def _process_string(self, input_string):
        self.byte_string = bytes(input_string, ENCODING)

        self._sync_with_byte_string()

    def _sync_with_byte_string(self):
        self.hex_string = []
        self.bit_string = []

        for char_as_int in self.byte_string:
            char_as_bin = bin(char_as_int)
            char_as_padded_bin = self.__format_binary_byte(char_as_bin)
            self.bit_string.append(char_as_padded_bin)

            char_as_hex = hex(char_as_int)
            char_as_padded_hex = self.__format_hex_byte(char_as_hex)
            self.hex_string.append(char_as_padded_hex)

    def _hex_to_byte(self, hex_arr):
        byte_arr = []
        for binary in hex_arr:
            byte = int(binary, HEX_BASE)
            byte_arr.append(byte)

        return byte_arr

    def _bin_to_byte(self, bin_arr):
        byte_arr = []
        for binary in bin_arr:
            byte = int(binary, BINARY_BASE)
            byte_arr.append(byte)

        return byte_arr

    def __format_hex_byte(self, hex_string):
        clean_hex_string = hex_string[HEX_HEADER_SIZE:]
        clean_hex_string = clean_hex_string.zfill(HEX_BYTE_SIZE)

        return "{}{}".format(HEX_HEADER, clean_hex_string)

    def __format_binary_byte(self, bin_string):
        clean_bin_string = bin_string[BIN_HEADER_SIZE:]
        clean_bin_string = clean_bin_string.zfill(BIN_BYTE_SIZE)

        return "{}{}".format(BIN_HEADER, clean_bin_string)
