n = int(input())
table = []
for _ in range(n):
    m, n = list(map(int, input().split()))
    table.extend([n]*m)

table.sort()  # 从小到大排序
# print(table)
max_time = 0
small = 0
large = len(table)-1
while small < large:
    max_time = max(max_time, table[small] + table[large])
    small += 1
    large -= 1
print(max_time)