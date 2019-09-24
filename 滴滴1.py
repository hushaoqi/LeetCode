# 垃圾分类
n, m = map(int, input().split())  # 总共n堆垃圾，m个约束条件
table = []
for _ in range(m):
    table.append(list(map(int, input().split())))
# print(table)
car1 = set()
car2 = set()
for i in range(len(table)):
    if table[i][0] not in car1 and table[i][1] not in car1:
        car1.add(table[i][0])
        car2.add(table[i][1])


'''
输入第一行包含两个正整数n，m，表示共有n堆垃圾，m个约束条件。(1<=n,m<=500)

接下来有m行，每行有两个正整数，a，b，表示第a堆垃圾和第b堆垃圾不能放在一辆垃圾车上。(1<=a,b<=n)

输出
输出仅包含一个正整数，表示两辆垃圾车一次最多带走的垃圾的数量。


样例输入
5 2
1 4
3 4
样例输出
4
'''







