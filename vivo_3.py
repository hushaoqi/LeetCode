'''
Welcome to vivo !
'''


def solution(N, M):
    # TODO Write your code here
    pre = [x for x in range(1, N + 1)]
    res =[]
    count = 1
    tem = pre[:]
    length = len(tem)
    while len(pre) != 0:
        if count % M == 0:
            res.append(tem[count % M - 1])
            print(tem[count % M - 1], end=" ")
            pre.pop(count % M - 1)
        if count % N == 0:
            tem = pre[:]
            length = len(tem)
            count -= length
        count += 1

N, M = map(int, input().split())
solution(N, M)

'''
6 3
3 6 4 2 5 1 

'''