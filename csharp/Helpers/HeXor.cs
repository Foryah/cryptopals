using System;

namespace Cryptopals.Helpers;

public class HeXor(BaseChanger baseInput)
{
    public BaseChanger Xor(BaseChanger key)
    {
        var baseBytes = baseInput.ToBytes();
        var keyBytes = key.ToBytes();

        var xoredBytes = ByteByByteXor(baseBytes, keyBytes);

        return new BaseChanger(xoredBytes);
    }

    #region Private
    private static byte[] ByteByByteXor(byte[] baseBytes, byte[] keyBytes)
    {
        if (baseBytes.Length != keyBytes.Length)
        {
            throw new InvalidOperationException("The two strings must have the same length");
        }

        byte[] resultBytes = new byte[baseBytes.Length];
        for (int i = 0; i < baseBytes.Length; i++)
        {
            resultBytes[i] = (byte)((int)baseBytes[i] ^ (int)keyBytes[i]);
        }
            
        return resultBytes;
    }
    #endregion
}
