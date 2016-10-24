import set1
from lib.solver import Solver
import unittest


class TestSet1(unittest.TestCase):

    def _test_challange1(self):
        s = Solver()
        s.load_hex("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")

        bin_str = s.get_str()
        self.assertEqual(bin_str, "I'm killing your brain like a poisonous mushroom")

        b64_str = s.get_b64()
        self.assertEqual(b64_str, "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t")

    def _test_challange2(self):
        s1 = Solver()
        str1 = "1c0111001f010100061a024b53535009181c"
        s1.load_hex(str1)

        s2 = Solver()
        str2 = "686974207468652062756c6c277320657965"
        s2.load_hex(str2)

        result = set1.heXor(s1, s2)
        hex_str = result.get_hex()
        self.assertEqual(hex_str, "746865206b696420646f6e277420706c6179")

    def _test_challange3(self):
        s = Solver()
        input_str = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
        s.load_hex(input_str)

        result_dict = set1.single_byte_xor_cipher_str(s)
        result_str = result_dict["string"]
        self.assertEqual(result_str, "Cooking MC's like a pound of bacon")

    def _test_challange4(self):
        input_file_name = "../data/xored_data"

        result_dict = set1.single_byte_xor_cipher_file(input_file_name)
        result_str = result_dict["string"]

        self.assertEqual(result_str, "Now that the party is jumping\n")

    def _test_challange5(self):
        smart_input = Solver()
        input_str = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
        smart_input.load_str(input_str)

        key = "ICE"
        result = set1.repeating_key_xor_cipher_str(smart_input, key)
        result_str = result.get_hex()

        self.assertEqual(result_str, "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f")

    def _test_hamming(self):
        smart_1 = Solver()
        str1 = "this is a test"
        smart_1.load_str(str1)

        smart_2 = Solver()
        str2 = "wokka wokka!!!"
        smart_2.load_str(str2)

        distance = set1.hamming_distance(smart_1, smart_2)
        self.assertEqual(distance, 37)

    def test_break_known_key_length(self):
        smart_input = Solver()
        input_str = "SPEAKSOFTLYANDCARRYABIGSTICKYOUWILLGOFAR"
        smart_input.load_str(input_str)

        key = "SECRET"
        key_length = len(key)

        encripted_b64_str = "ABUGEw4HHAMXHhwVHQEAExcGCgQBGwIHBwwAGRwbBhIKHgkTHAMCAA=="

        encripted_smart_str = set1.repeating_key_xor_cipher_str(smart_input, key)
        encripted_result = encripted_smart_str.get_b64()

        self.assertEqual(encripted_result, encripted_b64_str)

        recovered_key = set1.recover_key_based_on_length(encripted_smart_str, key_length)

        self.assertEqual(recovered_key, key)


if __name__ == '__main__':
    unittest.main()
