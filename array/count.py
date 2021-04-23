#  10807
import sys

n = int(sys.stdin.readline())
v1 = list(map(int, sys.stdin.readline().split()))
v = int(sys.stdin.readline())

cnt = 0
for i in v1:
    if i == v:
        cnt += 1

print(cnt)