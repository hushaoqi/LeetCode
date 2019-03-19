class Solution:
    def pivotIndex(self, nums: 'List[int]') -> 'int':
        for i in range(len(nums)):
            if sum(nums[0:i]) == sum(nums[i+1:len(nums)]): return i
        return -1
    #加和 优化
    def pivotIndex2(self, nums: 'List[int]') -> 'int':
        Sum = sum(nums)
        curSum = 0
        for i in range(len(nums)):
            if Sum - nums[i] == 2 * curSum: return i
            curSum += nums[i]
        return -1
    def pivotIndex3(self, nums: 'List[int]') -> 'int':
        Sum = sum(nums)
        curSum = 0
        for i, num in enumerate(nums):
            if curSum * 2 == Sum - num:
                return i
            curSum += num
        return -1
if __name__=='__main__':
    s = Solution()
    test = ([1, 2, 3],[1,2,4,-3,6],[1, 7, 3, 6, 5, 6],[1,2,3,4,5,6],[-1, -1, -1, -1, -1, 0],[-1, -1, -1, -1, 0, -1],[-1, -1, -1, -1, 1, -1],[-1,-1,-1,-1,1,0])
    for nums in test:
        print(s.pivotIndex3(nums),end=' ')