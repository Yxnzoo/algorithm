import sys

n = int(sys.stdin.readline())
j = 1

for i in range(1, n+1):
    print(' ' * (n - i) + '*' * j)
    j += 2
