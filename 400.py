class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 当 N 很大的时候会超出内存限制
        if n < 1:
            return
        res = [str(i) for i in range(1, n+1)]
        # print(res)
        string = "".join(res)
        # print(string)
        res = list(string)
        # print(res)
        return res[n-1]

    '''
    当x=234时, 1-9是1位的， 10-99是2位的， 100-234是3位的
    
    则y = 3 * (234-99) + 2 * 90 + 1 * 9
    
    用k代表x的位数， 可以得到函数 y = k*(x-10^(k-1)-1) + (k-1)*9*10^(k-2) + (k-2)*9*10^(k-3) + ... + 9
    
    化简可得： y = k*x + k - 10^(k-1) - 10^(k-2) - ... - 10^0
    '''
    def findNthDigit2(self, n):
        """
        :type n: int
        :rtype: int
        """
        k = 0
        count = 0

        while count < n:
            k += 1
            count += k * 9 * 10 ** (k - 1)
        clip_num = n - count + k * 9 * 10 ** (k - 1)

        k_num = (clip_num - 1) // k
        k_end = (clip_num - 1) % k
        num = 10 ** (k - 1) + k_num

        return int(str(num)[k_end])

    def findNthDigit3(self, n):
        """
        :type n: int
        :rtype: int
        """

        def func(x):
            if x == 0: return 0
            a = len(str(x))
            return x * a + a - sum(10 ** i for i in range(a))

        if n < 1:
            return

        left = 0
        right = 2 ** 31
        target = n
        mid = None
        found = False
        while left < right - 1:
            mid = (left + right) // 2
            mid_val = func(mid)
            if mid_val > target:
                right = mid
            elif mid_val < target:
                left = mid
            else:
                found = True
                break
        if found:
            return str(mid)[-1]
        if func(mid) > target:
            right = mid
        offset = func(right) - n
        return str(right)[-1 - offset]

    def findNthDigit4(self, n: int) -> int:
        index = 0
        while n - (9 * (10 ** index) * (index + 1)) > 0:
            n = n - (9 * (10 ** index) * (index + 1))
            index += 1
        nums = (n // (index + 1)) + (10 ** index)
        n = n % (index + 1)
        if n == 0:
            n = index + 1
            nums -= 1
        indexI = index - n + 2
        return int((nums % (10 ** indexI)) // (10 ** (indexI - 1)))


if __name__=="__main__":
    s = Solution()
    print(s.findNthDigit2(10000000))