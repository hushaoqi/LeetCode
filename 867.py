class Solution:
    def transpose(self, A: 'List[List[int]]') -> 'List[List[int]]':
        # 交换矩阵的行索引与列索引
        res = [[0] * len(A) for i in range(len(A[0]))]
        for r, row in enumerate(A):
            for c, val in enumerate(row):
                res[c][r] = val
        return res

    def transpose2(self, A: 'List[List[int]]') -> 'List[List[int]]':
        return [list(value) for value in zip(*A)]

if __name__=='__main__':
    s = Solution()
    # A = [[1,2,3],[4,5,6],[7,8,9]]
    A = [[1,2,3],[4,5,6]]
    print(s.transpose(A))