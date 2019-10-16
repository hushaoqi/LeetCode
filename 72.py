def distance(wordA, wordB):
    if not wordA or not wordB:
        return len(wordA) + len(wordB)
    if wordA[0] == wordB[0]:
        return distance(wordA[1:], wordB[1:])
    else:
        onefunc =  distance(wordA, wordB[1:])+1
        twofunc = distance(wordA[1:], wordB)+ 1
        threefunc = distance(wordA[1:], wordB[1:])+ 1
        return min(onefunc, twofunc, threefunc)
if __name__=='__main__':
    wordA, wordB = input().split("<ctrip>")
    res = distance(wordA, wordB)
    print(res)