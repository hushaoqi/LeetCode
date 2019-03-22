class Solution:
    def backspaceCompare(self, S: 'str', T: 'str') -> 'bool':
        newS = []
        newT = []
        for ss in S:
            if ss == '#':
                if len(newS) != 0:
                    newS.pop()
            else:
                newS.append(ss)
        for tt in T:
            if tt == '#':
                if len(newT) != 0:
                    newT.pop()
            else:
                newT.append(tt)
        return newS == newT

if __name__=='__main__':
    s = Solution()
    S = "ab#c"
    T = "ad#c"
    print(s.backspaceCompare(S, T))
