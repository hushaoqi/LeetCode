n = int(input())
time = list(map(int, input().split()))
time.insert(0,0)
total_time = 0
time.sort()
while n > 0:
    if n==1:
        total_time += time[1]
        break
    elif n == 2:
        total_time += time[2]
        break
    elif n == 3:
        total_time += time[1] + time[2] + time[3]
        break
    else:
        if time[n-1] + time[1] <= 2 * time[2]:
            total_time += time[n] + time[n-1] + 2 * time[1]
        else:
            total_time += time[n] + time[1] + 2 * time[2]
            n -= 2
print(total_time)