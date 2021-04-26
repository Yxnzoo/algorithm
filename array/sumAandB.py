# 3273
# 이진트리
import sys

n = int(sys.stdin.readline())
arr = sorted(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())

count = 0

i = 0
j = n - 1

while i != j:
    s = arr[i] + arr[j]
    if s == x:
        count += 1
        i += 1
    elif s > x:
        j -= 1
    else:
        i += 1

print(count)
