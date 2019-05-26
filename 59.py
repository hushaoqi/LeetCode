class Solution:
    def generateMatrix(self, n: int) -> 'List[List[int]]':
        if n == 0:
            return []
        matrix = [[0] * n for i in range(n)]
        up = 0
        down = n-1
        left = 0
        right = n-1
        num = 1

        while up <= down and left <= right:
            # 上
            j = left
            while j <= right:
                matrix[up][j] = num
                j += 1
                num += 1
            up += 1
            if up > down:
                break
            # 右
            i = up
            while i <= down:
                matrix[i][right] = num
                i += 1
                num += 1
            right -= 1
            if left > right:
                break
            # 下
            j = right
            while j >= left:
                matrix[down][j] = num
                j -= 1
                num += 1
            down -= 1
            if up > down:
                break
            # 左
            i = down
            while i >= up:
                matrix[i][left] = num
                i -= 1
                num += 1
            left += 1
            if left > right:
                break
        return matrix

    def generateMatrix2(self, n: int) -> 'List[List[int]]':
        matrix = [[0 for i in range(n)] for j in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for value in range(n * n):
            matrix[i][j] = value + 1
            if matrix[(i + di) % len(matrix)][(j + dj) % len(matrix[0])] != 0:
                di, dj = dj, -di  # 非常的巧妙
            i += di
            j += dj
        return matrix

    def generateMatrix3(self, n: int) -> 'List[List[int]]':
        ans = [[n ** 2]]
        t_len = n ** 2
        while t_len > n:
            temp = [list(i) for i in zip(*ans[::-1])]
            ans = [[i for i in range(t_len - len(temp[0]), t_len)]] + temp
            t_len -= len(temp[0])
        return ans

if __name__=='__main__':
    s =Solution()
    n = 4
    m = s.generateMatrix2(n)
    for i in range(n):
        print(m[i])
