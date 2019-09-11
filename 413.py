class Solution:
    def numberOfArithmeticSlices(self, A: 'List[int]') -> int:
        dp = [0]*len(A)
        SUM = 0
        for i in range(2, len(A)):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                dp[i] = 1 + dp[i-1]
                SUM += dp[i]

        return SUM

if __name__=='__main__':
    s = Solution()
    A = [1, 2, 3, 4]
    print(s.numberOfArithmeticSlices(A))