using FluentAssertions;
using Xunit;

namespace Cryptopals.Tests;

public class Set1Challenge1Test
{
    [Fact]
    public void Hex_to_string()
    {
        Solver
            .HexToAscii("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")
            .Should()
            .Be("I'm killing your brain like a poisonous mushroom");
    }

    [Fact]
    public void Hex_to_base_64()
    {
        Solver
            .HexToBase64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")
            .Should()
            .Be("SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t");
    }
}