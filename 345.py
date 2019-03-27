class Solution:
    def reverseVowels(self, s: str) -> str:
        list_s = list(s)
        # 用集合比列表速度快
        algha = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        if len(list_s) > 0:
            pre, beh = 0, len(list_s)-1
            while pre < beh:
                if list_s[pre] in algha and list_s[beh] in algha:
                    list_s[pre], list_s[beh] = list_s[beh], list_s[pre]
                    pre, beh = pre+1, beh-1

                if list_s[pre] not in algha:
                    pre += 1
                if list_s[beh] not in algha:
                    beh -= 1
        new_s = ''
        return new_s.join(list_s)

if __name__=='__main__':
    s = Solution()
    string = "leetcode"
    print(s.reverseVowels(string))