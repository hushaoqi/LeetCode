import  sys
class Solution:
    #关注连续的上坡，坡度之差即为收益，即找出谷和峰
    def maxProfit(self, prices: 'List[int]') -> 'int':
        if prices == []:return 0
        i = 0
        valley = prices[0]
        peak = prices[0]
        maxprofit = 0
        while (i < len(prices)-1):
            while (i < len(prices)-1) and (prices[i] >= prices[i+1]):
                i += 1
            valley = prices[i]
            while (i < len(prices)-1) and (prices[i] <= prices[i+1]):
                i += 1
            peak = prices[i]
            maxprofit += (peak - valley)
        return maxprofit
    '''
    思路和法一一样，不过化简为找每一个相邻的上坡，求和
    继续在斜坡上爬升并持续增加从连续交易中获得的利润，
    而不是在谷之后寻找每个峰值。
    最后，我们将有效地使用峰值和谷值，
    但我们不需要跟踪峰值和谷值对应的成本以及最大利润，
    但我们可以直接继续增加加数组的连续数字之间的差值，
    如果第二个数字大于第一个数字，我们获得的总和将是最大利润。
    这种方法将简化解决方案。
    '''
    def maxProfit2(self, prices: 'List[int]') -> 'int':
        maxprofit = 0
        for i in range(1,len(prices)):
            if (prices[i] > prices[i-1]):
                maxprofit += (prices[i] - prices[i-1])
        return maxprofit
if __name__=='__main__':
    s = Solution()
    prices = []
    print(s.maxProfit2(prices))
