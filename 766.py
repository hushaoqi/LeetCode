class Solution:
    '''
    1 2 3 4
    5 1 2 3
    9 5 1 2
    起点移动的方向是9 -> 5 -> 1 -> 2 -> 3 -> 4
    '''
    def isToeplitzMatrix(self, matrix: 'List[List[int]]') -> 'bool':
        row = len(matrix)
        col = len(matrix[0])
        p = row - 1
        q = 0
        while p >= 0 and q < col:
            val, i, j = matrix[p][q], p, q
            while i + 1 < row and j + 1 < col:
                i += 1
                j += 1
                if matrix[i][j] != val:
                    return False
            if p > 0:
                p = p - 1
            else:
                q = q + 1
        return True
    #按正常顺序来遍历数组，对于每个遍历到的数字，都跟其右下方的数字对比，如果不相同，直接返回false即可
    def isToeplitzMatrix2(self, matrix: 'List[List[int]]') -> 'bool':
        for i in range(len(matrix)-1):
            for j in range(len(matrix[0])-1):
                if matrix[i][j] != matrix[i+1][j+1] :
                    return False
        return True
    '''
    错位按行对比
    [1, 2, 3] == [1, 2, 3] 
    [5, 1, 2] == [5, 1, 2] 
    True
    '''
    def isToeplitzMatrix3(self, matrix: 'List[List[int]]') -> 'bool':
        for i in range(1, len(matrix)):
            #print(matrix[i][1:],' ',matrix[i - 1][0:-1],'\n')
            if matrix[i][1:] != matrix[i - 1][0:-1]:
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    matrix = [
        [1, 2, 3, 4],
        [5, 1, 2, 3],
        [9, 5, 1, 2]
    ]
    print(s.isToeplitzMatrix3(matrix))
