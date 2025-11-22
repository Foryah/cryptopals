namespace Cryptopals.Helpers;

public static class EnglishFrequencyAnalyzer
{
    private static readonly string EnglishLettersByFrequency = "etaoinshrd lcumwfgypbvkjxqz";

    public static int CalculateEnglishConfidenceScore(string input)
    {
        int score = 0;
        foreach (char c in input.ToLower())
        {
            if (EnglishLettersByFrequency.Contains(c))
            {
                score += EnglishLettersByFrequency.Length - EnglishLettersByFrequency.IndexOf(c);
            }
        }

        return score;
    }
}
