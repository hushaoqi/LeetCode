class Solution:
    def calPoints(self, ops: 'List[str]') -> 'int':
        score = []
        for s in ops:
            if s == '+':
                if len(score) == 0:
                    #score.append(0)
                    pass
                elif len(score) == 1:
                    score.append(score[-1])
                else:
                    score.append(score[-2] + score[-1])
            elif s == 'D':
                if len(score) == 0:
                    #score.append(0)
                    pass
                else:
                    score.append(score[-1] * 2)
            elif s == 'C':
                if len(score) == 0:
                    pass
                else:
                    score.remove(score[-1])
            else:
                score.append(int(s))
        return sum(score)

if __name__=='__main__':
    s = Solution()
    ops = ["+","5","2","C","D"]
    print(s.calPoints(ops))
