#  1021
from collections import deque
from sys import stdin

n, m = map(int, stdin.readline().split())
pickList = list(map(int, stdin.readline().split()))
q = deque(range(1, n + 1))

cnt = 0

for i in range(len(pickList)):
    if pickList[i] == q[0]:
        q.popleft()
        continue
    q_i = q.index(pickList[i])

    if q_i > len(q) // 2:
        q.rotate(len(q) - q_i)
        cnt += len(q) - q_i
    elif q_i <= len(q) // 2:
        q.rotate(-q_i)
        cnt += q_i
    q.popleft()

print(cnt)
