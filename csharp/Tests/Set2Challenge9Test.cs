using FluentAssertions;
using Xunit;

namespace Cryptopals.Tests;

public class Set2Challenge9Test
{
    [Fact]
    public void Should_PKCS7Pad_with_20bytes()
    {
        var paddedInput = Solver.PKCS7Pad("YELLOW SUBMARINE", 20);
        paddedInput.Should().Be("YELLOW SUBMARINE\x04\x04\x04\x04");
    }

    [Fact]
    public void Should_PKCS7Pad_with_16bytes()
    {
        var paddedInput = Solver.PKCS7Pad("YELLOW SUBMARINE", 16);
        paddedInput.Should().Be("YELLOW SUBMARINE\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10");
    }

    [Fact]
    public void Should_PKCS7Pad_with_17bytes()
    {
        var paddedInput = Solver.PKCS7Pad("YELLOW SUBMARINE", 17);
        paddedInput.Should().Be("YELLOW SUBMARINE\x01");
    }

    [Fact]
    public void Should_PKCS7Pad_with_8bytes()
    {
        var paddedInput = Solver.PKCS7Pad("YELLOW SUBMARINE", 8);
        paddedInput.Should().Be("YELLOW SUBMARINE\x08\x08\x08\x08\x08\x08\x08\x08");
    }
}
