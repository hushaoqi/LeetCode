import sys
class Solution:
    # 暴力递归 cost(i,j) = grid[i][j] + min(cost(i+1,j), cost(i,j+1))
    def minPathSum(self, grid: 'List[List[int]]') -> int:

        def caculate(i: int, j: int):
            # 递归初始点
            if i == len(grid) or j == len(grid[0]):
                return sys.maxsize
            # 到达终点
            if i == len(grid)-1 and j == len(grid[0])-1:
                return grid[i][j]
            return grid[i][j] + min(caculate(i + 1, j), caculate(i, j + 1))
        return caculate(0, 0)

    # 二维动态规划 dp(i,j)=grid(i,j)+min(dp(i+1,j),dp(i,j+1))
    def minPathSum2(self, grid: 'List[List[int]]') -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j != n-1:
                    dp[i][j] = grid[i][j] + dp[i][j+1]
                elif i != m-1 and j == n-1:
                    dp[i][j] = grid[i][j] + dp[i+1][j]
                elif i != m-1 and j != n-1:
                    dp[i][j] = grid[i][j] + min(dp[i+1][j], dp[i][j+1])
                else:
                    dp[i][j] = grid[i][j]
        return dp[0][0]
    # 一维动态规划  dp(j)=grid(i,j)+min(dp(j),dp(j+1))
    def minPathSum3(self, grid: 'List[List[int]]') -> int:
        m, n = len(grid), len(grid[0])
        dp = [0] * n
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j != n-1:
                    dp[j] = grid[i][j] + dp[j+1]
                elif i != m-1 and j == n-1:
                    dp[j] = grid[i][j] + dp[j]
                elif i != m-1 and j != n-1:
                    dp[j] = grid[i][j] + min(dp[j+1], dp[j])
                else:
                    dp[j] = grid[i][j]
        return dp[0]

if __name__=='__main__':
    s = Solution()
    grid = \
        [
            [1, 3, 1],
            [1, 5, 1],
            [4, 2, 1]
        ]
    print(s.minPathSum3(grid))