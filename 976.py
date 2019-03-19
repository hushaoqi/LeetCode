class Solution:
    def largestPerimeter(self, A: 'List[int]') -> 'int':
        A = sorted(A)
        A.reverse()
        # A.sort(reverse=True)
        for i in range(len(A)- 2):
            if A[i] < A[i+1] + A[i+2]:
                return sum(A[i:i+3])
        return 0
if __name__=='__main__':
    s = Solution()
    A = [3,6,2,3]
    print(s.largestPerimeter(A))
