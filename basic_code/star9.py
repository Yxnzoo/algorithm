import sys

n = int(sys.stdin.readline())
j = (2 * (n - 1))+1

for i in range(0, n-1):
    print(' '*i+'*'*j)
    j -= 2

for i in range(n, 0, -1):
    print(' '*(i-1)+'*'*j)
    j += 2