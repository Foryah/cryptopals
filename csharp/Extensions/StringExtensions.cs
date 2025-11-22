using System;
using System.Text;

namespace Cryptopals.Extensions;

public static class StringExtensions
{
    public static byte[] HexToBytes(this string hexString) => Convert.FromHexString(hexString);
    public static byte[] AsciiToBytes(this string asciiString) => Encoding.ASCII.GetBytes(asciiString);
    public static byte[] Base64ToBytes(this string b64Text) => Convert.FromBase64String(b64Text);
}
