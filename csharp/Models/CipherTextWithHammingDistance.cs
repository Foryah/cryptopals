namespace Cryptopals.Models;

public class CipherTextWithHammingDistance(string cipherText, int hammingDistance)
{
    public string CipherText { get; set; } = cipherText;
    public int HammingDistance { get; set; } = hammingDistance;
}
