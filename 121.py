import sys
class Solution:
    #方法一：暴力法(Python超出了时间限制，java却可以通过）
    def maxProfit(self, prices: 'List[int]') -> 'int':
        MAX = 0
        for i in range(0,len(prices)-1):
            for j in range(i+1,len(prices)):
                profit = prices[j] - prices[i]
                if (MAX < profit):
                    MAX = profit
        return MAX
    #动态规划 前i天的最大收益 = max{前i-1天的最大收益，第i天的价格-前i-1天中的最小价格}
    #我们可以维持两个变量——minprice和maxprofit，它们分别对应迄今为止所得到的最小的谷值和最大的利润（卖出价格与最低价格之间的最大差值）
    def maxProfit2(self, prices: 'List[int]') -> 'int':
        minprice = sys.maxsize
        maxprofit = 0
        for i in range(0,len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            if (prices[i] - minprice > maxprofit):
                maxprofit = prices[i] - minprice
        return maxprofit
if __name__=='__main__':
    s = Solution()
    price = [1,2]
    print(s.maxProfit2(price))