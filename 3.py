class Solution:
    """
    @param: : An integer
    @param: : An integer
    @return: An integer denote the count of digit x in m..n
    """

    def digitCounts(self, m, n, x):
        # write your code here
        result = 0
        for i in range(m, n + 1):
            result += str(i).count(str(x))
        return result

if __name__=='__main__':
    s = Solution()
    m, n, x = map(int, input().split())
    print(s.digitCounts(m, n, x))