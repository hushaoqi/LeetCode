import math
class Solution:
    #利用yield生成器，待解？？？？
    def fib(self, N: 'int') -> 'int':
        n, a, b = 0, 0, 1
        while n < N:
            yield b
            # print b
            a, b = b, a + b
            n = n + 1

    #通项公式
    def fib2(self, N: 'int') -> 'int':
        sqrt5 = math.sqrt(5)
        return round(pow((1 + sqrt5) / 2, N) / sqrt5)
        #return int((5 ** 0.5) * 0.2 * (((1 + 5 ** 0.5) / 2) ** N - ((1 - 5 ** 0.5) / 2) ** N))
    #递归转循环
    def fib3(self, N: 'int') -> 'int':
        n, a, b = 0, 0, 1
        #L = []
        while n < N:
            #L.append(b)
            a, b = b, a + b
            n = n + 1
        #return L[-1]
        return a
    #递归
    def fib4(self, N: 'int') -> 'int':
        if N == 0:
            return 0
        if N == 1:
            return 1
        return self.fib4(N-1) + self.fib4(N-2)

if __name__=='__main__':
    s = Solution()
    print(s.fib4(5))
    # for i in s.fib(6):
    #     print(i)


