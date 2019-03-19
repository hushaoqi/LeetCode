class Solution:
    def sortArrayByParity(self, A: 'List[int]') -> 'List[int]':
        even = []
        odd = []
        for num in A:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        return even + odd
if __name__=='__main__':
    s = Solution()
    A = [3, 1, 2, 4]
    print(s.sortArrayByParity(A))