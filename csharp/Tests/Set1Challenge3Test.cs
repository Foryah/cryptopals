using Cryptopals.Models;
using FluentAssertions;
using Xunit;

namespace Cryptopals.Tests;

public class Set1Challenge3Test
{
    [Fact]
    public void Should_DecryptWithSingleCharKey()
    {
        var result = new DecryptedMessageWithSingleCharKey("Cooking MC's like a pound of bacon", "X");
        var solverResult = Solver.DecryptWithSingleCharKey("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736");

        solverResult.DecryptedMessage.Should().Be(result.DecryptedMessage);
        solverResult.Key.Should().Be(result.Key);
    }
}
