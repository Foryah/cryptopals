using System;

namespace Cryptopals.Extensions;

public static class StringExtensions
{
    public static byte[] HexToBytes(this string hexString) => Convert.FromHexString(hexString);
}
