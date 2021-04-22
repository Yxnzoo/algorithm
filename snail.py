#  1913

n = int(input())
list = []

for i in range(0, n ** 2):
    list.append(i + 1)

list.reverse()

array = [[0 for col in range(n)] for row in range(n)]

row = 0
col = 0

sr = 0
sc = 0
er = n - 1
ec = n - 1

# for i in list:
#
#     array[row][col] = i
#
#     if sr <= row <= er:
#         col += 1
#         sr += 1
#     if col == ec:
#         row -= 1
#     if row == sr:
#         col -= 1
#         ec -= 1
#     if
#
# print(array)
