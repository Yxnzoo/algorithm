# 2480

a, b, c = map(int, input().split())
cnt = 0
if a == b == c:
    cnt = 10000 + a * 1000
elif a == b or a == c or b == c:
    if a == b or a == c:
        cnt = 1000 + a * 100
    else:
        cnt = 1000 + b * 100
else:
    cnt = max(a, b, c) * 100

print(cnt)
