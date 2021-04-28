#  10828
import re
from sys import stdin

n = int(stdin.readline())
left = []

for _ in range(n):
    order = stdin.readline().strip()
    if order.__contains__('push'):
        n = re.findall('\d+', order)
        left.append(n[0])
    elif order.__contains__('pop'):
        if not left:
            print(-1)
        else:
            print(left.pop())
    elif order.__contains__('size'):
        print(len(left))
    elif order.__contains__('empty'):
        if not left:
            print("1")
        else:
            print("0")
    elif order.__contains__('top'):
        if not left:
            print("-1")
        else:
            print(left[-1])
