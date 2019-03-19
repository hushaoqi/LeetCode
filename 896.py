class Solution:
    def isMonotonic(self, A: 'List[int]') -> 'bool':
        if len(A) == 1: return True
        for i in range(0,len(A)-1):
            if A[0] >= A[-1]:
                if A[i] < A[i+1]:
                    return False
            if A[0] <= A[-1]:
                if A[i] > A[i+1]:
                    return False
        return True
if __name__=='__main__':
    s = Solution()
    A = [1,1,0]
    print(s.isMonotonic(A))

