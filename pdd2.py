class Solution:
    def merge(self, temp, string):
        temp.append(string)
        temp.sort(key= lambda x:x[0])
        merged = []
        for interval in temp:
            if not merged or merged[-1][-1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][-1] = max(merged[-1][-1], interval[-1])
        SUM = 0
        for j in range(len(merged)):
            SUM += merged[j][1] - merged[j][0] + 1
        print(SUM)
        return merged

    def sum_num(self, merged):
        temp = []
        temp.append(merged[0])
        print(merged[0][1] - merged[0][0] + 1)
        for i in range(1, len(merged)):
            temp = self.merge(temp, merged[i])
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