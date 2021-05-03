#  10866
from collections import deque
from sys import stdin

n = int(stdin.readline())
d = deque([])
for _ in range(n):
    w = stdin.readline().split()
    if w[0].__eq__('push_front'):
        d.appendleft(w[1])
    elif w[0].__eq__('push_back'):
        d.append(w[1])
    elif w[0].__eq__('pop_front'):
        if d:
            print(d.popleft())
        else:
            print(-1)
    elif w[0].__eq__('pop_back'):
        if d:
            print(d.pop())
        else:
            print(-1)
    elif w[0].__eq__('size'):
        print(len(d))
    elif w[0].__eq__('empty'):
        if d:
            print(0)
        else:
            print(1)
    elif w[0].__eq__('front'):
        if d:
            print(d[0])
        else:
            print(-1)
    elif w[0].__eq__('back'):
        if d:
            print(d[-1])
        else:
            print(-1)
