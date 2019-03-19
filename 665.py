class Solution:
    def checkPossibility(self, nums: 'List[int]') -> 'bool':
        count = 1
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if count == 0:
                    return False
                if i == 1 or nums[i] >= nums[i - 2]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]
                count -= 1
        return True
if __name__ == '__main__':
    s = Solution()
    # nums = [3, 4, 2, 3]
    # nums = [4, 2, 3]
    nums = [-1, 4, 2, 3]
    print(s.checkPossibility(nums))
