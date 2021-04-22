# 2587

a = []

for _ in range(0,5):
    a.append(int(input()))

a.sort()

avg = 0
center = a[2]


for i in a:
    avg += int(i / 5)

print(avg)
print(center)