class Solution:
    def reverse(self, x: 'int') -> 'int':
        if x < 0:
            flag = -1
        else:
            flag = 1
        revx = int(str(abs(x))[::-1])
        #第一个冒号两侧的数字是指截取字符串的范围,省略是完全截取原来的字符串.
        #第二个冒号后面是指截取的步长, 比如2是指每2个截取一个. -1指从倒数开始截取.
        if revx > pow(2,31):
            return 0
        else:
            return revx * flag

if __name__ == "__main__":
    s = Solution()
    reverse_INt = s.reverse(-120)
    print(reverse_INt)