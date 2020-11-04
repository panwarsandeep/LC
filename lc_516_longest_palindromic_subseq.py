from functools import cmp_to_key
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        slen = len(s)
        # each cell of this this dp table represents length of longest palindromic subsequence
        # for the string s[i:j], here i is represented as row and j as column
        dp = [[0]*slen for _ in range(slen)]
        for i in range(slen):
            # each single char is palindrome for length 1, so s[i:i] represents one char
            # e.g. (0,0), (1,1) etc.
            dp[i][i] = 1
            if i < slen - 1 and s[i] == s[i+1]:
                dp[i][i+1] = 2
        for k in range(2, slen+1):
            for i in range(0, slen - k + 1):
                j = i + k - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][slen-1]


if __name__ == '__main__':
    sol = Solution()

    s = "aabaa"
    print(s)
    r = sol.longestPalindromeSubseq(s)
    print(r)