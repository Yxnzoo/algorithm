#  2475

sum = 0
numlist = map(int, input().split())

for i in numlist:
    sum += i ** 2

print(sum % 10)
