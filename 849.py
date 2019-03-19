import math
class Solution:
    def maxDistToClosest(self, seats: 'List[int]') -> 'int':
        flag = False
        curDistance, maxDistance = 0, 0
        for k in range(0, len(seats)):
            # 判断两边是否为0，特殊处理
            if (k == 0 and seats[k] == 0) or (k == len(seats)-1 and seats[-1] == 0):
                flag = True
            if seats[k] == 0:
                curDistance += 1
            else:
                if flag:
                    maxDistance = max(maxDistance, curDistance)
                else:
                    maxDistance = max(maxDistance, math.ceil(curDistance/2))
                curDistance = 0
                flag = False
        if flag:
            maxDistance = max(maxDistance, curDistance)
        return maxDistance

    def maxDistToClosest2(self, seats: 'List[int]') -> 'int':
        result, count, begin, end, begin_end = 0, 0, 0, 0, False
        for i in seats:
            if begin_end:  # r如果第一次出现1了，就用普通计数方式
                if i == 0:
                    count += 1
                else:
                    if count > result:
                        result = count
                    count = 0
            else:  # 处理前一截都是0的情况
                if i == 0:
                    begin += 1
                else:
                    begin_end = True
        end = count if seats[-1] == 0 else count
        return max(math.ceil(result / 2), begin, end)

    def maxDistToClosest3(self, seats: 'List[int]') -> 'int':
        # 特殊处理两边是0的情况
        a, b = 0, max(seats[::-1].index(1), seats.index(1)) * 2
        for i, v in enumerate(seats):
            if v == 1:
                if i - a > b:
                    b = i - a
                a = i

        return b // 2
if __name__=='__main__':
    s = Solution()
    seats = [1, 0, 0, 0]
    print(s.maxDistToClosest3(seats))
