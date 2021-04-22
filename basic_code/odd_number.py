# 2576

a = []

for _ in range(0, 7):
    a.append(int(input()))

cnt = 0
min_num = max(a)

for i in a:
    if i % 2 == 1:
        cnt += i
        if min_num > i:
            min_num = i

if cnt == 0:
    cnt = -1
    print(cnt)
else:
    print(cnt)
    print(min_num)
