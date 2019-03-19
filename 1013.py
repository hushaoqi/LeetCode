class Solution:
    def numPairsDivisibleBy60(self, time: 'List[int]') -> 'int':
        record = [0 for _ in range(0, 60)]
        for index, item in enumerate(time):
            record[item % 60] += 1

        res = 0
        for i in range(0, len(time)):
            temp = time[i] % 60
            if temp:
                record[temp] -= 1  # 每次操作前把自己的那一次去掉，保证去重，同时保证j > i
                res += record[60 - temp]
            elif temp == 0 and record[0] > 1:
                res += record[0] * (record[0] - 1) // 2  # 对于N个可以被60整除的数来说，在它们中取得所有结果的个数为C N 2 = N *(N - 1) / 2
                record[0] = 0  # 一次处理完所有的可以被60整除的数，然后把record[0]归零，保证不重复计算

        return res

    def numPairsDivisibleBy602(self, time: 'List[int]') -> 'int':
        record = [0 for _ in range(0, 60)]
        for index, item in enumerate(time):
            record[item % 60] += 1

        res = 0
        for i in range(0, 60):
            if i in [0, 30] and record[i] > 1:
                res += record[i] * (record[i] - 1)  # 对于0 和 30 来说，在它们中取得所有结果的个数为C N 2 = N *(N - 1) / 2， N是自身统计的个数
                record[i] = 0  # 一次处理完所有的这样的数，然后把record[0 or 30]归零，保证不重复计算
            elif i:
                res += record[60 - i] * record[i]

        return res // 2
if __name__ == '__main__':
    s = Solution()
    A = [30,20,150,100,40]
    print(s.numPairsDivisibleBy60(A))