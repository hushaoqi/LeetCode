'''
要点：

晒法求素数。
质因数分解。
因子求和即为结果。
'''
class Solution:
    def minSteps(self, n: int) -> int:
        record = [1] * 1001
        # 晒法记录 0 ~ 1000 内的素数
        def Decomposition(n, record):
            i = 1
            res = 0
            while n > 1:
                if record[i] == 0:
                    i += 1
                else:
                    if n % i:
                        i += 1
                    else:
                        while n > 1 and n % i == 0:
                            n /= i
                            res += i
                        i += 1
            return res

        def update(record):
            record[1] = 0
            for i in range(2, 1001):
                if record[i] == 1:
                    k = 2
                    while k * i <= 1000:
                        record[k * i] = 0
                        k += 1
        update(record)


        # 如果n是素数的话，直接返回该数即可
        if record[n] == 1:
            return n

        # 否则质因数分解，结果便是所有质因数的和
        return Decomposition(n, record)

    # 递归求解

    def minSteps2(self, n: int) -> int:
        def count_num(n):
            a = 0
            if n == 1:
                return 0
            else:
                for i in range(n // 2, 2, -1):
                    if n % i == 0:
                        a = i
                        break
                if a == 0:
                    return n
                else:
                    return int(n/a)+count_num(a)
        return count_num(n)

    def minSteps3(self, n):
        if n == 1:
            return 0
        res = n
        for i in range(n-1,1,-1):
            if n % i == 0:
                res = min(res, self.minSteps3(n//i) + i)  # + i 表示以i为模，最多需要 i + n//i 次
        return res

    def minSteps4(self, n):
        res = 0
        for i in range(2, n+1):
            while n % i == 0:
                res += i
                n /= i
        return res

if __name__=='__main__':
    s = Solution()
    print(s.minSteps4(12))