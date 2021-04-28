#  2493
from sys import stdin

n = int(stdin.readline())
topHigh = list(map(int, stdin.readline().split()))
stack, answer = [], []

for i in range(n):
    while stack:
        if stack[-1][1] > topHigh[i]:
            answer.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    if not stack:
        answer.append(0)
    stack.append([i, topHigh[i]])

print(" ".join(map(str, answer)))
