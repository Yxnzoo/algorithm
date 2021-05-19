#  1110

n = int(input())
check = n
new_num = 0
temp = 0
cnt = 0
while True:
    temp = n // 10 + n % 10
    new_num = (n % 10) * 10 + temp % 10
    cnt += 1
    num = new_num
    if new_num == check:
        break
print(cnt)
