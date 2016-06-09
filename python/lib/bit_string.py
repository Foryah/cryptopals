from __future__ import print_function

BIN_HEADER = "0b"
BYTE_SIZE = 8
BINARY_BASE = 2
BIN_HEADER_SIZE = len(BIN_HEADER)
CHAR_ON_SCREEN = 10


class BitString(object):

    def __str__(self):
        return self.input_string

    def __init__(self, input_string):
        self.input_string = input_string
        self.byte_string = []
        self.bit_string = []
        self.char_string = []

        self._process_string()

    def all_prints(self):
        length = len(self.byte_string)

        for start in range(0, length, CHAR_ON_SCREEN):
            end = start + CHAR_ON_SCREEN
            if end > length:
                end = start + (length - start)

            self._smart_print(start, end)

    def _smart_print(self, start, end):
        for index in range(start, end):
            print('{:^9}'.format(self.char_string[index]), end="")

        print("")
        for index in range(start, end):
            print('{:^9}'.format(self.byte_string[index]), end="")

        print("")
        for index in range(start, end):
            print('{:^8} '.format(self.bit_string[index]), end="")

        print("")
        print("")

    def get_str(self):
        return self.input_string

    def get_chr(self):
        return self.char_string

    def get_byte(self):
        return self.byte_string

    def get_bin(self):
        return self.bit_string

    def _process_string(self):
        self.char_string = bytes(self.input_string)

        for one_char in self.char_string:
            char_as_int = ord(one_char)
            char_as_bin = bin(char_as_int)
            char_as_padded_bin = self.__format_byte(char_as_bin)
            char_as_int = int(char_as_padded_bin, BINARY_BASE)

            self.byte_string.append(char_as_int)
            self.bit_string.append(char_as_padded_bin[BIN_HEADER_SIZE:])

    def __format_byte(self, bin_string):
        clean_bin_string = bin_string[BIN_HEADER_SIZE:]
        clean_bin_string = clean_bin_string.zfill(BYTE_SIZE)

        return "{}{}".format(BIN_HEADER, clean_bin_string)
