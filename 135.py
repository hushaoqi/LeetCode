n = int(input().strip())
fen = []
for _ in range(n):
    fen.append(int(input().strip()))

def num():
    if n == 1:
        return 1
    if n == 2:
        if fen[0] == fen[1]:
            return 2
        else:
            return 3

    count = [0] * n
    count[0] = 1
    for i in range(1,n):
        if fen[i] > fen[i-1]:
           count[i] = count[i-1] + 1
        else:
            count[i] = 1
    for j in range(n-2, -1, -1):
        if fen[j] > fen[j+1] and count[j] <= count[j+1]:
            count[j] = count[j+1] + 1

    return sum(count)
res = num()
print(res)

'''
6
3
6
3
5
6
2

10

4
1
4
2
1

7
'''