class Solution:
    #复制数组，排序，对比数组，不符这说明需要排序
    def findUnsortedSua_spaceay(self, nums: 'List[int]') -> 'int':
        if len(nums)<2:
            return 0
        temp = sorted(nums)
        start = 0
        end = len(temp) - 1
        while start < len(temp):
            if temp[start] == nums[start]:start += 1
            else:break
        while end > 0:
            if temp[end] == nums[end]:end -= 1
            else:break
        if end > start:
            return end - start + 1
        else:return 0
    #遍历找最小，最大
    # 思路是
    # 从左往右找到正确顺序的一边，end右边
    # 从右向左找到正确顺序的一边，start左边
    # O(n)的时间复杂度  O(1)的空间复杂度
    def findUnsortedSua_spaceay2(self, nums: 'List[int]') -> 'int':
        if len(nums) < 2:
            return 0
        start = 0
        end = -1
        max = nums[0]
        min = nums[len(nums) - 1]
        for i in range(1,len(nums)):
            #从左向右依次比较，如果下标为i的元素小于max，表示从i开始向左都需要调整，i右边不需要调整
            if max > nums[i] : end = i
            else:max = nums[i]
            #从右向左依次比较，如果下标为i的元素大于min，表示从i开始向右都需要调整，i左边不需要调整
            if min < nums[len(nums) - 1 - i]:
                start = len(nums) - 1 - i
            else:min = nums[len(nums) - 1 - i]
        return end - start + 1

if __name__ == '__main__':
    s = Solution()
    nums = [2, 6, 4, 8, 10, 9, 15]
    print(s.findUnsortedSua_spaceay2(nums))