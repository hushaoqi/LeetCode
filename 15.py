class Solution:
    # 思路: 先排序, 然后规定第一个数不动, 后面双指针法求和.并且去重
    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        n = len(nums)
        res = []
        if n < 3:
            return res
        nums.sort()
        # print(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:  # 判断固定的数是否重复
                continue
            left = i + 1
            right = n - 1
            while left < right:
                cur = nums[i] + nums[left] + nums[right]
                if cur == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:  # 判断是否重复
                        left += 1
                    while right < left and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif cur > 0:
                    right -= 1
                else:
                    left += 1
        return res

if __name__ == '__main__':
    s = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print(s.threeSum(nums))
