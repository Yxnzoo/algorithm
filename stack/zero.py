#  10773
from sys import stdin

k = int(stdin.readline())
left = []

for _ in range(k):
    n = int(stdin.readline())
    if n == 0:
        left.pop()
    else:
        left.append(n)


print(sum(left))