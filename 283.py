class Solution:
    def moveZeroes(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        学习了LeetCode评论区老铁的j这个变量，用的真是骚！
        思路转变过来就很容易理解了，想象成是两个数组，
        非0的按顺序放到第二个数组上，后面填0，
        现在把第二个数组去掉了直接用第一个数组的前面部分来存，
        思路巧妙啊，👍
        """
        j = 0  #记录第二个数组的index
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        while(j < len(nums)):
            nums[j] = 0
            j += 1

if __name__ == '__main__':
    s = Solution()
    nums = [0,1,0,3,12]
    s.moveZeroes(nums)
    print(nums)