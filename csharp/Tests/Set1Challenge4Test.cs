using Cryptopals.Models;
using FluentAssertions;
using Xunit;

namespace Cryptopals.Tests;

public class Set1Challenge4Test
{
    [Fact]
    public void Should_FindMessageInFile()
    {
        var result = new DecryptedMessageWithSingleCharKey("Now that the party is jumping\n", "5");
        var solverResult = Solver.FindMessageInFile("/Users/david/Projects/fun/cryptopals/data/xored_data");

        solverResult.DecryptedMessage.Should().Be(result.DecryptedMessage);
        solverResult.Key.Should().Be(result.Key);
    }
}
