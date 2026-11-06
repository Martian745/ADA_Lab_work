
def longestCommonSubsequence(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)

    # Use the shorter string for space optimization
    if n > m:
        text1, text2 = text2, text1
        m, n = n, m

    dp = [0] * (n + 1)

    for i in range(1, m + 1):
        diagonal = 0

        for j in range(1, n + 1):
            previous = dp[j]

            if text1[i - 1] == text2[j - 1]:
                dp[j] = diagonal + 1
            else:
                dp[j] = max(dp[j], dp[j - 1])

            diagonal = previous

    return dp[n]


def minDistance(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)

    # Initialize base cases
    dp = list(range(n + 1))

    for i in range(1, m + 1):
        diagonal = dp[0]
        dp[0] = i

        for j in range(1, n + 1):
            previous = dp[j]

            if word1[i - 1] == word2[j - 1]:
                dp[j] = diagonal
            else:
                dp[j] = 1 + min(
                    diagonal,    # Replace
                    dp[j],       # Delete
                    dp[j - 1]    # Insert
                )

            diagonal = previous

    return dp[n]


def main():
    print("=== String Dynamic Programming Suite ===")

    text1 = input("Enter first string: ")
    text2 = input("Enter second string: ")

    lcs = longestCommonSubsequence(text1, text2)
    distance = minDistance(text1, text2)

    print("\nLongest Common Subsequence Length:", lcs)
    print("Minimum Edit Distance:", distance)


if __name__ == "__main__":
    main()
