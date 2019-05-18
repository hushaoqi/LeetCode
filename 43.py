class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        mul_res = ''
        len1 = len(num1)
        len2 = len(num2)
        res = [0]*(len1 + len2)  # 两数相乘得到的乘积的长度其实正好是两个数字的长度之和
        for i in range(len1-1, -1, -1):
            for j in range(len2-1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                p1 = i + j
                p2 = i + j + 1
                total = mul + res[p2]
                res[p1] += total // 10
                res[p2] = (total % 10)
        # print(res)
        while res[0] == 0 and len(res) > 1:
            res.pop(0)  # 去除前导零
        for val in res:
            mul_res += str(val)
        return mul_res

    def multiply2(self, num1: str, num2: str) -> str:
        return str(eval(num1 + "*" + num2))  #纯属好玩

if __name__=='__main__':
    S = Solution()
    print(S.multiply(num1='12345', num2='1'))
    '''
    "9133"
    "0"
    输出 "0000"
    预期结果 "0"
    '''