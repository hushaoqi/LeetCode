class Solution:
    # 排序，判断是否存在相邻元素相等
    def containsDuplicate(self, nums: 'List[int]') -> 'bool':
        nums = sorted(nums)
        for i in range(0,len(nums)-1):
            if nums[i] == nums[i + 1]:return True
        return False
    # python利用set()一句话解决：#return len(set(nums)) < len(nums)

    def containsDuplicate2(self, nums: 'List[int]') -> 'bool':
        Numset = set()
        for i in range(0,len(nums)):
            Numset.add(nums[i])
        if len(Numset) < len(nums):return True
        else:return False
    #一句话解决：#return len(set(nums)) < len(nums)
    def containsDuplicate3(self, nums: 'List[int]') -> 'bool':
        return len(set(nums)) < len(nums)
if __name__=='__main__':
    s = Solution()
    nums = [1,1,1,3,3,4,3,2,4,2]
    print(s.containsDuplicate3(nums))
