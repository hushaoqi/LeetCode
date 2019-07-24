class Solution:
    def firstUniqChar(self, s: str) -> int:
        # 题目中表明只有小写字母，可用字典保存字母的数目,再次遍历
        table = {}
        for ss in s:
            if ss in table:
                table[ss] += 1
            else:
                table[ss] = 1
        for i in range(len(s)):
            if table[s[i]] == 1:
                return i
        return -1

if __name__== '__main__':
    so = Solution()
    s = "leetcode"
    print(so.firstUniqChar(s))