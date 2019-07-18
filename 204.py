import math
class Solution:
    def countPrimes(self, n: int) -> int:
        res = 1  # 从3开始计算，"2"是质数，所以初始化为1
        if n < 3:
            return 0
        else:
            for i in range(3, n):
                if i % 2 == 0:
                    continue
                flag = True  # False 表示不是素数
                for j in range(3,int(math.sqrt(i))+1, 2):
                    if i % j == 0:
                        flag = False
                        break
                if flag == True:
                    # print(i,end=' ')
                    res += 1
        return res
#  上面那种方法超时
    '''
    解法3：厄拉多塞筛法
    西元前250年，希腊数学家厄拉多塞(Eeatosthese)想到了一个非常美妙的质数筛法，
    减少了逐一检查每个数的的步骤，可以比较简单的从一大堆数字之中，筛选出质数来，
    这方法被称作厄拉多塞筛法(Sieve of Eeatosthese)。
    
    具体操作：先将 2~n 的各个数放入表中，然后在2的上面画一个圆圈，然后划去2的其他倍数；
    第一个既未画圈又没有被划去的数是3，将它画圈，再划去3的其他倍数；
    现在既未画圈又没有被划去的第一个数 是5，将它画圈，并划去5的其他倍数……依次类推，
    一直到所有小于或等于 n 的各数都画了圈或划去为止。
    这时，表中画了圈的以及未划去的那些数正好就是小于 n 的素数。
    
    '''
    def countPrimes2(self, n: int) -> int:
        num = [True] * n
        res = 0
        for i in range(2, int(math.sqrt(n))+1):
            if num[i] == True:
                # k = 2
                k = i  # 对k = 2 的一种优化
                while k * i < n:
                    num[k * i] = False
                    k += 1
        for i in range(2, n):
            if num[i] == True:
                res += 1
        print(num)
        return res

if __name__=="__main__":
    s = Solution()
    print(s.countPrimes2(30))