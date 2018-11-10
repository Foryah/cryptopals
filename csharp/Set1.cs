using System;
using System.Text;

public static class BaseChanger {
    private static byte[] byteInput;

    public static void loadHexa(string hexString) {
        byteInput = new byte[hexString.Length / 2];
        for (int i = 0; i < byteInput.Length; i++) {
            byteInput[i] = Convert.ToByte(hexString.Substring(i * 2, 2), 16);
        }
    }

    public static string toString() {
        return Encoding.ASCII.GetString(byteInput);
    }

    public static string toBase64() {
        return System.Convert.ToBase64String(byteInput);
    }
}

public static class Set1 {
    public static string HexToString(string hexString) {
        BaseChanger.loadHexa(hexString);
        return BaseChanger.toString();
    }

    public static string HexToBase64(string hexString) {
        BaseChanger.loadHexa(hexString);
        return BaseChanger.toBase64();
    }
}