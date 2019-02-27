class Solution:
    def getRow(self, rowIndex: 'int') -> 'List[int]':
        if rowIndex == 0: return [1]
        if rowIndex == 1: return [1, 1]

        pre = [1, 1]
        for i in range(2, rowIndex+1):
            cur = [1]  # 首1
            for m in range(0, len(pre) - 1):
                cur.append(pre[m] + pre[m + 1])
            cur.append(1)  # 尾1
            pre = cur
        return cur

if __name__ == '__main__':
    s = Solution()
    print(s.getRow(3))