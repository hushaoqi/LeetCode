import sys
import heapq
class Solution:
    # max（找出3个最大的数积，找出一个最大的和两个最小的积）
    # 方法一：直接排序
    def maximumProduct(self, nums: 'List[int]') -> 'int':
        nums = sorted(nums)
        length = len(nums)
        return max(nums[0]*nums[1]*nums[length-1],nums[length-1]*nums[length-2]*nums[length-3])
    # 方法二：找到需要的五个数即可
    def maximumProduct2(self, nums: 'List[int]') -> 'int':
        max1, max2, max3 = -sys.maxsize, -sys.maxsize, -sys.maxsize
        min1, min2 = sys.maxsize, sys.maxsize
        for num in nums:
            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num
            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num
        return max(min1*min2*max1, max1*max2*max3)
    # 神操作
    def maximumProduct3(self, nums: 'List[int]') -> 'int':
        l = heapq.nlargest(3, nums)
        s = heapq.nsmallest(2, nums)
        return max(l[0] * l[1] * l[2], l[0] * s[0] * s[1])
if __name__=='__main__':
    s = Solution()
    nums = [-1, 0, -3, 4]
    print(s.maximumProduct3(nums))
