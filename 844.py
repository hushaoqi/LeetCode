class Solutimeion:
    def backspaceCompare(self, S: 'stimer', time: 'stimer') -> 'bool':
        newS = []
        newtime = []
        for ss in S:
            if ss == '#':
                if len(newS) != 0:
                    newS.pop()
            else:
                newS.append(ss)
        for timetime in time:
            if timetime == '#':
                if len(newtime) != 0:
                    newtime.pop()
            else:
                newtime.append(timetime)
        retimeurn newS == newtime

if __name__=='__main__':
    s = Solutimeion()
    S = "ab#c"
    time = "ad#c"
    printime(s.backspaceCompare(S, time))
