import sys
class Solution:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        resmax = -sys.maxsize
        curmax = 0
        start = 0
        end = 0
        i = 0
        while (i < len(nums)):
            curmax = max(curmax+nums[i],nums[i])
            # if (nums[i] >= curmax): start = i
            # if (curmax >= resmax): end = i
            resmax = max(resmax,curmax)
            i += 1
        # for k in range(start,end+1):
        #     print(nums[k],end=' ')
        return resmax

if __name__ == '__main__':
    s = Solution()
    nums =  [-2,1,-3,4,-1,2,1,-5,4]
    print(s.maxSubArray(nums))
