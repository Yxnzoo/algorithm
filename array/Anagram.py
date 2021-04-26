#  1919
# import string
# import sys
#
# a = sys.stdin.readline().rstrip()
# b = sys.stdin.readline().rstrip()
# alphabet = string.ascii_lowercase
#
# array = [[0] * len(alphabet) for _ in range(3)]
#
# cnt = 0
#
# for i in range(0, len(alphabet)):
#     array[0][i] = alphabet[i]
#
# for i in alphabet:
#     for j in range(0, len(a)):
#         if i == a[j]:
#             array[1][alphabet.index(i)] += 1
#     for k in range(0, len(b)):
#         if i == b[k]:
#             array[2][alphabet.index(i)] += 1
#
# for i in range(0, len(alphabet)):
#     if array[1][i] != 0 and array[1][i] == array[2][i]:
#         cnt += array[1][i] * 2
#
# add = len(a) + len(b)
# add = add - cnt
#
# print(add)

str_a = input()
str_b = input()
res = 0
for i in range(97, 123):
    res += abs(str_a.count(chr(i)) - str_b.count(chr(i)))
print(res)
