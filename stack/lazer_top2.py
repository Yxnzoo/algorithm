#  2493 시간초과
from sys import stdin

n = int(stdin.readline())
topHigh = list(map(int, stdin.readline().split()))

s = []
high = 0

for i in range(n - 1, 0, -1):
    for j in range(n - 2, -1, -1):
        if topHigh[i] < topHigh[j] and i > j:
            s.append(j + 1)
            break
        else:
            if j == 0:
                s.append(0)
s.append(0)

for _ in range(0, len(s)):
    print(s.pop(), end=' ')
