class Solution:
    def spiralOrder(self, matrix: 'List[List[int]]') -> 'List[int]':
        if len(matrix) == 0:
            return []
        up = 0
        down = len(matrix)-1
        left = 0
        right = len(matrix[0])-1
        res = list()

        while up <= down and left <= right:
            # 上
            res.extend(matrix[up][left:right+1])
            up += 1
            if up > down:
                break
            # 右
            # i = up
            # while i <= down:
            #     res.append(matrix[i][right])
            #     i += 1
            res.extend([matrix[i][right] for i in range(up, down + 1)])  # 替代上面的循环
            right -= 1
            if left > right:
                break
            # 下
            temp = matrix[down][left:right+1]
            res.extend(temp[::-1])  # 逆序
            down -= 1
            if up > down:
                break
            # 左
            # i = down
            # while i >= up:
            #     res.append(matrix[i][left])
            #     i -= 1
            res.extend([matrix[i][left] for i in range(down, up-1, -1)])  # 替代上面的循环,但执行用时似乎比上面的长

            left += 1
            if left > right:
                break
        return res

if __name__=='__main__':
    s = Solution()
    m, n = map(int, input().split())
    matrix = []
    for i in range(m):
        matrix.append(list(map(int, input().split())))


    result = s.spiralOrder(matrix)
    result = str(result)
    for t in result:
        if t != '[' and t != ']' and t != ' ':
            print(t,end="")
