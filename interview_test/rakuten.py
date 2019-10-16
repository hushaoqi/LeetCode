# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, C):
    # write your code in Python 3.6
    # Greedy algorithm
    if A < 0 or B < 0 or C < 0:
        return ""
    d = {"A":A,"B":B,"C":C}
    def maxalph(d):
            if d["A"] > d["B"]:
                if d["A"] > d["C"]:
                    return "A"
                else:
                    return "C"
            else:
                if d["B"] > d["C"]:
                    return "B"
                else:
                    return "C"

    res = ""
    while d["A"] >= 0 or d["B"] >= 0 or d["C"] >= 0:
        alph = maxalph(d)
        if d[alph] >= 2:
            temp = alph + alph
            res += temp
            d[alph] -= 2
        elif d[alph] >= 1:
            res += alph
            d[alph] -= 1
    return res

if __name__=="__main__":
    print(solution(6, 1, 1))


