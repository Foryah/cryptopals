import base64
from bit_string import BitString

# TODO: Let BitString be a 'library'-like object :
#           -> No string version of hex/bin/byte

#       Only arrays and array consistency, and everything else should
#       be taken care of on this level. This object should transofrm
#       the arrays into connected strings of the arrays and keep them
#       consistent.
#
#       Maybe a good idea would be to call BitString - BitArray and
#       this class BitString, which keeps string representation of the
#       arrays. Then we'll have another BitWorker class that works with
#       BitString and does operations.


class BitWorker(object):

    def __init__(self):
        self.bit_string = BitString()

    def load_hex(self, hex_str):
        self.bit_string.set_hex_str(hex_str)

    def load_b64(self, base64_str):
        pass

    def get_bin(self):
        return self.bit_string.get_bin_str()

    def get_str(self):
        return self.bit_string.get_str()

    def get_b64(self):
        byte_arr = self.bit_string.get_byte()
        b64_bin_str = base64.b64encode(byte_arr)
        return b64_bin_str.decode("utf-8")

    def heXor(self, bit_worker_obj):
        first_bin_str = self.get_bin()
        second_bin_str = bit_worker_obj.get_bin()

        if len(first_bin_str) != len(second_bin_str):
            raise ValueError("The two strings are not equal. heXor abort !")

        int_val_of_first_bin_str = int(first_bin_str, 2)
        int_val_of_second_bin_str = int(second_bin_str, 2)

        xored_val = int_val_of_first_bin_str ^ int_val_of_second_bin_str
        bin_xored_str = hex(xored_val)

        return bin_xored_str[2:-1]


a = BitWorker()
b = BitWorker()
a.load_hex("1c0111001f010100061a024b53535009181c")
b.load_hex("686974207468652062756c6c277320657965")
print(a.heXor(b))
