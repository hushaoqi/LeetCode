# 线性动态规划
class Solution:
    # p[i]表示到i位置时首差值为正的摆动子序列的最大长度，
    # q[i]表示到i位置时首差值为负的摆动子序列的最大长度。
    # 我们从i=1开始遍历数组，然后对于每个遍历到的数字，再从开头位置遍历到这个数字，
    # 然后比较nums[i]和nums[j]，分别更新对应的位置
    # nums[i] > nums[i-1] : p[i] = q[i-1] + 1 , q[i] = q[i-1]
    # nums[i] < nums[i-1] : q[i] = p[i-1] + 1 , p[i] = p[i-1]
    def wiggleMaxLength(self, nums: 'List[int]') -> int:
        n = len(nums)
        if n == 0:
            return 0
        p = [1] * n
        q = [1] * n
        for i in range(1, n):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    p[i] = max(p[i], q[j] + 1)
                elif nums[i] < nums[j]:
                    q[i] = max(q[i], p[j] + 1)

        return max(p[-1], q[-1])

    # O(n)
    # 不在维护两个dp数组，而是维护两个变量p和q，然后遍历数组，如果当前数字比前一个数字大，则p=q+1，
    # 如果比前一个数字小，则q=p+1，
    # 最后取p和q中的较大值跟n比较，取较小的那个
    def wiggleMaxLength2(self, nums: 'List[int]') -> int:
        p, q, n = 1, 1, len(nums)
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                p = q + 1
            elif nums[i] < nums[i - 1]:
                q = p + 1
        return min(n, max(p, q))

if __name__ == '__main__':
    s = Solution()
    nums = list(map(int, input().strip().split(",")))  # 输入 1,7,4,9,2,5
    print(s.wiggleMaxLength(nums))
# https://leetcode-cn.com/problems/wiggle-subsequence/solution/bai-dong-xu-lie-by-leetcode/