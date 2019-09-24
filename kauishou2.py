from collections import Counter
n = int(input())
num = list(map(int, input().split()))
num.sort()
cha = []
for i in range(1, len(num)):
    cha.append(num[i] - num[i-1])
con = Counter(cha).most_common(1)
print(con[0][1]+1)
