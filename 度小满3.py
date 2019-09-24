while True:
    s = input()
    if len(s) == 0:
        break
    else:
        n, m = map(int, s.split())
    sg = [[0]*200 for _ in range(200)]
    ext = [False] * 200
    # for i in range(2, 201):
    #     for j in range(2, 201):
    #         for k in range(2, i-1):
    #             ext[sg[k][j] ^ sg[i-k][j]] = True
    #         for k in range(2, j-1):
    #             ext[sg[i][k] ^ sg[i][j-k]] = True
    #         w = 0
            # while w <=200:
            #     if ext[w] is False:
            #         sg[i][j] = w
            #         break
            #     w += 1
    if sg[n][m] == 0:
        print("WIN")
    else:
        print("LOSE")