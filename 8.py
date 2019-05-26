import sys
class Solution:
    def myAtoi(self, str: str) -> int:
        MAXSIZE = 2147483647
        MINSIZE = -2147483648
        # sys.maxsize = 9223372036854775807 Python中不存在最大int
        if len(str) == 0:  # 判断字符串是否为空
            return 0
        while len(str) != 0 and str[0] == ' ':  # 丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。
            str = str[1:]
        sign = 1
        if len(str) != 0 and (str[0] == '+' or str[0] == '-'):  # 寻找到的第一个非空字符为正或者负号时
            sign = 1 if str[0] == '+' else -1
            str = str[1:]

        if len(str) == 0:  # 判断剩余字符串是否为空
            return 0
        base = 0
        i = 0
        n = len(str)
        while i < n and ord('0') <= ord(str[i]) <= ord('9'):
            # 32位int的最大值 2147483647 的最后一位
            # 即 7 == INT_MAX % 10
            if base > MAXSIZE / 10 or (base == MAXSIZE / 10 and str[i] - '0' > 7):
                return MAXSIZE if sign == 1 else MINSIZE

            base = 10 * base + (int(str[i]))
            i += 1
        result = base * sign
        if (result < MINSIZE):return MINSIZE
        if (result > MAXSIZE):return MAXSIZE
        return result

if __name__=='__main__':
    s = Solution()
    print(s.myAtoi(str="   "))
