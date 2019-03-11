class Solution:
    def findMaxConsecutiveOnes(self, nums: 'List[int]') -> 'int':
        maxOne = 0
        curOne = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                curOne += 1
            else:                   #遇到0，判断，重新计数
                maxOne = max(maxOne , curOne)
                curOne = 0
        maxOne = max(maxOne, curOne)#遍历结束，判断
        return maxOne

if __name__=='__main__':
    s = Solution()
    nums = [1,1,0,1,1,1]
    print(s.findMaxConsecutiveOnes(nums))
