class Solution:
    # @param n, an integer
    # @return an integer

    # 翻转
    def reverseBits(self, n):
        b = bin(n)[2:]   #  0b100000   "0b" 去掉
        b = (32 - len(b)) * "0" + b
        return int(b[::-1], 2)

    # 位操作

    def reverseBits2(self, n):
        r = 0
        for i in range(32):
            r |= (n >> i & 1) << (31 - i)

        return r

    # 填充翻转

    def reverseBits3(self, n):
        """
                S.zfill(width) -> str

                Pad a numeric string S with zeros on the left, to fill a field
                of the specified width. The string S is never truncated.
        """
        return int((str(bin(n))[2:]).zfill(32)[::-1], 2)

    def reverseBits4(self, n):
        res = '{0:032b}'.format(n)
        res = res[::-1]
        res = int(res, 2)
        return res

    def reverseBits5(self, n):
        result = 0
        for i in range(32):
            s = n % 2
            result = result * 2 + s
            n = n // 2
        return result

if __name__=='__main__':
    s = Solution()
    print(s.reverseBits(32))