class Solution:
    def strStr(self, haystack: 'str', needle: 'str') -> 'int':
        # 当needle是空字符串时我们应当返回0 。这与C语言的strstr()以及Java的indexOf()定义相符
        if len(needle) == 0 :return 0
        # 不存在满足条件的子串
        if len(needle) > len(haystack) :return -1
        # 遍历比对
        for h in range(len(haystack) - len(needle) + 1):
            flag = True
            for n in range(len(needle)):
                if needle[n] != haystack[h+n]:
                    flag = False
                    break
            if flag : return h
        return -1

    # 使用内置函数
    def strStr2(self, haystack: 'str', needle: 'str') -> 'int':
        if needle not in haystack:
            return -1
        return haystack.index(needle)

if __name__=='__main__':
    s = Solution()
    print(s.strStr(haystack="mississippi", needle="mississippi"))

