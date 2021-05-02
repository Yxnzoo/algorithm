#  2164
from sys import stdin
from collections import deque

n = int(stdin.readline())
q = deque([i for i in range(n, 0, -1)])

while len(q) > 0:
    if len(q) == 1:
        break
    q.pop()
    q.appendleft(q.pop())

print(q.pop())
