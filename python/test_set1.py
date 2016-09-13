import set1
from lib.solver import Solver
import unittest


class TestSet1(unittest.TestCase):

    def test_challange1(self):
        s = Solver()
        s.load_hex("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")

        bin_str = s.get_str()
        self.assertEqual(bin_str, "I'm killing your brain like a poisonous mushroom")

        b64_str = s.get_b64()
        self.assertEqual(b64_str, "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t")

    def test_challange2(self):
        s1 = Solver()
        str1 = "1c0111001f010100061a024b53535009181c"
        s1.load_hex(str1)

        s2 = Solver()
        str2 = "686974207468652062756c6c277320657965"
        s2.load_hex(str2)

        result = set1.heXor(s1, s2)
        hex_str = result.get_hex()
        self.assertEqual(hex_str, "746865206b696420646f6e277420706c6179")

    def test_challange3(self):
        s = Solver()
        input_str = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
        s.load_hex(input_str)

        result_dict = set1.single_byte_xor_cipher_str(s)
        result_str = result_dict["string"]
        self.assertEqual(result_str, "Cooking MC's like a pound of bacon")

    def test_challange4(self):
        input_file_name = "../data/xored_data"

        result_dict = set1.single_byte_xor_cipher_file(input_file_name)
        result_str = result_dict["string"]

        self.assertEqual(result_str, "Now that the party is jumping\n")

if __name__ == '__main__':
    unittest.main()
