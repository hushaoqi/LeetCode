class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        b = str(bin(num)[2:])
        print(b)
        return b.count('1') == 1 and b.count('0') == (len(b) - 1) and b.count('0') % 2 == 0

    def isPowerOfFour2(self, num):
        """
        :type num: int
        :rtype: bool
        """
        flag = True
        if num == 0:
            flag = False
        while flag == True and num != 1:
            if num % 4 != 0:
                flag = False
            num = num / 4

        return flag

    def isPowerOfFour3(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num & (num - 1) != 0:
            return False
        return (num & 0x55555555) != 0

    def isPowerOfFour4(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        elif num == 1:
            return True
        elif num % 4:
            return False
        else:
            return self.isPowerOfFour(int(num / 4))

    def isPowerOfFour5(self, num):
        """
        :type num: int
        :rtype: bool
        """
        import math
        return num > 0 and 4 ** round(math.log(num, 4)) == num

if __name__=='__main__':
    s = Solution()
    print(s.isPowerOfFour(2 ** 3))