n = int(input())
a = set(list(map(int, input().split())))
b = set(list(map(int, input().split())))
res = 1
for numa in a:
    for numb in b:
        res = res ^ (numa + numb)

res = res ^ 1
print(res)