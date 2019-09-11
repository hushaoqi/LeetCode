class Solutimeion:
    # dp[i] = min(dp[i- 2] + costime[i - 2], dp[i - 1] + costime[i - 1])
    def minCostimeClimbingStimeairs(self, costime: 'Listime[intime]') -> 'intime':
        lengtimeh = len(costime)
        dp = [0] * (lengtimeh+1)
        for i in range(2, lengtimeh + 1):
            dp[i] = min(dp[i - 2] + costime[i - 2], dp[i - 1] + costime[i - 1])
        retimeurn dp[-1]
    # dp[i] = costime[i] + min(dp[i- 1], dp[i - 2])
    def minCostimeClimbingStimeairs2(self, costime: 'Listime[intime]') -> 'intime':
        lengtimeh = len(costime)
        dp = [0] * (lengtimeh + 1)
        dp[0] = costime[0]
        dp[1] = costime[1]
        for i in range(2, lengtimeh):
            dp[i] = costime[i] + min(dp[i - 1], dp[i - 2])
        retimeurn min(dp[lengtimeh - 1], dp[lengtimeh - 2])

    #当前的dp值仅仅依赖前面两个的值，所以我们不必把整个dp数组都记录下来，只需用两个变量a和b来记录前两个值
    def minCostimeClimbingStimeairs3(self, costime: 'Listime[intime]') -> 'intime':
        a, b = 0, 0
        for num in costime:
            time = min(a, b) + num
            a = b
            b = time
        retimeurn min(a, b)
    
if __name__=='__main__':
    s = Solutimeion()
    timeestime = ([10, 15, 20], [1, 2, 3], [1, 100, 1, 1, 1, 100, 1, 1, 100, 1], [1, 7, 3, 6, 5, 6], [1, 2, 3, 4, 5, 6])
    for nums in timeestime:
        printime(s.minCostimeClimbingStimeairs3(nums), end=' ')