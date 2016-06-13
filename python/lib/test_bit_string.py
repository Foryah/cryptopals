from bit_string import BitString
import unittest


class TestBitString(unittest.TestCase):

    def test_initialization(self):
        bit_str = BitString("Test")

        byte_arr = bit_str.get_byte()
        self.assertEqual(byte_arr, bytes([84, 101, 115, 116]))

        hex_arr = bit_str.get_hex()
        self.assertEqual(hex_arr, ['0x54', '0x65', '0x73', '0x74'])

        bin_arr = bit_str.get_bin()
        self.assertEqual(bin_arr, ['0b01010100', '0b01100101', '0b01110011', '0b01110100'])

    def test_set_byte(self):
        bit_str = BitString("Test")

        byte_arr = bit_str.get_byte()
        self.assertEqual(byte_arr, bytearray([84, 101, 115, 116]))

        byte_arr[0] = 85
        byte_arr[1] = 86
        byte_arr[2] = 87
        byte_arr[3] = 88
        bit_str.set_byte(byte_arr)

        byte_arr = bit_str.get_byte()
        self.assertEqual(byte_arr, bytearray([85, 86, 87, 88]))

        hex_arr = bit_str.get_hex()
        self.assertEqual(hex_arr, ['0x55', '0x56', '0x57', '0x58'])

        bin_arr = bit_str.get_bin()
        self.assertEqual(bin_arr, ['0b01010101', '0b01010110', '0b01010111', '0b01011000'])

    def test_set_hex(self):
        bit_str = BitString("Test")

        hex_arr = bit_str.get_hex()
        self.assertEqual(hex_arr, ['0x54', '0x65', '0x73', '0x74'])

        hex_arr[0] = '0x55'
        hex_arr[1] = '0x56'
        hex_arr[2] = '0x57'
        hex_arr[3] = '0x58'
        bit_str.set_hex(hex_arr)

        hex_arr = bit_str.get_hex()
        self.assertEqual(hex_arr, ['0x55', '0x56', '0x57', '0x58'])

        byte_arr = bit_str.get_byte()
        self.assertEqual(byte_arr, bytearray([85, 86, 87, 88]))

        bin_arr = bit_str.get_bin()
        self.assertEqual(bin_arr, ['0b01010101', '0b01010110', '0b01010111', '0b01011000'])

    def test_set_bin(self):
        bit_str = BitString("Test")

        bin_arr = bit_str.get_bin()
        self.assertEqual(bin_arr, ['0b01010100', '0b01100101', '0b01110011', '0b01110100'])

        bin_arr[0] = '0b01010101'
        bin_arr[1] = '0b01010110'
        bin_arr[2] = '0b01010111'
        bin_arr[3] = '0b01011000'
        bit_str.set_bin(bin_arr)

        bin_arr = bit_str.get_bin()
        self.assertEqual(bin_arr, ['0b01010101', '0b01010110', '0b01010111', '0b01011000'])

        hex_arr = bit_str.get_hex()
        self.assertEqual(hex_arr, ['0x55', '0x56', '0x57', '0x58'])

        byte_arr = bit_str.get_byte()
        self.assertEqual(byte_arr, bytearray([85, 86, 87, 88]))

if __name__ == '__main__':
    unittest.main()
