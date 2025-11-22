namespace Cryptopals.Models;

public class DecryptedMessageWithSingleCharKey(string decryptedMessage, string key, int confidenceScore = 0)
{
    public string DecryptedMessage { get; set; } = decryptedMessage;
    public string Key { get; set; } = key;
    public int ConfidenceScore { get; set; } = confidenceScore;
}
