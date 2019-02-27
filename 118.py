class Solution:
    def generate(self, numRows: 'int') -> 'List[List[int]]':
        if numRows == 0 : return []
        if numRows == 1 : return [[1]]
        if numRows == 2 : return [[1],[1,1]]
        num = [[1],[1,1]]
        pre = [1,1]
        for i in range(2,numRows):
            cur = [1] #首1
            for m in range(0,len(pre)-1):
                cur.append(pre[m] + pre[m+1])
            cur.append(1) #尾1
            num.append(cur)
            pre = cur
        return num
if __name__=='__main__':
    s = Solution()
    print(s.generate(7))
