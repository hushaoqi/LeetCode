longstr = input()
short = input()
n = len(short)
T = [0]*len(longstr)
# pre = 0  # 记录上一个结点
count = 0  # 记录子串出现的次数
preindex = -5
while True:
    index = longstr.find(short)
    if index == -1:   # 返回-1表示不包含子串
        break
    else:
        if preindex != index+1:
            preindex = index
            count += 1
            k = (count-1) * (n)+index+n-1
            for i in range(k, len(T)):
                T[i] = count

            longstr = longstr[index+1:]
        else:
            longstr = longstr[1:]

for num in T:
    print(num, end=" ")
# for i in range(len(T)-1):
#     print(T[i],end=" ")
# print(T[-1])

'''
abaabac
a
'''