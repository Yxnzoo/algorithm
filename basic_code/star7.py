import sys

n = int(sys.stdin.readline())
j = (2 * (n - 1)) + 1
k = 1

for i in range(1, n):
    print(' ' * (n - i) + '*' * k)
    k += 2

for i in range(n + 1, 0, -1):
    print(' ' * (n + 1 - i) + '*' * j)
    j -= 2
