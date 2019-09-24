class Solution:
    def __init__(self):
        self.count = 0

    def movingCount(self, threshold, rows, cols):
        arr = [[False] * cols for _ in range(rows)]
        self.findWay(arr, 0, 0, threshold)
        return self.count

    def findWay(self, arr, i, j, k):
        if i < 0 or j < 0 or i >= len(arr) or j >= len(arr[0]):
            return
        tempi = list(map(int, list(str(i))))
        tempj = list(map(int, list(str(j))))
        if sum(tempi) + sum(tempj) > k or arr[i][j] is True:
            return
        arr[i][j] = True
        self.count += 1
        self.findWay(arr, i+1, j, k)
        self.findWay(arr, i-1, j, k)
        self.findWay(arr, i, j+1, k)
        self.findWay(arr, i, j-1, k)


if __name__=='__main__':
    s = Solution()
    print(s.movingCount(3, 4, 4))
