class Solution:
    def findKthLargest(self, nums: 'List[int]', k: int) -> int:
        # 类似冒泡排序，只不过进行K轮
        n = len(nums)
        for i in range(k):
            n -= 1
            for j in range(n):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums[-k]
    # 由于Python性能太慢，在极端情况下，运行超时
    def findKthLargest2(self, nums: 'List[int]', k: int) -> int:
        nums = sorted(nums)
        return nums[-k]
    # 由于只需要找出第K大，所以还是第一种方法的思路，我们并不需要将所有元素排序，而是选出K个大的数就行
    # 这里运用快速排序的思想

    def findKthLargest3(self, nums: 'List[int]', k: int) -> int:
        left = 0
        right = len(nums) - 1
        while True:
            pos = self.partition(nums, left, right)
            if pos == k - 1:
                return nums[pos]
            elif pos > k - 1:
                right = pos - 1
            else:
                left = pos + 1

    def partition(self, nums, left, right):
        pivot = nums[left]
        l = left + 1
        r = right
        while l <= r:
            if nums[l] < pivot and nums[r] > pivot:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            if nums[l] >= pivot:
                l += 1
            if nums[r] <= pivot:
                r -= 1
        nums[left], nums[r] = nums[r], nums[left]
        return r

if __name__=='__main__':
    s = Solution()
    nums = [3,2,3,1,2,4,5,5,6]
    k = 5
    print(s.findKthLargest3(nums, k))