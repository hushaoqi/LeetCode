class Solution:
    def arrayPairSum(self, nums: 'List[int]') -> 'int':
        nums = sorted(nums)
        maxSum = 0
        for i in range(0,len(nums)-1,2):
            maxSum += min(nums[i] ,nums[i+1])
        return maxSum
if __name__ == '__main__':
    s = Solution()
    nums = [1,4,3,2]
    print(s.arrayPairSum(nums))