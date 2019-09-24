arr = list(map(int, input().strip().split()))
n = arr[0]
m = arr[1]
shudui = []
for i in range(m):
    a = list(map(int, input().strip().split()))
    shudui.append(a[0])
    shudui.append(a[1])
red = set()
blue = set()
for i in range(0, len(shudui), 2):
    if (shudui[i] not in red) and (shudui[i] not in blue):
        red.add(shudui[i])
        if shudui[i + 1] not in blue:
            blue.add(shudui[i + 1])

    elif shudui[i] in blue:
        if (shudui[i + 1] not in red) and (shudui[i + 1] not in blue):
            red.add(shudui[i + 1])
        elif shudui[i + 1] in blue:
            n -= 1

    elif shudui[i] in red:
        if (shudui[i + 1] not in red) and (shudui[i + 1] not in blue):
            blue.add(shudui[i + 1])
        elif shudui[i + 1] in red:
            n -= 1

if n % 2 == 0:
    print(n)
else:
    print(n - 1)