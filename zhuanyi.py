n = int(input())
a_box = list(map(int, input().split()))
a_space = list(map(int, input().split()))

sum_num = sum(a_box)
a_box.sort(reverse=True)
a_space.sort(reverse=True)
temp = 0
for i in range(len(a_box)):
    temp+= a_space[i]
    if temp >= sum_num:
        k = i + 1
        break
t = 0
for i in range(k, len(a_box)):
    t += a_box[i]
print(k, end=" ")
print(t)