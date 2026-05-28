class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)

        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # Empty string matches empty pattern
        dp[m][n] = True

        # Fill table from bottom-right to top-left
        for i in range(m, -1, -1):
            for j in range(n - 1, -1, -1):

                first_match = (
                    i < m and 
                    (p[j] == s[i] or p[j] == ".")
                )

                # Case where next pattern character is "*"
                if j + 1 < n and p[j + 1] == "*":
                    dp[i][j] = (
                        dp[i][j + 2] or                 # use zero copies
                        (first_match and dp[i + 1][j])  # use one or more copies
                    )

                # Normal character match
                else:
                    dp[i][j] = first_match and dp[i + 1][j + 1]

        return dp[0][0]
