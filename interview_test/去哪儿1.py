from math import factorial
def Cn_k(n, k):
    return (factorial(n) // factorial(n-k))

n = int(input())
if n == 0:
    print(1)
else:
    for i in range(n+1):
        print(Cn_k(n, i), end=' ')


from collections import defaultdict
def Cn_k(n, k):
    C = defaultdict(int)
    for row in range(n + 1):
        C[row, 0] = 1
        for col in range(1, k+1):
            if col <= row:
                C[row, col] = C[row-1, col-1] + C[row-1, col]
    return C[n, k]
n = int(input())
for i in range(n+1):
    print(Cn_k(n, i), end=' ')