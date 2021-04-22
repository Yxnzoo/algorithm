# 2562

a = []

for _ in range(0, 9):
    a.append(int(input()))

print(max(a))
print(a.index(max(a))+1)
