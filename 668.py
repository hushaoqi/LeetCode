class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        low, high = 1, m*n+1
        while low < high:
            mid = low + (high - low) // 2
            if self.LEX(m, n, mid) >= k:
                high = mid
            else:
                low = mid + 1
        return low
    def LEX(self,m, n, x):
        count = 0
        for i in range(1, m+1):
            count += min(x//i, n)
        return count

if __name__=='__main__':
    s = Solution()
    m, n, k = 3, 3, 5
    print(s.findKthNumber(m, n, k))