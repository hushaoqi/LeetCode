class Solution:
    def removeElement(self, nums: 'List[int]', val: 'int') -> 'int':
        if len(nums) == 0: return 0
        i = 0
        for j in range(0,len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i+=1
        return i
#当我们遇到 nums[i] = valnums[i]=val 时，我们可以将当前元素与最后一个元素进行交换，并释放最后一个元素。这实际上使数组的大小减少了 1。
#请注意，被交换的最后一个元素可能是您想要移除的值。但是不要担心，在下一次迭代中，我们仍然会检查这个元素。

    def removeElement2(self, nums: 'List[int]', val: 'int') -> 'int':
        i = 0
        length = len(nums)
        while i < length:
            if nums[i] == val:
                nums[i] = nums[length - 1]
                #减小数组大小
                length -= 1
            else: i+=1
        return length

if __name__ == '__main__':
    s = Solution()
    nums = [0, 0, 0, 0, 1, 2, 2, 3, 3, 4]
    print(s.removeElement(nums,0))
    print(nums)
    # print(s.removeElement2(nums,3))
    # print(nums)