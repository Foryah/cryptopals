using System;
using System.Text;

namespace Set1 
{
    public enum StringType {Hex, Base64, ASCII};

    public class HeXor
    {
        private BaseChanger _baseInput;

        public HeXor(BaseChanger baseInput)
        {
            _baseInput = baseInput;
        }

        public BaseChanger Xor(BaseChanger key)
        {
            byte[] baseBytes, keyBytes, xoredBytes;

            baseBytes = _baseInput.ToBytes();
            keyBytes = key.ToBytes();

            xoredBytes = ByteByByteXor(baseBytes, keyBytes);

            return new BaseChanger(xoredBytes);
        }

        private byte[] ByteByByteXor(byte[] baseBytes, byte[] keyBytes)
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
    }

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
            BaseChanger xoredBaseChanger;

            HeXor hexxor = new HeXor(inputBaseChanger);
            xoredBaseChanger = hexxor.Xor(keyBaseChanger);

            return xoredBaseChanger.ToHex();
        }
    }
}