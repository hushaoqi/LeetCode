class Solution:
    # dp[i] = min(dp[i- 2] + cost[i - 2], dp[i - 1] + cost[i - 1])
    def minCostClimbingStairs(self, cost: 'List[int]') -> 'int':
        length = len(cost)
        dp = [0] * (length+1)
        for i in range(2, length + 1):
            dp[i] = min(dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1])
        return dp[-1]
    # dp[i] = cost[i] + min(dp[i- 1], dp[i - 2])
    def minCostClimbingStairs2(self, cost: 'List[int]') -> 'int':
        length = len(cost)
        dp = [0] * (length + 1)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, length):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        return min(dp[length - 1], dp[length - 2])

    #当前的dp值仅仅依赖前面两个的值，所以我们不必把整个dp数组都记录下来，只需用两个变量a和b来记录前两个值
    def minCostClimbingStairs3(self, cost: 'List[int]') -> 'int':
        a, b = 0, 0
        for num in cost:
            t = min(a, b) + num
            a = b
            b = t
        return min(a, b)
    
if __name__=='__main__':
    s = Solution()
    test = ([10, 15, 20], [1, 2, 3], [1, 100, 1, 1, 1, 100, 1, 1, 100, 1], [1, 7, 3, 6, 5, 6], [1, 2, 3, 4, 5, 6])
    for nums in test:
        print(s.minCostClimbingStairs3(nums), end=' ')