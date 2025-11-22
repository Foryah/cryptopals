using Cryptopals.Helpers;

namespace Cryptopals;

public static class Solver
{
    public static string HexToAscii(string hexInput)
    {
        BaseChanger bChanger = new BaseChanger(hexInput, StringType.Hex);
        return bChanger.ToAscii();
    }

    public static string HexToBase64(string hexInput)
    {
        BaseChanger bChanger = new BaseChanger(hexInput, StringType.Hex);
        return bChanger.ToBase64();
    }

    public static string XorEqualHexes(string hexInput, string hexKey)
    {
        BaseChanger inputBaseChanger = new BaseChanger(hexInput, StringType.Hex);
        BaseChanger keyBaseChanger = new BaseChanger(hexKey, StringType.Hex);

        HeXor hexxor = new HeXor(inputBaseChanger);
        var xoredBaseChanger = hexxor.Xor(keyBaseChanger);

        return xoredBaseChanger.ToHex();
    }
}