using FluentAssertions;
using Xunit;

namespace Cryptopals.Tests;

public class Set1Challenge7Test
{
    [Fact]
    public void Should_DecryptAES128InECBMode()
    {
        var decryptedText = Solver.DecryptAES128InECBMode("/Users/david/Projects/fun/cryptopals/data/ch7_file", "YELLOW SUBMARINE");

        decryptedText.Should().StartWith("I'm back and I'm ringin' the bell");
    }
}
