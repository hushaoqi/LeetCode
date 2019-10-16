class Solution:
    def merge(self, intervals):
        intervals.sort(key= lambda x:x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][-1] <interval[0]:
                merged.append(interval)
            else:
                merged[-1][-1] = max(merged[-1][-1], interval[-1])
        return merged
    # 遍历所有区间，打印累计长度
    def sum_num(self, merged):

        for i in range(len(merged)):
            temp = self.merge(merged[:i+1])
            SUM = 0
            for j in range(len(temp)):
                SUM += temp[j][1] - temp[j][0] + 1
            print(SUM)
        return
if __name__== "__main__":
    arr = list(map(int, input().strip().split()))
    n, m = arr[0], arr[1]
    string = []
    for i in range(m):
        string.append([])
        string[i] = list(map(int, input().strip().split()))
    A = Solution()
    # string = A.merge(string)
    A.sum_num(string)

    '''
4 3
1 2
2 3
3 4
2
3
4
    '''