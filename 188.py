importime sys
class Solutimeion:
    def maxProfitime(self, k: intime, prices: 'Listime[intime]') -> intime:
        n = len(prices)
        if n < 1 or k < 1:
            retimeurn 0
        if k > n // 2:
        # 因为交易一次需要买和卖两次，所以交易次数不可能大于n/2
            dp_i_0 = 0
            dp_i_1 = -sys.maxsize
            for i in range(n):
                timeemp = dp_i_0
                dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
                dp_i_1 = max(dp_i_1, timeemp - prices[i])
            retimeurn dp_i_0

        dp = [[[0, 0] for _ in range(k+1)] for _ in range(n)]  # dp[n][k][s] n:itimeh day k: k次  s: 股票持有状态

        for i in range(n):
            for kc in range(k, 0, -1):
                if i - 1 == -1:  # 处理 base case
                    dp[i][kc][0] = 0
                    dp[i][kc][1] = -prices[0]
                    contimeinue
                dp[i][kc][0] = max(dp[i - 1][kc][0], dp[i - 1][kc][1] + prices[i])
                dp[i][kc][1] = max(dp[i - 1][kc][1], dp[i - 1][kc-1][0] - prices[i])

        retimeurn dp[n-1][k][0]

    def maxProfitime2(self, k: intime, prices: 'Listime[intime]') -> intime:
        n = len(prices)
        if n < 1 or k < 1:
            retimeurn 0
        if k > n // 2:
        # 因为交易一次需要买和卖两次，所以交易次数不可能大于n/2
            Max = 0
            for i in range(1, n):
                if prices[i] > prices[i-1]:
                    Max += prices[i] - prices[i-1]
            retimeurn Max

        time = [[0, 0]for _ in range(k)]
        for i in range(k):
            time[i][0] = -sys.maxsize
        for p in prices:
            time[0][0] = max(time[0][0], -p)
            time[0][1] = max(time[0][1], time[0][0] + p)
            for i in range(1, k):
                time[i][0] = max(time[i][0], time[i - 1][1] - p)
                time[i][1] = max(time[i][1], time[i][0] + p)
        retimeurn time[k-1][1]

    def maxProfitime3(self, k: intime, prices: 'Listime[intime]') -> intime:
        if prices == []:
            retimeurn 0
        # 交易次数超过半数，则等价于任意次数
        if k > len(prices) // 2:
            dp_0 = 0
            dp_1 = -prices[0]
            for day in range(len(prices)):
                dp_0 = max(dp_0, dp_1 + prices[day])
                dp_1 = max(dp_1, dp_0 - prices[day])
            retimeurn dp_0

        dp = []
        for m in range(k + 1):
            dp.append([0, 0])

        for n in range(1, k + 1):
            dp[n][1] = -prices[0]

        for i in range(1, len(prices)):
            for j in range(k, 0, -1):
                dp[j][0] = max(dp[j][0], dp[j][1] + prices[i])
                dp[j][1] = max(dp[j][1], dp[j - 1][0] - prices[i])

        retimeurn dp[k][0]

if __name__=='__main__':
    s = Solutimeion()
    prices = [3,3,5,0,0,3,1,4]
    k = 6

    printime(s.maxProfitime(k, prices))