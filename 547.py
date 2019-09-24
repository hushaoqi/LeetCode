def find_friend_circle(M):
    pre_friend = [-1] * len(M)
    rank = dict()
    for i in range(len(M)):
        for j in range(i):
            if M[i][j] == 1:
                union(i, j, pre_friend, rank)
    circle_num = 0
    for i in pre_friend:
        if i == -1:
            circle_num += 1
    return circle_num


def find_friend(num, pre_friend):
    while pre_friend[num] != -1:
        num = pre_friend[num]
    return num


def union(x, y, pre_friend, rank):
    if x == y:
        return
    x = find_friend(x, pre_friend)
    y = find_friend(y, pre_friend)
    rank_x = rank[x] if x in rank else 0
    rank_y = rank[y] if y in rank else 0
    if x == y:
        return
    if rank_x > rank_y:
        pre_friend[y] = x
    elif rank_x < rank_y:
        pre_friend[x] = y
    else:
        pre_friend[x] = y
        rank[y] = 1

if __name__=="__main__":
    N = int(input())
    M = []
    for _ in range(N):
        M.append(list(map(int, input().strip().split())))
    print(find_friend_circle(M))