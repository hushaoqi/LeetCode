'''
               dp[i + 1][j - 1] + 2                       if (s[i] == s[j])
            /
dp[i][j] =

            \  max(dp[i + 1][j], dp[i][j - 1])        if (s[i] != s[j])
'''
import sys
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        dp = [[0]*n for _ in range(n)]
        i = n - 1
        while i >= 0:
            dp[i][i] = 1
            j = i + 1
            while j < n:
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

                j += 1
            i -= 1
        return dp[0][n-1]

    # 进行空间优化
    def longestPalindromeSubseq2(self, s: str) -> int:
        n = len(s)
        res = 0
        dp = [1] * n
        for i in range(n-1, -1, -1):
            length = 0
            for j in range(i+1, n):
                temp = dp[j]
                if s[i] == s[j]:
                    dp[j] = length + 2
                length = max(length, temp)
        for num in dp:
            res = max(res, num)
        return res


if __name__ == '__main__':
    s = Solution()
    while True:
        strs = sys.stdin.readline().strip()
        if len(strs) != 0:
            print(s.longestPalindromeSubseq(strs))
        else:
            break