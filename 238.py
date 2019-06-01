class Solution:
    def productExceptSelf(self, nums: 'List[int]') -> 'List[int]':
        left = []
        pre = 1
        for i in range(len(nums)):
            left.append(pre)
            pre = pre * nums[i]

        # print(left)
        right = []
        back = 1
        for i in range(len(nums)-1, -1, -1):
            right.append(back)
            back = back * nums[i]

        right = right[::-1]
        # print(right)
        res = []
        for j in range(len(nums)):
            res.append(left[j] * right[j])
        return res
    # 进一步常数空间的实现,出于对空间复杂度分析的目的，输出数组不被视为额外空间。
    # 所以可以利用输出数组存储

    def productExceptSelf2(self, nums: 'List[int]') -> 'List[int]':
        n = len(nums)
        res = [1] * n

        for i in range(1, n):
            res[i] = res[i-1] * nums[i-1]
        right = 1
        for i in range(n-1, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res

if __name__=='__main__':
    s = Solution()
    nums = [1, 2, 3, 4]
    print(s.productExceptSelf2(nums))

