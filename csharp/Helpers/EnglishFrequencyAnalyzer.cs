using System.Collections.Generic;

namespace Cryptopals.Helpers;

public static class EnglishFrequencyAnalyzer
{
    private static readonly Dictionary<char, int> EnglishLettersByFrequency = new Dictionary<char, int>
    {
        {'e', 13},
        {'t', 9},
        {'a', 8},
        {'o', 7},
        {'i', 7},
        {'n', 6},
        {'s', 6},
        {'h', 6},
        {'r', 6},
        {'d', 4},
        {' ', 4},
        {'l', 4},
        {'c', 3},
        {'u', 3},
        {'m', 2},
        {'w', 2},
        {'f', 2},
        {'y', 2},
        {'p', 2},
        {'b', 1},
        {'v', 1},
        {'k', 1},
        {'j', 0},
        {'x', 0},
        {'q', 0},
        {'z', 0}
    };

    public static int CalculateEnglishConfidenceScore(string input)
    {
        int score = 0;
        foreach (char c in input.ToLower())
        {
            if (EnglishLettersByFrequency.TryGetValue(c, out var value))
            {
                score += value;
            }
        }

        return score;
    }
}
