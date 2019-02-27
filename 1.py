class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        n = len(nums)
        # 创建一个空字典
        d = {}
        for x in range(n):
            a = target - nums[x]
            # 字典d中存在nums[x]时
            if nums[x] in d:
                return [d[nums[x]], x]
            # 否则往字典增加键/值对
            else:
                d[a] = x
        # 边往字典增加键/值对，边与nums[x]进行对比


if __name__ == '__main__':
    s = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    sum_result = s.twoSum(nums,target)
    print(sum_result)
