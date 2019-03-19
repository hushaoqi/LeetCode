class Solution:
    def sortedSquares(self, A: 'List[int]') -> 'List[int]':
        res = []
        for num in A:
            res.append(num*num)
        res.sort()
        return res
        #return sorted([x * x for x in A])

if __name__ == '__main__':
    s = Solution()
    A = [-4,-1,0,3,10]
    print(s.sortedSquares(A))