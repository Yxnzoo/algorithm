# 10093

a, b = map(int, input().split())

# alist = []
#
# for i in range(a + 1, b):
#     alist.append(i)
#
# print(len(alist))
# for j in alist:
#     print(j, end=" ")

a, b = min(a, b), max(a, b)
cnt = 0
if a != b:
    cnt = b-a-1
print(cnt)

for j in range(a + 1, b):
    print(j, end=" ")
