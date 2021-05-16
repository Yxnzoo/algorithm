# 9012

from sys import stdin

n = int(stdin.readline())
for i in range(n):
    s = stdin.readline().strip()
    sum = 0
    for j in s:
        if j == '(':
            sum += 1
        elif j == ')':
            sum -= 1
        if sum < 0:
            print('NO')
            break
    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')
