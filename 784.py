class Solution:
    # DFS 回溯
    def letterCasePermutation(self, S: 'str') -> 'List[str]':
        res = list()
        length = len(S)
        if length == 0:
            return [""]

        def dfs(start, temp):
            if start >= length or len(temp) == length:
                res.append(temp)
                return
            # print(start, temp ,end='\n')
            if S[start].isdigit():
                dfs(start + 1, temp + S[start])

            elif S[start].islower():
                dfs(start + 1, temp + S[start])
                dfs(start + 1, temp + S[start].upper())

            elif S[start].isupper():
                dfs(start + 1, temp + S[start])
                dfs(start + 1, temp + S[start].lower())

        dfs(0, "")
        return res

    # BFS
    def letterCasePermutation2(self, S:'str') -> 'List[str]':
        import copy
        res = [""]

        for i, x in enumerate(S):
            # if len(res) == 0:
            #     res.append(x)
            if x.isdigit():
                for index, item in enumerate(res):
                    res[index] += x
            elif x.isupper():
                temp = list()
                for index, item in enumerate(res):
                    # print item
                    temp.append(item + x)
                    temp.append(item + (x.lower()))
                res = copy.deepcopy(temp[:])
            elif x.islower():
                temp = list()
                for index, item in enumerate(res):
                    temp.append(item + x)
                    temp.append(item + (x.upper()))
                res = copy.deepcopy(temp[:])
            # print temp
        return res
    # BitMap

    def letterCasePermutation3(self, S: 'str') -> 'List[str]':
        l = len(S)
        n = 2 ** l
        res = list()
        if l == 0:
            res.append("")
        for i in range(0, n):
            temp = ""

            for j in range(0, l):
                if ((2 ** j) & i) == 0:
                    temp += S[j].lower()
                else:
                    temp += S[j].upper()
            if temp not in res:
                res.append(temp)
        return res

    def letterCasePermutation4(self, S: 'str') -> 'List[str]':

        res = ['']
        for c in S:
            res = [i + c for i in res] + [i + c.swapcase() for i in res if c.isalpha()]
        return res
    # 递归
    def letterCasePermutation5(self, S: 'str') -> 'List[str]':
        def permutation(s, index, prefix):
            if index > len(s) - 1:
                return prefix

            tmp = []
            for p in prefix:
                if s[index].isdigit():
                    tmp.append(p + s[index])
                else:
                    tmp.append(p + s[index].lower())
                    tmp.append(p + s[index].upper())
            res = permutation(s, index + 1, tmp)
            return res

        return permutation(S, 0, [''])

if __name__ == '__main__':
    S = Solution()
    s = "abcd"
    print(S.letterCasePermutation(s))