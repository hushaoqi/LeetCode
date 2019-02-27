class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> 'int':
        if len(nums) == 0: return 0
        i = 0
        for j in range(1,len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1

if __name__ == '__main__':
    s = Solution()
    nums = [0, 0, 0, 0, 1, 2, 2, 3, 3, 4]
    print(s.removeDuplicates(nums))
    print(nums)
