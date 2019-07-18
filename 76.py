from collections import Counter
import sys
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        start = 0
        minLen = sys.maxsize
        t_table = {}
        s_table = {}
        sn = len(s)
        for pt in t:
            if pt not in t_table:
                t_table[pt] = 1
            else:
                t_table[pt] += 1
            s_table[pt] = 0  # 初始化s_table
        # print(t_table, s_table)
        left, right = 0, 0
        match = 0

        # 滑动窗口
        while right < sn:
            if s[right] in s_table:
                s_table[s[right]] += 1
                if s_table[s[right]] == t_table[s[right]]:
                    match += 1
            right += 1

            while match == len(t_table):  # 如果相等则包含T
                if right - left < minLen:
                    start = left
                    minLen = right - left

                if s[left] in t_table:
                    s_table[s[left]] -= 1
                    if s_table[s[left]] < t_table[s[left]]:
                        match -= 1
                left += 1
        if minLen != sys.maxsize:
            res = s[start:start + minLen]
        return res


    def minWindow2(self, s: str, t: str) -> str:

        if not t or not s:
            return ""

        # Dictionary which keeps a count of all the unique characters in t.
        dict_t = Counter(t)

        # Number of unique characters in t, which need to be present in the desired window.
        required = len(dict_t)

        # left and right pointer
        l, r = 0, 0

        # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency.
        # e.g. if t is "AABC" then the window must have two A's, one B and one C. Thus formed would be = 3 when all these conditions are met.
        formed = 0

        # Dictionary which keeps a count of all the unique characters in the current window.
        window_counts = {}

        # ans tuple of the form (window length, left, right)
        ans = float("inf"), None, None

        while r < len(s):

            # Add one character from the right to the window
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1

            # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            # Try and co***act the window till the point where it ceases to be 'desirable'.
            while l <= r and formed == required:
                character = s[l]

                # Save the smallest window until now.
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                # The character at the position pointed by the `left` pointer is no longer a part of the window.
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1

                # Move the left pointer ahead, this would help to look for a new window.
                l += 1

            # Keep expanding the window once we are done co***acting.
            r += 1
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]




if __name__== '__main__':
    solution = Solution()
    S = "ADOBECODEBANC"
    T = "ABC"
    print(solution.minWindow(S, T))