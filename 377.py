class Solution:
    def combinationSum4(self, nums: 'List[int]', target: int) -> int:
        size = len(nums)
        if size == 0 or target <= 0:
            return 0

        dp = [0 for _ in range(target + 1)]

        # 这一步很关键，想想为什么 dp[0] 是 1
        # 因为 0 表示空集，空集和它"前面"的元素凑成一种解法，所以是 1
        # 这一步要加深体会
        # 使用dp数组，dp[i]代表组合数为i时使用nums中的数能组成的组合数的个数
        # 举个例子比如nums=[1,3,4],target=7; dp[7]=dp[6]+dp[4]+dp[3]
        dp[0] = 1

        for i in range(1, target + 1):
            for j in range(size):
                if i >= nums[j]:
                    dp[i] += dp[i - nums[j]]

        return dp[-1]

if __name__=='__main__':
    s = Solution()
    nums = list(map(int, input().strip().split()))
    target = int(input().strip())
    print(s.combinationSum4(nums, target))