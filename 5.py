class Solution:
    # 暴力搜索 对于Python这种渣渣性能肯定超时
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        n = len(s)
        max_st = ''
        for i in range(n):  # 从每一个字符开始，截取到最后一个字符
            for j in range(i, n):
                st = s[i: j+1]
                if st == st[::-1] and len(st) > len(max_st):
                    max_st = st
        return max_st
    # 动态规划
    def longestPalindrome2(self, s: str) -> str:
        k = len(s) # 计算字符串的长度
        matrix = [[0 for i in range(k)] for i in range(k)] # 初始化n*n的列表
        logestSubStr = ""  # 存储最长回文子串
        logestLen = 0 # 最长回文子串的长度

        for j in range(0, k):
            for i in range(0, j + 1):
                if j - i <= 1:
                    if s[i] == s[j]:
                        matrix[i][j] = 1 # 此时f(i,j)置为true
                        if logestLen < j - i + 1: # 将s[i:j]的长度与当前的回文子串的最长长度相比 
                            logestSubStr = s[i:j + 1]  # 取当前的最长回文子串
                            logestLen = j - i + 1  # 当前最长回文子串的长度
            else:
                if s[i] == s[j] and matrix[i + 1][j - 1]:  # 判断
                    matrix[i][j] = 1
                if logestLen < j - i + 1:
                    logestSubStr = s[i:j + 1]
                    logestLen = j - i + 1

        return logestSubStr



if __name__=='__main__':
    s = Solution()
    string = "cb"
    print(s.longestPalindrome2(string))