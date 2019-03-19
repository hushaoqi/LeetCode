class Solution:
    def sortArrayByParityII(self, A: 'List[int]') -> 'List[int]':
        even = []
        odd = []
        res = []
        for i in range(0, len(A)):
            if A[i] % 2 == 0:
                even.append(A[i])
            else:
                odd.append(A[i])

        for j in range(0, len(even)):
            res.append(even[j])
            res.append(odd[j])
        return res
    # 代码优化，节省内存
    def sortArrayByParityII2(self, A: 'List[int]') -> 'List[int]':
        odd = 1
        even = 0
        res = [0] * (len(A))
        for i in A:
            if i % 2 == 0:
                res[even] = i
                even += 2
            else:
                res[odd] = i
                odd += 2
        return res

if __name__=='__main__':
    s = Solution()
    A = [4,2,5,7]
    print(s.sortArrayByParityII(A))