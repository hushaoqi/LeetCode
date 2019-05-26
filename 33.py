class Solution:
    def search(self, nums: 'List[int]', target: int) -> int:
        length = len(nums)
        if length == 0:
            return -1
        if length == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        rot = length   # 如果没有旋转

        for i in range(length - 1):
            if nums[i] > nums[i + 1]:
                rot = i + 1
                break
        # 如果旋转了，找到旋转分割点
        front = nums[:rot]
        front_result, behind_result = -1, -1
        if len(front) != 0:
            front_result = self.binary_search(front, target)
        behind = nums[rot:]
        if len(behind) != 0:
            behind_result = self.binary_search(behind, target)
            if behind_result != -1:
                behind_result = rot + behind_result

        if front_result == -1 and behind_result == -1:
            return -1
        elif front_result != -1:
            return front_result
        else:
            return behind_result



    def binary_search(self, arr: 'List[int]', target: int) ->int:
        if len(arr) == 0:
            return -1
        low = 0
        high = len(arr)
        mid = (low + high) // 2
        while low < high:
            if arr[mid] == target:
                return mid
            if arr[mid] < target:
                low = mid + 1
            else:
                high = mid
            mid = (low + high) // 2
        return -1

    # 上面的方法有个问题，查找断点的时间复杂度是O(n)
    '''
    如果中间的数小于最右边的数，则右半段是有序的，
    若中间数大于最右边数，则左半段是有序的
    '''
    def search2(self, nums: 'List[int]', target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] == target :
                return mid
            if nums[mid] < nums[right]:
                if nums[mid] < target and nums[right] >= target:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[left] <= target and nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1

if __name__=='__main__':
    s = Solution()
    print(s.search2(nums=[4,5,6,7,0,1,2], target=4))