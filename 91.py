class Solution:
    # dpi = dpi−2 + dpi−1
    # 输入 '12' 的结果为 2，如果我们在 '12' 后面增加一个数字 3，输入变成 '123'，结果是 '12'的结果 + '1'的结果 = 3
    # i 从索引 1 开始逐渐遍历 s，当前位置对应结果 = 上上次结果(如果 i 位置字符和 i-1 位置字符的组合满足条件) + 上次结果(如果 s[i] 不为 0)
    def numDecodings(self, s: str) -> int:
        pp, p = 1, int(s[0] != '0')
        for i in range(1, len(s)):
            pp, p = p, pp * (9 < int(s[i - 1:i + 1]) <= 26) + p * (int(s[i]) > 0)
        return p

    def numDecodings2(self, s: str) -> int:
        if s == '':
            return 0
        if s[0] == '0':
            return 0
        dp = [1 for i in range(len(s) + 1)]
        for i in range(2, len(s) + 1):
            if 9 < int(s[i - 2:i]) <= 26:
                if not int(s[i - 1]) == 0:
                    dp[i] = dp[i - 1] + dp[i - 2]
                else:
                    dp[i] = dp[i - 2]
            else:
                if not int(s[i - 1]) == 0:
                    dp[i] = dp[i - 1]
                else:
                    return 0
        return dp[-1]

if __name__=='__main__':
    s = Solution()
    while True:
        strs = input().strip()
        if len(strs) == 0:
            break
        else:
            print(s.numDecodings(strs))