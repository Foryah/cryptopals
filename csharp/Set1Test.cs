// This file was auto-generated based on version 1.4.0 of the canonical data.

using Xunit;
using Set1;

public class Set1Test
{
    [Fact]
    public void Hex_to_string()
    {
        Assert.Equal(
            "I'm killing your brain like a poisonous mushroom",
            Solver.HexToAscii(
                "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
            )
        );
    }

    [Fact]
    public void Hex_to_base_64()
    {
        Assert.Equal(
            "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t",
            Solver.HexToBase64(
                "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
            )
        );
    }

    [Fact]
    public void Xor_two_hex_strings()
    {
        Assert.Equal(
            "746865206B696420646F6E277420706C6179",
            Solver.XorEqualHexes( "1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965")
        );
    }
}