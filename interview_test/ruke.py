# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, C):
    # write your code in Python 3.6
    # Greedy algorithm
    if A < 0 or B < 0 or C < 0:
        return ""
    d = {"a":A,"b":B,"c":C}
    px = sorted(d.keys())
    res = ""

    while d[px[0]] > 0 or d[px[1]] > 0 or d[px[2]] > 0:
        if d[px[0]] >= 2:
            res += (px[0] + px[0])
            d[px[0]] -= 2
            if d[px[1]] >= 2:
                res += (px[1] + px[1])
                d[px[1]] -= 2
            elif d[px[1]] >= 1:
                res += px[1]
                d[px[1]] -= 1
            else:
                if d[px[2]] >= 1:
                    res += px[2]
                    d[px[2]] -= 1

        elif d[px[0]] >= 1:
            res += px[0]
            d[px[0]] -= 1

        else:
            return res
        px = sorted(d.keys())

    return res


if __name__=="__main__":
    print(solution(1, 3, 1))


