class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        b = str(bin(n)[2:])
        return b.count('1')

    def hammingWeight2(self, n):
        """
        :type n: int
        :rtype: int
        """
        temp = n
        res = 0
        while temp:
            res += temp % 2
            temp = temp // 2
        return res

    def hammingWeight3(self, n):

        return bin(n).count('1')

    def hammingWeight4(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            if n & 1 == 1:
                count += 1
            n >>= 1
        return count

if __name__ == '__main__':
    s = Solution()
    print(s.hammingWeight3(31))