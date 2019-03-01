#首先题目理解不要错：否存在两个不同的索引 i 和 j，使得 nums [i] == nums [j]， i 和 j 的差的绝对值最大为 k   ——>  指的是绝对值不超过K（注意“存在”）
class Solution:
    #字典法
    def containsNearbyDuplicate(self, nums: 'List[int]', k: 'int') -> 'bool':
        dic = {} #创建空字典
        for i in range(0,len(nums)):
            if nums[i] not in dic:  #如果元素不在字典中，则添加
                dic[nums[i]] = i
                continue
            if (i - dic[nums[i]]) <= k: return True  #如果元素在字典中，则判断索引差值是否 <= k，若是，说明存在
            else:dic[nums[i]] = i     #若不小于k，则更新索引
        return False
'''代码优化
        dic = {} #创建空字典
        for i in range(len(nums)):
            if nums[i] in dic:
                if i-dic[nums[i]] <= k:
                    return True
            dic[nums[i]] = i
        return False
'''

if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3,1]
    k = 3
    print(s.containsNearbyDuplicate(nums,k))