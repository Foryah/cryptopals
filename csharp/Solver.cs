using Cryptopals.Extensions;

namespace Cryptopals;

public static class Solver
{
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