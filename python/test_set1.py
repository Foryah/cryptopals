import set1
import unittest


class TestSet1(unittest.TestCase):

    def test_challange1(self):
        bin_str = set1.hex2bin_str("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")
        self.assertEqual(bin_str.decode("ascii"), "I'm killing your brain like a poisonous mushroom")

        bin_str = set1.hex2b64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")
        self.assertEqual(bin_str.decode("ascii"), "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t")

if __name__ == '__main__':
    unittest.main()
