N, M = map(int, input().split())  # N表示数字个数，M表示游戏轮数，0<= M <= N/2
A = list(map(int,input().split()))
total = M * 2  # 表示M轮游戏总共参与的数字个数
A.sort()
A = A[:total]
# print(A)
pre = 0
post = len(A)-1
sumnum = 0
while pre < post:
    sumnum += A[pre] * A[post]
    pre += 1
    post -= 1
print(sumnum)