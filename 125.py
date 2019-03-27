import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = []
        for ss in s:
            if '0' <= ss <= '9' or 'a' <= ss <= 'z':
                new_str.append(ss)
            if 'A' <= ss <= 'Z':
                new_str.append(chr(ord('a') + ord(ss) - ord('A')))
        print(new_str)
        return new_str == new_str[::-1]

    # import re ,使用正则表达式筛选过滤

    def isPalindrome2(self, s: str) -> bool:
        alphanumeric = re.sub("[^A-Za-z0-9]+", "", s).lower()
        #正则匹配
        print(alphanumeric)
        return alphanumeric == alphanumeric[::-1]

    # 过滤除数字字母之外的所有字符，将其替换为’‘
    def isPalindrome3(self, s: str) -> bool:
        s = s.lower()
        for i in " ,:.?!@#-+=%^&*\"\';\(\)`":
            s = s.replace(i, '')
        return s == s[::-1]

    # 提取字母数字，然后使用前后双指针遍历
    def isPalindrome4(self, s: 'str') -> 'bool':
        s = [c for c in s if c.isalpha() or c.isdigit()]
        if len(s) <= 1:
            return True
        i, j = 0, len(s) - 1
        while i < j:
            if s[i].lower() != s[j].lower():
                return False
            i, j = i + 1, j - 1
        return True

    # 使用filter
    def isPalindrome5(self, s: 'str') -> 'bool':
        if not len(s):
            return True
        s = "".join(filter(str.isalnum, s)).lower()
        return s == s[::-1]
if __name__=='__main__':
    s = Solution()
    string = "A man, a plan, a canal: Panama"
    print(s.isPalindrome2(string))