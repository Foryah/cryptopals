using System;
using System.Text;

namespace Cryptopals.Helpers;

public class BaseChanger 
{
    private byte[] _byteInput;

    public BaseChanger(string initialString, StringType type)
    {
        switch (type)
        {
            case StringType.Hex:
                LoadHex(initialString);
                break;
            default:
                throw new InvalidOperationException("Operation not supported!");
        }
    }
        
    public BaseChanger(byte[] initialBytes)
    {
        _byteInput = initialBytes;
    }

    public BaseChanger(BaseChanger anotherBaseChanger)
    {
        _byteInput = anotherBaseChanger.ToBytes();
    }

    private void LoadHex(string hexInput)
    {
        _byteInput = new byte[hexInput.Length / 2];
        for (int i = 0; i < _byteInput.Length; i++)
        {
            _byteInput[i] = Convert.ToByte(hexInput.Substring(i * 2, 2), 16);
        }
    }

    public string ToAscii() => Encoding.ASCII.GetString(_byteInput);
    public string ToBase64() => Convert.ToBase64String(_byteInput);
    public string ToHex() => BitConverter.ToString(_byteInput).Replace("-", string.Empty);
    public byte[] ToBytes() => _byteInput;
}
