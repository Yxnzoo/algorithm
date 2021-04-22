import sys

n = int(sys.stdin.readline())
j = (2 * (n - 1))

for i in range(1, n):
    print('*' * i + ' ' * j + '*' * i)
    j -= 2

for i in range(n, 0, -1):
    print('*' * i + ' ' * j + '*' * i)
    j += 2
