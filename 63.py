class Solution:
    '''
    复杂度分析

    时间复杂度 ：O(M×N) 。长方形网格的大小是M×N，而访问每个格点恰好一次。
    空间复杂度 ：O(1)。我们利用 obstacleGrid 作为 DP 数组，因此不需要额外的空间。
    '''
    def uniquePathsWithObstacles(self, obstacleGrid: 'List[List[int]]') -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        # 左上角为初始点，由于没有路径可以到达，设置为1
        obstacleGrid[0][0] = 1
        # 左边第一列，只能由上一个结点到达，若上一个结点有障碍或不能到达，则该节点亦不能到达设置为1
        for i in range(1, m):
            obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1)
        # 上面第一行，只能由左边一个结点到达，若左边一个结点有障碍或者不能到达，则该结点亦不能到达设置为1
        for j in range(1, n):
            obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j-1] == 1)
        # 开始遍历网格，
        for i in range(1, m):
            for j in range(1, n):
                # 如果某个格点初始不包含任何障碍物，就把值赋为上方和左侧两个格点方案数之和
                # obstacleGrid[i, j] = obstacleGrid[i - 1, j] + obstacleGrid[i, j - 1]
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                # 如果这个点有障碍物，设值为 0 ，这可以保证不会对后面的路径产生贡献。
                else:
                    obstacleGrid[i][j] = 0
        return obstacleGrid[m-1][n-1]
    # 空间优化
    def uniquePathsWithObstacles2(self, obstacleGrid: 'List[List[int]]') -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [1] + [0] * n
        for i in range(0, m):
            for j in range(0, n):
                dp[j] = 0 if obstacleGrid[i][j] == 1 else dp[j] + dp[j - 1]
        return dp[-2]  # dp[-1]是为了当i = 0时方便计算，不用判断边界，所以dp[-2]才是解


if __name__=='__main__':
    s = Solution()
    grid =\
            [
                [0, 0, 0],
                [0, 1, 0],
                [0, 0, 0]
            ]
    print(s.uniquePathsWithObstacles2(grid))