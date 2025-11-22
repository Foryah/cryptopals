using FluentAssertions;
using Xunit;

namespace Cryptopals.Tests;

public class Set1Challenge2Test
{
    [Fact]
    public void Xor_two_hex_strings()
    {
        Solver.XorEqualHexes("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965")
            .Should()
            .Be("746865206B696420646F6E277420706C6179");
    }
}
