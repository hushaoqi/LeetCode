class Solution:
    def numMagicSquaresInside(self, grid: 'List[List[int]]') -> 'int':
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(1,m-1):
            for j in range(1,n-1):
                num = {grid[i-1][j-1], grid[i-1][j], grid[i-1][j+1],
                    grid[i][j-1], grid[i][j], grid[i][j+1],
                    grid[i+1][j-1], grid[i+1][j], grid[i+1][j+1]}
                numlen = len(num)
                # 判断填充数字是否为从 1 到 9 的不同数字
                if numlen != 9: continue
                if (1<=grid[i-1][j-1]<=9 and 1<=grid[i-1][j]<=9 and 1<=grid[i-1][j+1]<=9 and
                        1 <=grid[i][j-1]<=9 and 1<=grid[i][j]<=9 and 1<=grid[i][j+1]<=9 and
                        1 <=grid[i+1][j-1]<=9 and 1<=grid[i+1][j]<=9 and 1<=grid[i+1][j+1]<=9):
                # 判断每行，每列以及两条对角线上的各数之和都相等（可以用sum函数）
                    if( grid[i-1][j-1] + grid[i-1][j] + grid[i-1][j+1] ==
                        grid[i][j-1] + grid[i][j] + grid[i][j+1] ==
                        grid[i+1][j-1] + grid[i+1][j] + grid[i+1][j+1] ==
                        grid[i-1][j-1] + grid[i][j-1] + grid[i+1][j-1] ==
                        grid[i-1][j] + grid[i][j] + grid[i+1][j] ==
                        grid[i-1][j+1] + grid[i][j+1] + grid[i+1][j+1] ==
                        grid[i-1][j-1] + grid[i][j] + grid[i+1][j+1] ==
                        grid[i-1][j+1] + grid[i][j] + grid[i+1][j-1]
                    ):
                        count += 1
        return count

    def numMagicSquaresInside2(self, grid):
        def is_magic_square(grid, row, col):
            # s = 15
            # 判断填充数字是否为从 1 到 9 的不同数字
            if {
                grid[row - 1][col - 1],
                grid[row - 1][col],
                grid[row - 1][col + 1],
                grid[row][col - 1],
                grid[row][col],
                grid[row][col + 1],
                grid[row + 1][col - 1],
                grid[row + 1][col],
                grid[row + 1][col + 1]
             } != {1, 2, 3, 4, 5, 6, 7, 8, 9}:
                return 0
            for i in range(3):
                if grid[row - 1 + i][col - 1] + grid[row - 1 + i][col] + grid[row - 1 + i][col + 1] != 15:
                    return 0
                if grid[row - 1][col - 1 + i] + grid[row][col - 1 + i] + grid[row + 1][col - 1 + i] != 15:
                    return 0
            # if (grid[row+1][col-1] + grid[row][col] + grid[row-1][col+1]) != 15 or (grid[row-1][col-1] + grid[row][col] + grid[row+1][col+1]) != 15:
            #     return 0
            return 1

        cnt = 0
        row_len = len(grid)
        col_len = len(grid[0])
        for i in range(1, row_len - 1):
            for j in range(1, col_len - 1):
                if grid[i][j] == 5:
                    cnt += is_magic_square(grid, i, j)
        return cnt
    # 简化判断
    def numMagicSquaresInside3(self, grid):
        r = 0
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                if {grid[i][j], grid[i][j + 2], grid[i + 2][j], grid[i + 2][j + 2]} == {2, 4, 6, 8} and \
                        grid[i + 1][j + 1] == 5:
                    if sum(grid[i][j:j + 3]) == sum(grid[i + 2][j:j + 3]) == grid[i][j] + grid[i + 1][j] + grid[i + 2][ \
                        j] == 15:
                        r += 1
        return r
if __name__=='__main__':
    s = Solution()
    # grid = [[4,3,8,4],
    #         [9,5,1,9],
    #         [2,7,6,2]]
    grid = [[5, 5, 5],
            [5, 5, 5],
            [5, 5, 5]]
    print(s.numMagicSquaresInside3(grid))
