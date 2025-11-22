using FluentAssertions;
using Xunit;

namespace Cryptopals.Tests;

public class Set1Challenge6Test
{
    [Fact]
    public void Should_CalculateHammingDistance()
    {
        Solver.CalculateHammingDistance("this is a test", "wokka wokka!!!")
            .Should()
            .Be(37);
    }

    [Fact]
    public void Should_DecryptRepeatedKeyXoredFile()
    {
        var bestDecryptedMessage = Solver.DecryptRepeatedKeyXoredFile("/Users/david/Projects/fun/cryptopals/data/ch6_file");
        bestDecryptedMessage.DecryptedMessage.Should().StartWith("I'm back and I'm ringin' the bell");
        bestDecryptedMessage.Key.Should().Be("Terminator X: Bring the noise");
    }
}
