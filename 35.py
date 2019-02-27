class Solution:
    def searchInsert(self, nums: 'List[int]', target: 'int') -> 'int':
        i= len(nums)-1
        while i >= 0:
            #如果存在target就返回当前坐标
            if nums[i] == target : return i
            #如果大于就继续遍历
            if nums[i] > target : i -= 1
            #如果小于就返回上一个下标
            if nums[i] < target : return i+1

    def searchInsert2(self, nums: 'List[int]', target: 'int') -> 'int':
        low = 0
        high = len(nums) - 1
        mid = (low+high)//2
        while low < high:
            if target == nums[mid]:return mid
            if target < nums[mid] :
                high = mid
                mid = (low + high) // 2
            if target > nums[mid]:
                low = mid + 1
                mid = (low + high) // 2
        #注意使用二分查找，出现超出数组界外的情况，需要加一
        if target > nums[high]: return  high + 1
        else:return high
if __name__ == '__main__':
    s = Solution()
    nums = [1, 3, 5, 6]
    val = 9
    print(s.searchInsert2(nums,val))
