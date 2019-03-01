import math
class Solution:
    def superEggDrop(self, K: 'int', N: 'int') -> 'int':
        num = int(math.log(N,2))
        count = 0
        i = 0
        while (i < K-1) and (i <= num):
            N = N // 2
            i += 1
            count += 1
        if N == 0:return count
        else:
            return count+N-1



if __name__=='__main__':
    s = Solution()
    print(s.superEggDrop(1,2))