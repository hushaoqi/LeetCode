class Solution:
    '''
    将所有的数置为相反数。那么，出现正数的位置即为消失的数字。比如，[4,3,2,7,8,2,3,1]
    重置后将为[-4,-3,-2,-7,8,2,-3,-1]
    '''
    def findDisappearedNumbers(self, nums: 'List[int]') -> 'List[int]':
        for i in range(len(nums)):
            nums[abs(nums[i]) - 1] = - abs(nums[abs(nums[i])- 1])
        res = []
        for j in range(len(nums)):
            if(nums[j] > 0):
                res.append(j+1)
        return res
    #Python中集合法
    def findDisappearedNumbers2(self, nums: 'List[int]') -> 'List[int]':
        res = set(range(1,len(nums)+1))
        res = res.difference(nums) #求差集
        return list(res)
    #简化代码：
    #return list(set(range(1,len(nums)+1)).difference(nums))
    #或
    #return list({i for i in range(1, len(nums) + 1)} - set(nums))


    #hash表（字典）不满足空间复杂度要求，还是集合的思想
    def findDisappearedNumbers3(self, nums: 'List[int]') -> 'List[int]':
        d = {}
        res = []
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]= i+1
        for i in range(1,len(nums)+1):
            if i not in d:
                res.append(i)
        return res

if __name__=='__main__':
    s = Solution()
    nums = [4,3,2,7,8,2,3,1]
    print(s.findDisappearedNumbers3(nums))
