class Solution:
    def threeSumClosest(self, nums: 'List[int]', target: int) -> int:
        n = len(nums)
        nums.sort()
        min_sum = sum(nums[0:3])
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]: # 判断固定的数是否重复
                continue
            left = i + 1
            right = n - 1
            while left < right:
                cur = nums[i] + nums[left] + nums[right]
                if abs(target - cur) < abs(target - min_sum):
                    min_sum = cur

                if cur > target:
                    right -= 1
                elif cur < target:
                    left += 1
                else:
                    return target

        return min_sum

if __name__=='__main__':
    s = Solution()
    nums = [-1, 2, 1, -4]
    target = 1
    print(s.threeSumClosest(nums, target))