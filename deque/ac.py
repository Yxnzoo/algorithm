#  5430
from collections import deque
from sys import stdin

t = int(stdin.readline())

for _ in range(t):
    rev = False
    p = stdin.readline().rstrip()
    al = int(stdin.readline())
    string = stdin.readline().lstrip('[').rstrip(']\n').split(',')
    arr = deque(string)
    if len(arr) < p.count('D') or arr[0] == '' and p.count('D') > 0:
        print('error')
        continue
    for i in p:
        if i == 'R':
            rev = not rev
        elif i == 'D':
            if rev:
                arr.pop()
            else:
                arr.popleft()
    if rev:
        arr.reverse()
    print('[' + ','.join(arr) + ']')
