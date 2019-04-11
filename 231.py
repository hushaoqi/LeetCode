import math
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        b = str(bin(n)[2:])
        return b.count('1') == 1 and b.count('0') == (len(b) - 1)

    def isPowerOfTwo2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False

        k = int(math.log(n, 2))

        return 2 ** k == n

    def isPowerOfTwo3(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0: return False
        n = n & (n - 1)
        if n == 0:
            return True
        return False
    #   return n > 0 and not n & (n - 1)
    
if __name__=='__main__':
    s = Solution()
    print(s.isPowerOfTwo(16))