class Solution:
    #法一：直接双重循环依次移动每一个元素,时间复杂度：O(kn),空间复杂度：O(1)

    def rotate(self, nums: 'List[int]', k: 'int') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        #先简化移动次数K
        k %= length
        for i in range(k):
            temp = nums[length-1]
            for j in range(length-1,0,-1):
                nums[j] = nums[j - 1]
            nums[0] = temp
        #print(nums)
    # 法二：翻转: 时间复杂度：O(n), 空间复杂度：O(1)
    def rotate2(self, nums: 'List[int]', k: 'int') -> 'None':
        length = len(nums)
        k %= length
        self.reverse(nums, 0, length - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, length - 1)
        #print(nums)
    def reverse(self,nums: 'List[int]', start: 'int',end: 'int'):
        while (start < end):
            nums[start], nums[end] = nums[end],nums[start]
            start += 1
            end -= 1
    #法三：循环交换  时间复杂度：O(n^2/k)  空间复杂度：O(1)
    def rotate3(self, nums: 'List[int]', k: 'int') -> 'None':
        length = len(nums)
        k %= length
        for start in range(0,len(nums),k):
            for i in range(0,k):
                nums[start + i], nums[len(nums)-k+i] = nums[len(nums)-k+i], nums[start +i]

            if k == 0 :break
            length -= k
            k %= length
        #print(nums)

if __name__=='__main__':
    s = Solution()
    nums = [1,2,3,4,5,6,7]
    k = 3
    s.rotate2(nums,k)