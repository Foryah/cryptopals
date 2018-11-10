// This file was auto-generated based on version 1.4.0 of the canonical data.

using Xunit;

public class Set1Test
{
    [Fact]
    public void Hex_to_string()
    {
        Assert.Equal(
            "I'm killing your brain like a poisonous mushroom",
            Set1.HexToString(
                "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
            )
        );
    }

    [Fact]
    public void Hex_to_base_64()
    {
        Assert.Equal(
            "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t",
            Set1.HexToBase64(
                "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
            )
        );
    }
}