using System.Collections.Generic;
using System.IO;
using System.Linq;
using Cryptopals.Extensions;
using Cryptopals.Helpers;
using Cryptopals.Models;

namespace Cryptopals;

public static class Solver
{
    public static string DecryptAES128InECBMode(string filePath, string key)
    {
        var encryptedB64Text = File.ReadAllText(filePath);
        var encryptedText = encryptedB64Text.Base64ToBytes();

        var decryptedBytes = encryptedText.AES128InECBDecrypt(key.AsciiToBytes());
        return decryptedBytes.ToAscii();
    }

    public static DecryptedMessageWithKey DecryptRepeatedKeyXoredFile(string filePath)
    {
        var encryptedB64Text = File.ReadAllText(filePath);
        var encryptedText = encryptedB64Text.Base64ToBytes();

        var keyLengthNormalisedHammingDistance = new Dictionary<int, int>();
        var keyLengthsToTry = Enumerable.Range(2, 40).ToList();
        foreach (var keyLength in keyLengthsToTry)
        {
            var keyLengthSizeChunks = encryptedText[..(keyLength * 4)].Chunk(keyLength).ToList();

            var normalizedHammingDistanceGroup1 = keyLengthSizeChunks[0].GetHammingDistance(keyLengthSizeChunks[1]) / keyLength;
            var normalizedHammingDistanceGroup2 = keyLengthSizeChunks[1].GetHammingDistance(keyLengthSizeChunks[2]) / keyLength;
            var normalizedHammingDistanceGroup3 = keyLengthSizeChunks[2].GetHammingDistance(keyLengthSizeChunks[3]) / keyLength;

            var normalisedTotalHammingDistance = normalizedHammingDistanceGroup1 + normalizedHammingDistanceGroup2 + normalizedHammingDistanceGroup3 / 3;

            keyLengthNormalisedHammingDistance[keyLength] = normalisedTotalHammingDistance;
        }

        DecryptedMessageWithKey? bestDecryptedMessageOverall = null;
        var bestKeyHammingDistance = keyLengthNormalisedHammingDistance
            .OrderBy(kv => kv.Value)
            .Take(3)
            .Select(kv => kv.Value);
        var bestKeyLengths = keyLengthNormalisedHammingDistance
            .Where(k => bestKeyHammingDistance.Contains(k.Value))
            .Select(k => k.Key);
        foreach (var keyLength in bestKeyLengths)
        {
            var keyLengthSizeChunks = encryptedText.Chunk(keyLength).ToList();

            var blockMap = new Dictionary<int, List<byte>>();
            for (var i = 0; i < keyLength; i++)
            {
                blockMap[i] = [];
            }

            foreach (var chunk in keyLengthSizeChunks)
            {
                for (var i = 0; i < chunk.Length; i++)
                {
                    blockMap[i].Add(chunk[i]);
                }
            }

            var keyBytesList = new List<byte>();
            foreach (var block in blockMap.Values)
            {
                var blockBytes = block.ToArray();
                var decryptedBlock = DecryptWithSingleCharKey(blockBytes.ToHex());
                keyBytesList.Add((byte)decryptedBlock.Key[0]);
            }

            var keyBytes = keyBytesList.ToArray();
            var decryptedBytes = encryptedText.XorWithRepeatedKey(keyBytes);
            var decryptedMessage = decryptedBytes.ToAscii();
            var englishConfidenceScore = EnglishFrequencyAnalyzer.CalculateEnglishConfidenceScore(decryptedMessage);

            if (bestDecryptedMessageOverall == null || englishConfidenceScore > bestDecryptedMessageOverall.ConfidenceScore)
            {
                bestDecryptedMessageOverall = new DecryptedMessageWithKey(decryptedMessage, keyBytes.ToAscii(), englishConfidenceScore);
            }
        }

        return bestDecryptedMessageOverall!;
    }

    public static int CalculateHammingDistance(string asciiA, string asciiB)
    {
        var bytesA = asciiA.AsciiToBytes();
        var bytesB = asciiB.AsciiToBytes();

        return bytesA.GetHammingDistance(bytesB);
    }

    public static string EncryptWithRepeatingKeyToHex(string asciiText, string key)
    {
        var plainTextBytes = asciiText.AsciiToBytes();
        var keyBytes = key.AsciiToBytes();

        var encryptedBytes = plainTextBytes.XorWithRepeatedKey(keyBytes);
        return encryptedBytes.ToHex();
    }

    public static DecryptedMessageWithKey FindMessageInFile(string filePath)
    {
        DecryptedMessageWithKey? bestDecryptedMessageOverall = null;
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

    public static DecryptedMessageWithKey DecryptWithSingleCharKey(string hexInput)
    {
        var inputBytes = hexInput.HexToBytes();

        DecryptedMessageWithKey? bestDecryptedMessage = null;
        var potentialKeys = Enumerable.Range(0, 256).Select(b => (byte)b).ToList();
        foreach (var key in potentialKeys)
        {
            var decryptedMessage = inputBytes.XorWithSingleCharKey(key);
            var englishConfidenceScore = EnglishFrequencyAnalyzer.CalculateEnglishConfidenceScore(decryptedMessage.ToAscii());

            if (bestDecryptedMessage == null || englishConfidenceScore > bestDecryptedMessage.ConfidenceScore)
            {
                bestDecryptedMessage = new DecryptedMessageWithKey(decryptedMessage.ToAscii(), ((char)key).ToString(), englishConfidenceScore);
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