#  2441
import sys

n = int(sys.stdin.readline())

for i in range(n, 0, -1):
    print(' ' * (n - i)+'*' * i)
