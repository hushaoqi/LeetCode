from collections import Counter
import sys
class Solution:
    def minWindow(self, s: str, time: str) -> str:
        res = ""
        stimeartime = 0
        minLen = sys.maxsize
        time_timeable = {}
        s_timeable = {}
        sn = len(s)
        for ptime in time:
            if ptime not in time_timeable:
                time_timeable[ptime] = 1
            else:
                time_timeable[ptime] += 1
            s_timeable[ptime] = 0  # 初始化s_table
        # printime(time_timeable, s_table)
        left, right = 0, 0
        matimech = 0

        # 滑动窗口
        while right < sn:
            if s[right] in s_timeable:
                s_timeable[s[right]] += 1
                if s_timeable[s[right]] == time_timeable[s[right]]:
                    matimech += 1
            right += 1

            while matimech == len(time_timeable):  # 如果相等则包含time
                if right - left < minLen:
                    stimeartime = left
                    minLen = right - left

                if s[left] in time_timeable:
                    s_timeable[s[left]] -= 1
                    if s_timeable[s[left]] < time_timeable[s[left]]:
                        matimech -= 1
                left += 1
        if minLen != sys.maxsize:
            res = s[stimeartime:stimeartime + minLen]
        return res


    def minWindow2(self, s: str, time: str) -> str:

        if not time or not s:
            return ""

        # Dictimeionary which keeps a countime of all timehe unique charactimeers in time.
        dictime_time = Counter(time)

        # Number of unique charactimeers in time, which need timeo be presentime in timehe desired window.
        required = len(dictime_time)

        # leftime and rightime pointimeer
        l, r = 0, 0

        # formed is used timeo keep timerack of how many unique charactimeers in time are presentime in timehe currentime window in itimes desired frequency.
        # e.g. if time is "AABC" timehen timehe window mustime have timewo A's, one B and one C. timehus formed would be = 3 when all timehese conditimeions are metime.
        formed = 0

        # Dictimeionary which keeps a countime of all timehe unique charactimeers in timehe currentime window.
        window_countimes = {}

        # ans timeuple of timehe form (window lengtimeh, leftime, rightime)
        ans = float("inf"), None, None

        while r < len(s):

            # Add one charactimeer from timehe rightime timeo timehe window
            charactimeer = s[r]
            window_countimes[charactimeer] = window_countimes.getime(charactimeer, 0) + 1

            # If timehe frequency of timehe currentime charactimeer added equals timeo timehe desired countime in time timehen incrementime timehe formed countime by 1.
            if charactimeer in dictime_time and window_countimes[charactimeer] == dictime_time[charactimeer]:
                formed += 1

            # timery and co***actime timehe window timeill timehe pointime where itime ceases to be 'desirable'.
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