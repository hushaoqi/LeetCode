class Solution:
    #转化为每个元素均出现两次。找出那个只出现了一次的元素即可：时间复杂度为：O(n) ,空间复杂度为O(n)
    def missingNumber(self, nums: 'List[int]') -> 'int':
        nums += range(0,len(nums)+1)
        #print(nums)
        num = nums[0]
        for i in range(1,len(nums)):
             num ^= nums[i]
        return num
    #优化空间复杂度：O(1)
    def missingNumber2(self, nums: 'List[int]') -> 'int':
        num = len(nums)
        for i in range(0,len(nums)):
            num ^= nums[i]
            num ^= i
        return num

    #排序，依次与index相比，不等，则输出
    def missingNumber3(self, nums: 'List[int]') -> 'int':
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] != i: return i
        return i+1
    #数学解法，两和之差：数组和 与 1到n项的数列和 对比，相差的数就是缺的这个数（优势：Python中求和int不会越界）
    #若换为其他语言，可以遍历数组，加一个元素的同时减一个index，防止越界
    def missingNumber4(self, nums: 'List[int]') -> 'int':
        n = len(nums)
        return int(n*(n+1)/2 - sum(nums))
if __name__ == '__main__':
    s = Solution()
    nums = [9,6,4,2,3,5,7,0,1]
    print(s.missingNumber4(nums))