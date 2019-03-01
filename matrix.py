class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        d = len(matrix)
        for u in range(0,d):
            l = 0
            r = len(matrix[u]) - 1
            while l <= r:
                mid = (l + r) // 2
                #print(matrix[u][mid])
                if matrix[u][mid] == target:return True
                if matrix[u][mid] < target: l = mid + 1
                if matrix[u][mid] > target: r = mid - 1
        return False
if __name__=='__main__':
    s = Solution()
    matrix = \
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
    target = 20
    print(s.searchMatrix(matrix,target))