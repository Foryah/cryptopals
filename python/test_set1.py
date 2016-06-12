import set1
import unittest


class TestSet1(unittest.TestCase):

    def test_challange1(self):
        bin_str = set1.hex_str2bin_str("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")
        self.assertEqual(bin_str.decode("ascii"), "I'm killing your brain like a poisonous mushroom")

        bin_str = set1.hex_str2b64_str("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")
        self.assertEqual(bin_str.decode("ascii"), "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t")

    def test_challange2(self):
        str1 = "1c0111001f010100061a024b53535009181c"
        str2 = "686974207468652062756c6c277320657965"

        self.assertEqual(set1.heXor(str1, str2), "746865206b696420646f6e277420706c6179")

    def test_challange3(self):
        input_str = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

        self.assertEqual(set1.single_byte_xor_cipher_str(input_str), "Cooking MC's like a pound of bacon")

    def test_challange4(self):
        input_file_name = "../data/xored_data"

        self.assertEqual(set1.single_byte_xor_cipher_file(input_file_name), " ? ")

if __name__ == '__main__':
    unittest.main()
