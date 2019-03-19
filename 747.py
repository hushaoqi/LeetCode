import sys
class Solution:
    def dominantIndex(self, nums: 'List[int]') -> 'int':
        max1, max2= - sys.maxsize,- sys.maxsize
        index = -1
        for i in range(len(nums)):
            if max1 < nums[i]:
                index = i
                max2 = max1
                max1 = nums[i]
            if max2 < nums[i] < max1:
                max2 = nums[i]
        #if max1 >= max2 * 2 and index != -1:  #这里如果不用乘法用减法,会不会效率更高
        if max1 - max2 >= max2 and index != -1:
            return index
        else:
            return -1
if __name__=='__main__':
    s = Solution()
    test = ([1],[0,0,3,2],[1, 2, 3],[1,2,4,-3,6],[1, 7, 3, 6, 5, 6],[1,2,3,4,5,6],[-1, -1, -1, -1, -1, 0],[-1, -1, -1, -1, 0, -1],[-1, -1, -1, -1, 1, -1],[-1,-1,-1,-1,1,0])
    for nums in test:
        print(s.dominantIndex(nums),end=' ')