# -*- coding: utf-8 -*-
import abc
import re


CHAR_ON_SCREEN = 10
ENCODING = "utf-8"

# The interface between the modules should be... bytes !?
# The BitString class should have a is_consistent boolean value that gets set to false
# whenever a write operation happens on one of the modules and when we do a read we check
# the consistency and if it's not consistent then we run the sync method


class ExBitString(object):

    # ########################### PRINT ############################### #
    def print_all(self):
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

    def print_as_bin(self):
        bin_arr_with_no_headers = map(lambda bin_str: bin_str[BIN_HEADER_SIZE:], self.bit_string)
        print(" ".join(bin_arr_with_no_headers))

    def print_as_hex(self):
        hex_arr_with_no_headers = map(lambda hex_str: hex_str[HEX_HEADER_SIZE:], self.hex_string)
        print(" ".join(hex_arr_with_no_headers))

    # ########################### GETs ############################### #
    def get_str(self):
        return "".join(self.unicode_string)

    def get_byte(self):
        return self.byte_string

    def get_hex(self):
        return self.hex_string

    def get_bin_arr(self):
        return self.bit_string

    def get_bin_str(self):
        bin_arr_with_no_headers = map(lambda bin_str: bin_str[BIN_HEADER_SIZE:], self.bit_string)

        return "".join(bin_arr_with_no_headers)

    # ########################### SETs ############################### #
    def set_str(self, string):
        if type(string) != str:
            raise ValueError("Unable to set str for : {} {}"
                             .format(type(string), string))

        self._process_string(string)

    def set_byte_arr(self, byte_arr):
        if type(byte_arr) != bytearray:
            raise ValueError("Unable to set byte arr for : {} {}"
                             .format(type(byte_arr), byte_arr))

        self.byte_string = byte_arr
        self._sync_with_byte_string()

    def set_hex_arr(self, hex_arr):
        if type(hex_arr) != list:
            raise ValueError("Unable to set hex arr for : {} {}"
                             .format(type(hex_arr), hex_arr))

        byte_arr = self._hex_to_byte(hex_arr)

        self.byte_string = byte_arr
        self._sync_with_byte_string()

    def set_bin_arr(self, binary):
        if type(binary) != list:
            raise ValueError("Unable to set bin arr for : {} {}"
                             .format(type(binary), binary))

        byte_arr = self._bin_to_byte(binary)

        self.byte_string = byte_arr
        self._sync_with_byte_string()

    def set_hex_str(self, hex_str):
        if type(hex_str) != str:
            raise ValueError("Unable to set hex str for : {} {}"
                             .format(type(hex_str), hex_str))

        # Convert the string to a hex array
        hex_arr = []
        for i in range(0, len(hex_str), 2):
            hex_arr.append("0x" + str(hex_str[i:i + 2]))

        self.set_hex_arr(hex_arr)

    # ########################### HELPER FUNCTIONS ############################### #
    def _process_string(self, input_string):
        self.byte_string = bytearray(input_string, ENCODING)

        self._sync_with_byte_string()

    def _sync_with_byte_string(self):
        self.hex_string = []
        self.bit_string = []
        self.unicode_string = []

        for char_as_int in self.byte_string:
            char_as_bin = bin(char_as_int)
            char_as_padded_bin = self.__format_binary_byte(char_as_bin)
            self.bit_string.append(char_as_padded_bin)

            char_as_hex = hex(char_as_int)
            char_as_padded_hex = self.__format_hex_byte(char_as_hex)
            self.hex_string.append(char_as_padded_hex)

            self.unicode_string.append(chr(char_as_int))

    def _hex_to_byte(self, hex_arr):
        byte_arr = []
        for binary in hex_arr:
            byte = int(binary, HEX_BASE)
            byte_arr.append(byte)

        return bytearray(byte_arr)

    def _bin_to_byte(self, bin_arr):
        byte_arr = []
        for binary in bin_arr:
            byte = int(binary, BINARY_BASE)
            byte_arr.append(byte)

        return bytearray(byte_arr)

    def __format_hex_byte(self, hex_string):
        clean_hex_string = hex_string[HEX_HEADER_SIZE:]
        clean_hex_string = clean_hex_string.zfill(HEX_BYTE_SIZE)

        return "{}{}".format(HEX_HEADER, clean_hex_string)

    def __format_binary_byte(self, bin_string):
        clean_bin_string = bin_string[BIN_HEADER_SIZE:]
        clean_bin_string = clean_bin_string.zfill(BIN_BYTE_SIZE)
        return "{}{}".format(BIN_HEADER, clean_bin_string)


DIRTY = "dirty"
CLEAN = "clean"


class ModulePrototype(metaclass=abc.ABCMeta):
    """ A module is a class that knows how to handle a certain representation
        of a dataset.

        The function always receives a bytes object and 'loads' it to an
        internal representation.

        Once the class is initialized and the internal representaiton is in place,
        we allow the user to access this representation the same way you do with
        an array ( using brackets ).

        Other than the bracket notation that can be used on this class, the class also
        knows how to 'dump' the internal representation as an bytes object.

        The class shoud have a state variable which returns:
             -> dirty if the object has been written to
             -> clean if the object has not been written to
    """

    @abc.abstractmethod
    def load(self):
        """ Checks and imports the bytes object and converts it to internal representation """
        pass

    @abc.abstractmethod
    def dump(self):
        """ Exports the internal representation as a bytes object """
        pass

    @abc.abstractmethod
    def __str__(self):
        """ Returns the string version of the internal representation"""
        pass

    @abc.abstractmethod
    def __getitem__(self, arg):
        """ Allows us to get class data as an array using brackets """
        pass

    @abc.abstractmethod
    def __setitem__(self, arg):
        """ Allows us to set class data as an array using brackets """
        pass


class HexModule(ModulePrototype):
    HEX_HEADER = "0x"
    HEX_HEADER_SIZE = len(HEX_HEADER)
    HEX_BYTE_SIZE = 2
    HEX_BASE = 16

    def __init__(self):
        self.hex_arr = []
        self.state = CLEAN

    def __str__(self):
        # We want to display the hex the right way, not Little Endian way
        # hence we print a reverse slice
        return "".join(self.hex_arr[::-1])

    def __getitem__(self, arg):
        return self.hex_arr[arg]

    def __setitem__(self, arg, value):
        value_str = str(value)

        if re.match("[0-9a-fA-F]", value_str):
            self.hex_arr[arg] = value_str
        else:
            raise ValueError("Wrong value {}. A hex str can only contain [0-1a-fA-F]"
                             .format(value_str))

    def load(self, bytes_arr):
        for byte in bytes_arr:
            hex_str = hex(byte)

            hex_str_no_header = hex_str[HexModule.HEX_HEADER_SIZE:]
            hex_str_no_header_filled = hex_str_no_header.zfill(HexModule.HEX_BYTE_SIZE)
            hex_arr = list(hex_str_no_header_filled)

            self.hex_arr.extend(hex_arr)

        # We we'll use Little Endian so we must reverse the array
        self.hex_arr = self.hex_arr[::-1]
        self.state = CLEAN

    def dump(self):
        bytes_arr = []
        # We need to use the reversed array to get the right chars
        reversed_hex_arr = self.hex_arr[::-1]

        nr_of_bits = len(reversed_hex_arr)
        for i in range(HexModule.HEX_BYTE_SIZE, nr_of_bits + 1, HexModule.HEX_BYTE_SIZE):
            hex_str = "".join(reversed_hex_arr[i - HexModule.HEX_BYTE_SIZE:i])
            hex_val = int(hex_str, HexModule.HEX_BASE)

            bytes_arr.append(hex_val)

        self.state = CLEAN
        return bytes(bytes_arr, 'utf-8')


class BinaryModule(ModulePrototype):
    BIN_HEADER = "0b"
    BIN_HEADER_SIZE = len(BIN_HEADER)
    BIN_BYTE_SIZE = 8
    BINARY_BASE = 2

    def __init__(self):
        self.bin_arr = []
        self.state = DIRTY

    def __str__(self):
        # We want to display the bin the right way, not Little Endian way
        # hence we print a reverse slice
        return "".join(self.bin_arr[::-1])

    def __getitem__(self, arg):
        return self.bin_arr[arg]

    def __setitem__(self, arg, value):
        if value in [0, 1, "0", "1"]:
            self.bin_arr[arg] = str(value)
            self.state = DIRTY
        else:
            raise ValueError("Wrong value {}. A binary string can only have 1's and 0's !"
                             .format(value))

    def load(self, bytes_arr):
        for byte in bytes_arr:
            bin_str = bin(byte)

            bin_str_no_header = bin_str[BinaryModule.BIN_HEADER_SIZE:]
            bin_str_no_header_filled = bin_str_no_header.zfill(BinaryModule.BIN_BYTE_SIZE)
            bin_arr = list(bin_str_no_header_filled)

            self.bin_arr.extend(bin_arr)

        # We we'll use Little Endian so we must reverse the array
        self.bin_arr = self.bin_arr[::-1]
        self.state = CLEAN

    def dump(self):
        bytes_arr = []
        # We need to use the reversed array to get the right chars
        reversed_bin_arr = self.bin_arr[::-1]

        nr_of_bits = len(reversed_bin_arr)
        for i in range(BinaryModule.BIN_BYTE_SIZE, nr_of_bits + 1, BinaryModule.BIN_BYTE_SIZE):
            bin_str = "".join(reversed_bin_arr[i - BinaryModule.BIN_BYTE_SIZE:i])
            bin_val = int(bin_str, BinaryModule.BINARY_BASE)

            bytes_arr.append(bin_val)

        self.state = CLEAN
        return bytes(bytes_arr, 'utf-8')


class ByteModule(ModulePrototype):
    BYTE_SIZE = 8

    def __init__(self):
        self.byte_arr = []
        self.state = DIRTY

    def __str__(self):
        return " ".join(self.byte_arr)

    def __getitem__(self, arg):
        return self.byte_arr[arg]

    def __setitem__(self, arg, value):
        if int(value) in range(0, 255):
            self.byte_arr[arg] = str(value)
            self.state = DIRTY
        else:
            raise ValueError("Wrong value {}. A byte can only have values between 0 and 255"
                             .format(value))

    def load(self, bytes_arr):
        bytes_str_arr = map(lambda int_val: str(int_val), bytes_arr)
        self.byte_arr = bytes_str_arr
        self.state = CLEAN

    def dump(self):
        self.state = CLEAN
        return self.byte_arr


class BitString(object):

    def __init__(self):
        self.byte = ByteModule()
        self.bin = BinaryModule()
        self.hex = HexModule()
        self.modules = [self.byte, self.bin, self.hex]

    def load(self, string):
        bytes_arr = bytes(string, 'utf-8')

        for module in self.modules:
            module.load(bytes_arr)
