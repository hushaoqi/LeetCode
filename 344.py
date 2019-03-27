class Solution:
    def reverseString(self, s: 'List[str]') -> 'None':
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) > 0:
            pre, beh = 0, len(s)-1
            while pre < beh:
                s[pre], s[beh] = s[beh], s[pre]
                pre, beh = pre+1, beh-1

    def reverseString2(self, s: 'List[str]') -> 'None':
        # 这是Python中最简单的做法，但是似乎不符合题意中的返回值为None的条件
        return s[::-1]

if __name__=='__main__':
    s = Solution()
    string = ["h","e","l","l","o"]
    s.reverseString(string)
    print(string)