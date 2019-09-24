N, M = map(int, input().split())
table = []
for _ in range(N):
    table.append(list(map(int, input().split())))
# print(table)
print(sum(table[:][2]))
'''
输入
第一行输入两个整数N和M，1≤N，M≤10^5。

接下来N行，第i行输入三个整数a、b和c，表示第i名工人只懂得操作第a台和第b台机器，且其能力值为c，1≤a<b≤M，1≤c≤10^9。

输出
输出所有操作机器的工人的能力值总和的最大值


样例输入
3 3
1 2 1
1 2 2
1 2 3
样例输出
5

提示
可以让第2名工人操作第1台机器，让第3名工人操作第2台机器。
'''