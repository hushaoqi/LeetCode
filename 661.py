class Solution:
    def imageSmoother(self, M: 'List[List[int]]') -> 'List[List[int]]':
        col = len(M[0])
        row = len(M)
        N = [[0]*col for _ in range(row)]
        #(i-1,j-1),(i-1,j),(i-1,j+1)
        #(i, j-1 ),(i , j),(i, j+1 )
        #(i+1,j-1),(i+1,j),(i+1,j+1)
        positions = [[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1]]
        for i in range(row):
            for j in range(col):
                SUM = M[i][j]
                num = 1
                for position in positions:
                    x = i + position[0]
                    y = j + position[1]
                    if (x < 0 or x >= row or y < 0 or y >= col): continue
                    num += 1
                    SUM += M[x][y]
                N[i][j] = SUM // num
        return N

    def imageSmoother2(self, M: 'List[List[int]]') -> 'List[List[int]]':
        r, c = len(M), len(M[0]) #记住这种赋值方式
        N = [[0 for j in range(c)] for i in range(r)] #还有这种赋值方式
        if r == 1:
            if c == 1:
                return M
            N[0][0] = (M[0][0] + M[0][1]) // 2
            N[0][c-1] = (M[0][c-1] + M[0][c-2]) // 2
            for i in range(1, c-1):
                N[0][i] = (M[0][i-1] + M[0][i] + M[0][i+1]) // 3
            return N
        if c == 1:
            N[0][0] = (M[0][0] + M[1][0]) // 2
            N[r-1][0] = (M[r-1][0] + M[r-2][0]) // 2
            for i in range(1, r-1):
                N[i][0] = (M[i-1][0] + M[i][0] + M[i+1][0]) // 3
            return N
        #处理角点
        N[0][0] = (M[0][0] + M[0][1] + M[1][0] + M[1][1]) // 4
        N[0][c-1] = (M[0][c-1] + M[0][c-2] + M[1][c-1] + M[1][c-2]) // 4
        N[r-1][0] = (M[r-1][0] + M[r-1][1] + M[r-2][0] + M[r-2][1]) // 4
        N[r-1][c-1] = (M[r-1][c-1] + M[r-1][c-2] + M[r-2][c-1] + M[r-2][c-2]) // 4
        #单独处理边界
        for i in range(1, c-1):
            N[0][i] = (M[0][i-1] + M[0][i] + M[0][i+1] + M[1][i-1] + M[1][i] + M[1][i+1]) // 6
            N[r-1][i] = (M[r-1][i-1] + M[r-1][i] + M[r-1][i+1] + M[r-2][i-1] + M[r-2][i] + M[r-2][i+1]) // 6
        for i in range(1, r-1):
            N[i][0] = (M[i-1][0] + M[i][0] + M[i+1][0] + M[i-1][1] + M[i][1] + M[i+1][1]) // 6
            N[i][c-1] = (M[i-1][c-1] + M[i][c-1] + M[i+1][c-1] + M[i-1][c-2] + M[i][c-2] + M[i+1][c-2]) // 6
        #处理中间点
        for i in range(1, r-1):
            for j in range(1, c-1):
                N[i][j] = (M[i-1][j-1] + M[i-1][j] + M[i-1][j+1] + M[i][j-1] + M[i][j] + M[i][j+1] + M[i+1][j-1] + M[i+1][j] + M[i+1][j+1]) // 9
        return N
if __name__=='__main__':
    s = Solution()
    M = [[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]
    print(s.imageSmoother2(M))

