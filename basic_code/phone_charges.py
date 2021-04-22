#  1267

n = int(input())
slist = list(map(int, input().split()))

ycnt = 0
mcnt = 0

for i in slist:
    ycnt += i // 30 * 10 + 10
    mcnt += i // 60 * 15 + 15

if ycnt > mcnt:
    print("M", int(mcnt))
elif ycnt < mcnt:
    print("Y", int(ycnt))
else:
    print("Y", "M", int(ycnt))
