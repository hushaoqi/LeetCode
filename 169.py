class Solution:
    def majorityElement(self, nums: 'List[int]') -> 'int':
        count = {}
        for num in nums:
            if num in count:
                times = count[num] + 1
                count[num] = times
            else:
                count[num] = 1
        MAX = 0
        for num in count:
            if count[num] > MAX:
                MAX = count[num]
        for k, v in count.items():
            if v == MAX:
                return k

if __name__=='__main__':
    s = Solution()
    nums = [2,2,1,1,1,2,2]
    print(s.majorityElement(nums))