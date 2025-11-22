using System;
using System.Linq;
using System.Text;

namespace Cryptopals.Extensions;

public static class BytesExtensions
{
    public static string ToHex(this byte[] bytes) => Convert.ToHexString(bytes);
    public static string ToAscii(this byte[] bytes) => Encoding.ASCII.GetString(bytes);
    public static string ToBase64(this byte[] bytes) => Convert.ToBase64String(bytes);

    public static byte[] Xor(this byte[] bytes, byte[] key)
    {
        if (bytes.Length != key.Length)
        {
            throw new InvalidOperationException("The two strings must have the same length");
        }

        var output = new byte[bytes.Length];
        for (var i = 0; i < bytes.Length; i++)
        {
            output[i] = (byte)(bytes[i] ^ key[i]);
        }

        return output;
    }

    public static byte[] DecryptWithSingleCharKey(this byte[] bytes, byte key)
    {
        var sameLengthKey = bytes.Select(_ => key).ToArray();
        return bytes.Xor(sameLengthKey);
    }
}
