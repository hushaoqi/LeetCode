import collections
class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #统计数组中每个数字的个数
        #如果k为0且该数字出现的次数大于1，则结果count自增1；
        #如果k不为0，且用当前数字加上k后得到的新数字也在数组中存在，则结果count自增1
        c = collections.Counter(nums)
        count = 0
        if k < 0:
            return 0
        if k == 0:
            for item in c.keys():
                if c[item] > 1:
                    count += 1
            return count
        else:
            for item in c.keys():
                if item + k in c:
                    count += 1
            return count

    #使用了双指针，需要给数组排序，节省了空间的同时牺牲了时间。
    # 我们遍历排序后的数组，然后在当前数字之后找第一个和当前数之差不小于k的数字，
    # 若这个数字和当前数字之差正好为k，那么结果count自增1，然后遍历后面的数字去掉重复数字
    def findPairs2(self, nums, k):
        nums = sorted(nums)
        count = 0
        i,j = 0,0
        #range()是一个迭代器，它只会输出信息，而不能修改迭代器的内容
        while i < len(nums):#for i in range(len(nums)):  Python一大坑，循环中对循环变量的修改并不会改变i的迭代
            j = max(j,i + 1)
            while(j < len(nums) and nums[j] - nums[i] < k): j += 1
            if (j < len(nums) and nums[j] - nums[i] == k): count += 1
            while(i < (len(nums)-1) and nums[i] == nums[i+1]) : i += 1
            i += 1
        return count
if __name__ == '__main__':
    s = Solution()
    nums = [3,1,4,1,5]
    k = 2
    print(s.findPairs2(nums,k))