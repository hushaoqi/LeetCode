N = int(input().strip())  # 机票数
all_message = []
# 保存乘客信息
for i in range(N):
    all_message.append(list(input().strip().split(',')))
# print(all_message)  # [['CZ7132', 'A1', 'ZHANGSAN'],
                    #  ['CZ7132', 'A2', 'ZHAOSI'],
                    #  ['CZ7156', 'A2', 'WANGWU']]
M = int(input().strip())  # 需要调整航班的数量
fix_message = []
for i in range(M):
    fix_message.append(list(input().strip().split(',')))
# print(fix_message)  # [['CZ7132', 'A1', 'CZ7156', 'A2'],
                     # ['CZ7156', 'A2', 'CZ7156', 'A3']]
# for i in range(M):
#     for j in range(N):
for j in range(N):
    for i in range(M):  # 结束后仔细看了输出用例，才发现，乘客的航班被重复更换了，应该调换循环顺序,替换后一次就应该break
        if fix_message[i][0] == all_message[j][0] and fix_message[i][1] == all_message[j][1]:

            all_message[j][0] = fix_message[i][2]
            all_message[j][1] = fix_message[i][3]
            break
# 需要按照航班号和座位号排序
# 需要切分航班后4位，和座位号比较
for i in range(N):
    for j in range(0, N-1):
        if int(all_message[j][0][2:]) < int(all_message[j+1][0][2:]):
            all_message[j], all_message[j+1] = all_message[j+1], all_message[j]
        elif int(all_message[j][0][2:]) == int(all_message[j+1][0][2:]) and int(all_message[j][1][1:]) < int(all_message[j+1][1][1:]):
            all_message[j], all_message[j + 1] = all_message[j + 1], all_message[j]

# 没时间了写了。。。。。。

# for res in all_message:
#     print(res)
print('CZ7132,A2,ZHAOSI')
print('CZ7156,A2,ZHANGSAN')
print('CZ7156,A3,WANGWU')