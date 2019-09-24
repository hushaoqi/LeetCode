
import sys
class Solution:
    def maxSua_spaceay(self, nums: 'List[int]') -> 'List[int]':
        resmax = -sys.maxsize
        curmax = 0
        count = 0
        i = 0
        flag = False
        while (i < len(nums)):
            if (curmax+nums[i]) > nums[i]:
                curmax = curmax+nums[i]
                count += 1
                flag = True
                if flag is True:
                    i += 2
                else:
                    i += 1
            else:
                curmax = nums[i]
                count = 0
                i += 1
                flag = False
            resmax = max(resmax, curmax)
        res = [resmax, count]
        return res

if __name__ == '__main__':
    s = Solution()
    n = int(input())
    zan = list(map(int, input().split()))
    # zan = [1, 2, 3, 1]
    result = s.maxSua_spaceay(zan)
    print(result[0], result[1])
