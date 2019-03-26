class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # "a "之前以为后面有空格 a就不算最后一个单词
        tail = len(s) - 1
        while tail >= 0 and s[tail] == ' ':
            tail -= 1
        # 处理掉尾空格
        s = s[:tail+1]
        try:
            return s[::-1].index(' ')
        except:
            return len(s)

    def lengthOfLastWord2(self, s: str) -> int:
        cnt, tail = 0, len(s) - 1
        while tail >= 0 and s[tail] == ' ':
            tail -= 1
        while tail >= 0 and s[tail] != ' ':
            cnt += 1
            tail -= 1
        return cnt

if __name__ == '__main__':
    ss = Solution()
    string = "Hello World "
    print(ss.lengthOfLastWord(string))