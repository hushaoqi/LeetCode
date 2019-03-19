class Solution:
    def findLengthOfLCIS(self, nums: 'List[int]') -> 'int':
        longgest = 0
        if len(nums) <= 0:return 0
        if len(nums) == 1:return 1
        curlenth = 1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                curlenth += 1
            else:
                longgest = max(longgest, curlenth)
                curlenth = 1
        longgest = max(longgest, curlenth)
        return longgest

if __name__=='__main__':
    s = Solution()
    #nums = [2, 2, 2, 2, 2]
    #nums = [1,3,5,4,7]
    nums = [1,3,5,7]
    print(s.findLengthOfLCIS(nums))
