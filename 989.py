class Solution:
    def addToArrayForm(self, A: 'List[int]', K: 'int') -> 'List[int]':
        knum = []
        res = []
        while K != 0:
            knum.insert(0, K % 10)
            K //= 10

        lenK = len(knum)
        lenA = len(A)
        i, j = lenA - 1, lenK - 1
        carry = 0
        while i >= 0 and j >= 0:
            result = (A[i] + knum[j] + carry) % 10
            carry = (A[i] + knum[j] + carry) // 10
            res.insert(0, result)
            i -= 1
            j -= 1
        if j < 0:
            while i >= 0:
                result = (A[i] + carry) % 10
                carry = (A[i] + carry) // 10
                res.insert(0, result)
                i -= 1
        if i < 0:
            while j >= 0:
                result = (knum[j] + carry) % 10
                carry = (knum[j] + carry) // 10
                res.insert(0, result)
                j -= 1
        if carry != 0:
            res.insert(0, carry)
        return res
    # 可以不用转化K，直接计算
    def addToArrayForm2(self, A: 'List[int]', K: 'int') -> 'List[int]':
        n = len(A)
        i = n - 1
        while i >= 0 and K > 0:
            temp = A[i] + K % 10
            A[i] = temp % 10
            K //= 10
            K += temp // 10
            i -= 1
        while K > 0:
            A.insert(0, K % 10)
            K //= 10
        return A
if __name__ == '__main__':
    s = Solution()
    A = [1,2,0,0]
    K = 9999941
    print(s.addToArrayForm2(A,K))
