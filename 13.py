class Solution:
    def romanToInt(self, s: 'str') -> 'int':
        # 用字典存储罗马数字映射表，从后往前遍历，若当前值大于等于后面的值，则加；若当前值小于后面的值，则减
        num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        Sum = 0
        if len(s) == 0: return 0
        if len(s) == 1: return num[s]
        Sum += num[s[-1]]
        for i in range(len(s)-2, -1, -1):
            if num[s[i]] >= num[s[i+1]]:
                Sum += num[s[i]]
            else:
                Sum -= num[s[i]]
        return Sum
if __name__ == '__main__':
    s = Solution()
    ss = 'MCMXCIV'
    print(s.romanToInt(ss))

