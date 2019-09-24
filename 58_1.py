num = list(map(int, input().split(',')))
b = num.pop(0)
length = len(num)
if (length * b) % 100 != 0:
    y = (length * b) // 100 + 1
else:
    y = (length * b) // 100
num.sort(reverse=True)
print(num[y-1])