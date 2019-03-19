class Solution:
    def flipAndInvertImage(self, A: 'List[List[int]]') -> 'List[List[int]]':
        for i in range(len(A)):
            A[i] = A[i][::-1]  #图像翻转，即逆序
            for j in range(len(A[i])):
                A[i][j] = A[i][j] ^ 1  #反转图像，即0 全部被 1 替换， 1 全部被 0 替换，异或操作
        return A

    def flipAndInvertImage2(self, A: 'List[List[int]]') -> 'List[List[int]]':
        for i, p in enumerate(A):
            A[i] = list(reversed(p))
            # 2 invert
            for j, v in enumerate(A[i]):
                if A[i][j] is 0:
                    A[i][j] = 1
                else:
                    A[i][j] = 0
        return A
if __name__=='__main__':
    s = Solution()
    A = [[1,1,0],[1,0,1],[0,0,0]]
    print(s.flipAndInvertImage2(A))