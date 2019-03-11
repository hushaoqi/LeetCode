import sys
class Solution:
    def thirdMax(self, nums: 'List[int]') -> 'int':
        if(len(nums)<3):return max(nums)
        else:
            max1,max2,max3 = -sys.maxsize,-sys.maxsize,-sys.maxsize
            for i in range(len(nums)):
                if (nums[i] > max1):  #替换最大，第二大，第三大
                    max3 = max2
                    max2 = max1
                    max1 = nums[i]
                    continue
                elif(nums[i] > max2 and nums[i] < max1):  #替换第二大，第三大
                    max3 = max2
                    max2 = nums[i]
                    continue
                elif(nums[i] > max3 and nums[i] < max2):  #替换第三大
                    max3 = nums[i]
                    continue
            if (max3 in nums):  #判断是否存在第三大
                return max3
            else:               #不存在第三大
                return max1

if __name__=='__main__':
    s = Solution()
    nums = [1,2,2,3333,2,2]
    print(s.thirdMax(nums))
