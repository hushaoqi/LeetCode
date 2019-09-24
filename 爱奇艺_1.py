N = int(input())
game_list = list(map(int, input().split()))
game_max = 0
for a in game_list:
    game_max = max(a, game_max)
l = 0
r = game_max * 2
while l < r:
    m = (l + r)//2
    game_count = 0
    for a in game_list:
        game_count += max(m-a, 0)
    if m > game_count:
        l = m + 1
    else:
        r = m
print(max(l, game_max))