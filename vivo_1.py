# -*- coding:utf-8 -*-
import heapq
class Solution:
    less = []
    greater = []
    def Insert(self, num):
        # write code here

        if len(self.less) == 0 or num <= self.less[0]:
            heapq.heappush(self.less,num)
        else:
            heapq.heappush(self.greater,num)
        if len(self.less) == len(self.greater) + 2:
            heapq.heappush(self.greater, heapq.heappop(self.less))
        if len(self.less) + 1 == len(self.greater):
            heapq.heappush(self.less, heapq.heappop(self.greater))
    def GetMedian(self):
        # write code here
        if len(self.less) == len(self.greater):
            return (heapq.heappop(self.less) + heapq.heappop(self.greater)) / 2
        else:
            return heapq.heappop(self.less)
if __name__== "__main__":
    s = Solution()
    num = [5,2]  # ,3,4,1,6,7,0,8
    for n in num:
        s.Insert(n)
    print(s.less)
    print(s.greater)
    print(s.GetMedian())