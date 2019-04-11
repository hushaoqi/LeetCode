class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 对于Python就有点麻烦了。因为Python的整数不是固定的32位，所以需要做一些特殊的处理

        sum = (a ^ b)
                        # 异或这里可看做是相加但是不显现进位，比如5 ^ 3
                        # 0 1 0 1
                        # 0 0 1 1
                        #--------
                        # 0 1 1 0
                        # 上面的如果看成传统的加法，不就是1 + 1 = 2，进1得0，
                        # 但是这里没有显示进位出来，仅是相加，0 + 1或者是1 + 0都不用进位
        carry = (a & b) << 1
                        # 相与为了让进位显现出来，比如5 & 3
                        # 0 1 0 1
                        # 0 0 1 1
                        #--------
                        # 0 0 0 1
                        # 上面的最低位1和1相与得1，而在二进制加法中，这里1 + 1
                        # 也应该是要进位的，所以刚好吻合，但是这个进位1应该要再往前一位，所以左移一位
        if carry != 0:

                        # 经过上面这两步，如果进位不等于0，那么就是说还要把进位给加上去，
                        # 所以用了尾递归，一直递归到进位是0。
            return self.getSum(sum, carry)
                        # 最高位为1即负数左移会报错, 使carry最高位永远为0
        return sum

    def getSum2(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MAX = 0x7fffffff
        # MIN = 0x80000000
        mask = 0xFFFFFFFF
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1)
        return a if a <= MAX else ~(a ^ mask)

    def getSum3(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while b != 0:
            carry = a & b
            a = (a ^ b) % 0x100000000
            b = (carry << 1) % 0x100000000
        return a if a <= 0x7FFFFFFF else a | (~0x100000000 + 1)

if __name__=='__main__':
    s = Solution()
    print(s.getSum(-1, 1))
