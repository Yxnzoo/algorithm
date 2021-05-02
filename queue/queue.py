#  10845
from sys import stdin
import re

n = int(stdin.readline())
q = []
for _ in range(n):
    word = stdin.readline().strip()
    if word.__contains__('push'):
        n = re.findall('\d+', word)[0]
        q.append(n)
    elif word.__contains__('front'):
        if q:
            print(q[0])
        else:
            print(-1)
    elif word.__contains__('pop'):
        if q:
            print(q.pop(0))
        else:
            print(-1)
    elif word.__contains__('size'):
        print(len(q))
    elif word.__contains__('back'):
        if q:
            print(q[-1])
        else:
            print(-1)
    elif word.__contains__('empty'):
        if q:
            print(0)
        else:
            print(1)
