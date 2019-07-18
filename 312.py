class Solution:
    def maxCoins(self, nums: 'List[int]') -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for m in range(2,n):
            for i in range(n-m):
                j = i + m
                for k in range(i+1, j):
                    dp[i][j] = max(dp[i][j], nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j])
        print(dp)
        return dp[0][n - 1]

if __name__ == '__main__':
    s = Solution()
    nums = [3,1,5,8]
    print(s.maxCoins(nums))
