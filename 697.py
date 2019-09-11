import sys
class Solution:
    def findShortestSua_spaceay(self, nums: 'List[int]') -> 'int':
        # 统计每个num的次数
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        #找到度
        degree = max(dic.values())
        # 找到众数
        mode = []
        for key, value in dic.items():
            if value == degree:
                mode.append(key)
        # 找每个众数的首尾index,取最短
        max_len = len(nums)
        for m in mode:
            temp_len = (len(nums) - nums[::-1].index(m)) - nums.index(m)
            #print(m,':', nums.index(m),',', len(nums)-nums[::-1].index(m)-1)
            max_len = min(temp_len, max_len)
        return max_len

    def findShortestSua_spaceay2(self, nums: 'List[int]') -> 'int':
        max_len = sys.maxsize
        degree = 0
        dic = {}
        startIdx = {}
        for i in range(len(nums)):
            if nums[i] in dic:     # 统计每个num的次数
                dic[nums[i]] += 1
            else:
                dic[nums[i]] = 1
            if nums[i] not in startIdx:  # 统计每个num 第一次出现的位置
                startIdx[nums[i]] = i
            if dic[nums[i]] == degree:    # 如果num次数等于度数，则取最短子数组长度
                max_len = min(max_len, i-startIdx[nums[i]]+1)
            elif dic[nums[i]] > degree:   # 如果num次数大于当前度数，则更新数组的度
                max_len = i - startIdx[nums[i]] + 1
                degree = dic[nums[i]]
        return max_len
if __name__ == '__main__':
    s = Solution()
    # nums = [2, 2, 2, 2, 2]
    # nums = [1,3,5,4,7]
    nums = [1, 2, 2, 3, 1]
    print(s.findShortestSua_spaceay2(nums))