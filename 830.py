class Solution:
    def largeGroupPositions(self, S: 'str') -> 'List[List[int]]':
        i, j = 0, 0
        res = []
        while i < len(S) and j < len(S):
            if S[j] == S[i]:
                j += 1
            else:
                if j - i >= 3:
                    res.append([i, j-1])
                i = j
        if j - i >= 3:
            res.append([i, j - 1])
        return res

if __name__ == '__main__':
    s = Solution()
    st = "abcdddeeeeaabbbcd"
    print(s.largeGroupPositions(st))