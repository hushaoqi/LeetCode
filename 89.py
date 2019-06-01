class Solution:
    '''

    关键是搞清楚格雷编码的生成过程, G(i) = i ^ (i / 2); 异或操作
    如
    n = 3:
    G(0) = 000,  二进制与格雷码的关系
    G(1) = 1 ^ 0 = 001 ^ 000 = 001
    G(2) = 2 ^ 1 = 010 ^ 001 = 011
    G(3) = 3 ^ 1 = 011 ^ 001 = 010
    G(4) = 4 ^ 2 = 100 ^ 010 = 110
    G(5) = 5 ^ 2 = 101 ^ 010 = 111
    G(6) = 6 ^ 3 = 110 ^ 011 = 101
    G(7) = 7 ^ 3 = 111 ^ 011 = 100
    '''
    # 镜射排列
    def grayCode(self, n: int) -> 'List[int]':
        res = [0]
        i = 0
        while i < n:
            size = len(res)
            j = size - 1
            while j >= 0:
                res.append(res[j] | (1 << i))
                j -= 1
            i += 1
        return res

    # 二进制数转格雷码

    def grayCode2(self, n: int) -> 'List[int]':
        res = []
        i = 0
        while i < pow(2, n):  # 格雷编码，每次变一位，总共有 2 ** n 个编码
            res.append((i // 2) ^ i)  #
            i += 1
        return res

    # 递归方法

    def grayCode3(self, n: int) -> 'List[int]':
        res = []
        if n == 0 or n == 1:
            for i in range(n + 1):
                res.append(i)
            return res
        tmp = self.grayCode(n - 1)
        res += tmp
        tmp = tmp[::-1]
        c = pow(2, n - 1)
        for i in tmp:
            res.append(c + i)
        return res

if __name__=='__main__':
    s = Solution()
    print(s.grayCode3(3))
