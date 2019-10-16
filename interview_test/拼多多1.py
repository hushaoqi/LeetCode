from collections import Counter
import sys
N, K = map(int, input().split())
number = list(input())
number = list(map(int, number))
result = Counter(number)
print(result)
