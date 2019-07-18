class Solution:
    def addBinary(self, a: str, b: str) -> str:
        lista = list(map(int,list(a)))
        listb = list(map(int,list(b)))
        # print(lista)
        # print(listb)
        carry = 0
        res = []
        i, j = len(a)-1, len(b)-1
        while i >= 0 or j >= 0:
            sum = carry
            sum += lista[i] if i >= 0 else 0
            sum += listb[j] if j >= 0 else 0
            res.append(sum % 2)
            carry = sum // 2
            i -= 1
            j -= 1
        if carry == 1:
            res.append(carry)
        res = res[::-1]
        result = ''
        for i in range(len(res)):
            result += ''.join(str(res[i]))
        return result




if __name__=='__main__':
    s = Solution()
    a = "10"
    b = "11"
    print(s.addBinary(a, b))