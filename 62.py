import math
class Solution:
    # 思路一:排列组合 因为机器到底右下角,向下几步,向右几步都是固定的,
    # 比如,m=3,n=2,我们只要向下1步,向右2步就一定能到达终点. 所以有C_{m+n-2}^{m-1}
    def uniquePaths(self, m: int, n: int) -> int:
        return math.factorial(m+n-2) // (math.factorial(m-1) * math.factorial(n-1))
    '''
    思路二:动态规划

    我们令dp[i][j]是到达i,j最少步数
    
    动态方程: dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    注意,对于第一行dp[0][j],或者第一列dp[i][0],由于都是在边界,所以只能为1
    
    时间复杂度:O(m*n)O(m∗n)
    
    空间复杂度:O(m * n)O(m∗n)
    
    优化:因为我们每次只需要dp[i-1][j],dp[i][j-1]
    
    所以我们只要记录这两个数,直接看代码吧!
    '''
    def uniquePaths2(self, m: int, n: int) -> int:
        dp = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        # print(dp)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

    def uniquePaths3(self, m: int, n: int) -> int:
        pre = [1] * n
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] = pre[j] + cur[j - 1]
            pre = cur[:]
        return pre[-1]

    def uniquePaths4(self, m: int, n: int) -> int:
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j - 1]
        return cur[-1]

if __name__=='__main__':
    s = Solution()
    print(s.uniquePaths2(3, 3))