class Solution:
    def findTheDifference(self, s: 'str', t: 'str') -> 'str':
        # 将所给的字符串转换为字符数组，求字符数组的int和，作差，再转回char，返回
        # 数字与自身异或结果为0
        ret = 0
        for c in s + t:
            ret ^= ord(c)
        return chr(ret)

    # 解1: s，t分别排序好，用指针从头开始逐一比对，发现不同即返回
    def findTheDifference2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s = sorted(s)
        t = sorted(t)
        for i in range(len(s)):
            if s[i] != t[i]:
                return t[i]
        return t[-1]

    # 解2: 用dict，分别把s，t存成dict，若t中有key是s中没有的，或者相同的key，t的value比s大，那么返回该key
    def findTheDifference3(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        a = {}
        b = {}
        for i in s:
            if i in a:
                a[i] += 1
            else:
                a[i] = 1
        for i in t:
            if i in b:
                b[i] += 1
            else:
                b[i] = 1
        for i in b:
            if i not in a or b[i] != a[i]:
                return i
    # 剔除法
    def findTheDifference4(self, s: str, t: str) -> str:
        s = list(s)
        t = list(t)

        for i in s:
            del t[t.index(i)]

        return t[0]

if __name__=='__main__':
    S = Solution()
    s = "abcd"
    t = "cabed"
    print(S.findTheDifference2(s, t))

