n = int(input())  # 成就数
finish = 0
for i in range(1, n+1):
    work = list(map(int, input().split()))
    work = work[1:]
    if len(work) != 0:
        work = max(work)
        if work > finish:
            print(work-finish, end=" ")
            finish = work
        elif finish < i:
            print(i-finish, end=" ")
            finish = i
        else:
            print(0,end=" ")
    else:
        if finish < i:
            print(i-finish, end=" ")
            finish = i
        else:
            print(0,end=" ")

'''
3
1 2
0
1 2


2 0 1

5
2 3 5
1 4
2 2 5
0
1 4

5 0 0 0 0
'''