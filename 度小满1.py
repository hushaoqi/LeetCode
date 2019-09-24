
def minPathSum(grid: 'List[List[int]]', x, y) -> int:
    m, n = x + 500, y + 500
    dp = [0] * 1000
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
    x, y, n = map(int, input().split())
    grid = [[1]*1000 for _ in range(1000)]
    for i in range(n):
        xi, yi = map(int, input().split())
        # grid[xi+500][yi+500] = 1
    print(minPathSum(grid, x, y))
    print(x+y)