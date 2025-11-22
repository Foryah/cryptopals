using System.IO;
using System.Linq;
using Cryptopals.Extensions;
using Cryptopals.Helpers;
using Cryptopals.Models;

namespace Cryptopals;

public static class Solver
{
    public static DecryptedMessageWithSingleCharKey FindMessageInFile(string filePath)
    {
        DecryptedMessageWithSingleCharKey? bestDecryptedMessageOverall = null;
        foreach (string line in File.ReadLines(filePath))
        {
            var decryptedMessage = DecryptWithSingleCharKey(line);
            if (bestDecryptedMessageOverall == null || decryptedMessage.ConfidenceScore > bestDecryptedMessageOverall.ConfidenceScore)
            {
                bestDecryptedMessageOverall = decryptedMessage;
            }
        }

        return bestDecryptedMessageOverall!;
    }
    
    public static DecryptedMessageWithSingleCharKey DecryptWithSingleCharKey(string hexInput)
    {
        var inputBytes = hexInput.HexToBytes();

        DecryptedMessageWithSingleCharKey? bestDecryptedMessage = null;
        var potentialKeys = Enumerable.Range(0, 256).Select(b => (byte)b).ToList();
        foreach (var key in potentialKeys)
        {
            var decryptedMessage = inputBytes.DecryptWithSingleCharKey(key);
            var englishConfidenceScore = EnglishFrequencyAnalyzer.CalculateEnglishConfidenceScore(decryptedMessage.ToAscii());

            if (bestDecryptedMessage == null || englishConfidenceScore > bestDecryptedMessage.ConfidenceScore)
            {
                bestDecryptedMessage = new DecryptedMessageWithSingleCharKey(decryptedMessage.ToAscii(), ((char)key).ToString(), englishConfidenceScore);
            }
        }

        return bestDecryptedMessage!;
    }

    public static string HexToAscii(string hexInput)
    {
        var inputBytes = hexInput.HexToBytes();
        return inputBytes.ToAscii();
    }

    public static string HexToBase64(string hexInput)
    {
        var inputBytes = hexInput.HexToBytes();
        return inputBytes.ToBase64();
    }

    public static string XorEqualHexes(string hexInput, string hexKey)
    {
        var inputBaseChanger = hexInput.HexToBytes();
        var keyBaseChanger = hexKey.HexToBytes();

        var xoredBytes = inputBaseChanger.Xor(keyBaseChanger);
        return xoredBytes.ToHex();
    }
}