import sys

n = 1
while True:
    s = sys.stdin.readline().strip()
    if s[0] == '-':
        break
    stk = 0
    cnt = 0
    for i in range(len(s)):
        if stk == 0 and s[i] == '}':
            cnt += 1
            stk += 1
        elif s[i] == '}':
            stk -= 1
        elif s[i] == '{':
            stk += 1
    print(f'{n}. {cnt+int(stk/2)}')
    n += 1