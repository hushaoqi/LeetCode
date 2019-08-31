class Solution:
    # 双指针
    def isSubsequence(self, s: str, t: str) -> bool:
        lens = len(s)
        lent = len(t)
        if lens == 0:
            return True
        if lent == 0:
            return False
        i, j = 0, 0
        while i < lens and j < lent:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        if i == lens:
            return True
        else:
            return False
    # 动态规划
    # 思路：
    # 状态：dp[i][j]为s的从头开始到i的子字符串是否为t从头开始到j的子字符串的子序列
    # 状态转移公式：
    # 当char[i] == char[j]时，则字符i一定是j的子序列，如果0~i - 1子字符串是0~j - 1子字符串的子序列，
    # 则dp[i][j] = true，所以dp[i][j] = dp[i - 1][j - 1]；
    # 当char[i] != char[i]时，即判断当前0~i子字符串是否是0~j - 1的子字符串的子序列，
    # 即dp[i][j] = dp[i][j - 1]。如ab，eabc，虽然s的最后一个字符和t中最后一个字符不相等，
    # 但是因为ab是eab的子序列，所以ab也是eabc的子序列
    # 初始化：空字符串一定是t的子字符串的子序列，所以dp[0][j] = true
    # 结果：返回dp[sLen][tLen]

    def isSubsequence2(self, s: str, t: str) -> bool:
        lens = len(s)
        lent = len(t)
        dp = [[bool]*(lent+1) for _ in range(lens+1)]
        # 初始化
        for j in range(lent):
            dp[0][j] = True
        for i in range(1, lens+1):
            for j in range(1, lent+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[lens][lent]



if __name__=='__main__':
    s = Solution()
    strs = input().strip()
    strt = input().strip()
    print(s.isSubsequence2(strs, strt))
