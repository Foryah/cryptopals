using System;
using System.Text;

namespace Set1 {
    public enum StringType {Hex, Base64, ASCII};

    public class BaseChanger {
        private byte[] _byteInput;

        public BaseChanger(string initialString, StringType type) {
            if (type == StringType.Hex) {
                LoadHex(initialString);
            }
        }

        private void LoadHex(string hexString) {
            _byteInput = new byte[hexString.Length / 2];
            for (int i = 0; i < _byteInput.Length; i++) {
                _byteInput[i] = Convert.ToByte(hexString.Substring(i * 2, 2), 16);
            }
        }

        public string ToAscii() => Encoding.ASCII.GetString(_byteInput);
        public string ToBase64() => Convert.ToBase64String(_byteInput);
    }

    public static class Solver {
        public static string HexToAscii(string hexString) {
            BaseChanger bChanger = new BaseChanger(hexString, StringType.Hex);
            return bChanger.ToAscii();
        }

        public static string HexToBase64(string hexString) {
            BaseChanger bChanger = new BaseChanger(hexString, StringType.Hex);
            return bChanger.ToBase64();
        }
    }
}