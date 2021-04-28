#  1874 스택수열

n = int(input())
s, op = [], []
count = 1
temp = True

for _ in range(n):
    num = int(input())
    while count <= num:
        s.append(count)
        op.append('+')
        count += 1
    if s[-1] == num:
        s.pop()
        op.append('-')
    else:
        temp = False
if not temp:
    print('NO')
else:
    for i in op:
        print(i)
