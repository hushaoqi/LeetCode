class Solution:
    #法一：转换为字符串，翻转比较
    def isPalindrome(self, x: 'int') -> 'bool':
        num = str(x)
        trans = num[::-1]
        # print(num)
        # print(trans)
        return num == trans
    #法二：翻转一半数字，所有负数都不是回文数,被10整除的非零数不是回文数
    #如何知道反转数字的位数已经达到原始数字位数的一半？
    #我们将原始数字除以 10，然后给反转后的数字乘上 10，
    # 所以，当原始数字小于反转后的数字时，就意味着我们已经处理了一半位数的数字。
    def isPalindrome2(self, x: 'int') -> 'bool':
        if ((x < 0) or (x % 10 == 0 and x != 0)) : return  False

        reverse = 0
        while (x > reverse):
            reverse = reverse * 10 + x % 10
            x /= 10
        #当数字长度为奇数时，我们可以通过 revertedNumber/10 去除处于中位的数字。
        #由于处于中位的数字不影响回文（它总是与自己相等），所以我们可以简单地将其去除。
        return (x == reverse) or (x == reverse / 10)


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(12221))
    print(s.isPalindrome2(121))
