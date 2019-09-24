def min_Path_Sum(grid: 'List[List[int]]', m, n) -> int:
    dp = [0] * n
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if i == m - 1 and j != n - 1:
                dp[j] = grid[i][j] + dp[j + 1]
            elif i != m - 1 and j == n - 1:
                dp[j] = grid[i][j] + dp[j]
            elif i != m - 1 and j != n - 1:
                dp[j] = grid[i][j] + min(dp[j + 1], dp[j])
            else:
                dp[j] = grid[i][j]
    return dp[0]
m = int(input())
n = int(input())
grid = []
for _ in range(m):
    grid.append(list(map(int, input().split())))
print(min_Path_Sum(grid, m, n))