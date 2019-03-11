class Solution:
    # 滑动窗口法
    def findMaxAverage(self, nums: 'List[int]', k: 'int') -> 'float':
        SUM = sum(nums[0:k])
        res = SUM
        for i in range(k,len(nums)):
            SUM += (nums[i] - nums[i - k])
            res = max(res,SUM)
        return res / k
if __name__ == '__main__':
    s = Solution()
    nums = [1,12,-5,-6,50,3]
    k = 4
    print(s.findMaxAverage(nums,k))