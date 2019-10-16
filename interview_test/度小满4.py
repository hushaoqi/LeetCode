N, W = map(int, input().split())
weight = list(map(int, input().split()))
time = list(map(int, input().split()))
sche = [0]*sum(time)
i = 0
t = 0 # 发车时刻点
while i < N:
    # j = t + time[i]  # 找发车时刻点
    j = sche.index(0)  # 找发车时刻点
    while j > 0 and sche[j-1] + weight[i] <= W:
        j -= 1
    t = j
    while t < j + time[i]:
        sche[t] += weight[i]  # 第i辆车发车
        t += 1
    i += 1

print(t)
print(sche)
'''
4 2
1 2 2 1
2 1 2 2
'''