import math
class Solution:
    # 很明显递归会超出时间限制
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)

    # 递归改进
    def climbStairs1(self, n: int) -> int:
        self.res = [0] * (n + 1)
        return self.helper(n)

    def helper(self, n: int):
        if n <= 1:
            return 1
        if self.res[n] > 0:
            return self.res[n]
        self.res[n] = self.helper(n - 1) + self.helper(n - 2)
        return self.res[n]

    # 一维动态规划，记录前两次的结果
    def climbStairs2(self, n: int) -> int:
        if n <= 1:
            return 1
        dp = [0]*n
        dp[0] = 1  # 一步台阶
        dp[1] = 2  # 两步台阶
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp.pop()

    # 进一步优化，我们只用两个整型变量a和b来存储过程值
    def climbStairs3(self, n: int) -> int:
        a = 1
        b = 1
        while n > 0:
            b += a
            a = b - a
            n -= 1
        return a
    # 神仙操作：分治法 Divide and Conquer 的解法
    def climbStairs4(self, n: int) -> int:
        if n <= 1:
            return 1
        return self.climbStairs4(n // 2) * self.climbStairs4(n - n // 2) + self.climbStairs4(n // 2 - 1) * self.climbStairs4(n - n // 2 - 1)
    # 神仙操作：通项公式
    def climbStairs5(self, n: int) -> int:
        root5 = math.sqrt(5)
        return int((1 / root5) * (pow((1 + root5) / 2, n + 1) - pow((1 - root5) / 2, n + 1)))

if __name__=='__main__':
    s = Solution()
    print(s.climbStairs1(6))